import streamlit as st
import random
import datetime
from core.utils import topbar, questions, score_color

def show_medical():
    topbar("Equipo Clínico 🏥", "medical")

    st.markdown("""
    <div class="medical-header">Resumen de pacientes</div>
    <div style="color:#8a9ab0;font-size:0.95rem;margin-bottom:1.5rem;">
        Centro de Memoria Los Almendros · Semana del {week}
    </div>
    """.format(week=datetime.datetime.now().strftime("%b %d, %Y")), unsafe_allow_html=True)

    tabs = st.tabs(["👥  Todos los pacientes", "📈  Análisis", "⚙️  Configuración"])

    patients = st.session_state.patients

    # ── ALL PATIENTS TAB ──
    with tabs[0]:
        col_filter, _ = st.columns([2, 3])
        with col_filter:
            status_filter = st.selectbox("Filtrar por estado", ["Todos", "Estable", "Necesita atención", "Día difícil"],
                                         label_visibility="collapsed")

        status_map = {"Todos": None, "Estable": "stable", "Necesita atención": "concern", "Día difícil": "hard"}
        filtered = patients if status_filter == "Todos" else [p for p in patients if p["status"] == status_map[status_filter]]

        for p in filtered:
            col_card, col_action = st.columns([4, 1])
            with col_card:
                trend_html = f'<span class="trend-up">▲ {p["trend"]}</span>' if "+" in p["trend"] \
                    else f'<span class="trend-down">▼ {p["trend"]}</span>'
                st.markdown(f"""
                <div class="patient-card {p['status']}">
                    <div class="patient-avatar" style="background:{'#e8f4ef' if p['status']=='stable'
                        else '#fef8e8' if p['status']=='concern' else '#fef0ee'};">
                        {p['avatar']}
                    </div>
                    <div style="flex:1;">
                        <div class="patient-name">{p['name']} <span style="color:#b0a0b0;font-weight:400;font-size:0.85rem;">· {p['age']} yrs</span></div>
                        <div class="patient-meta">Última sesión: {p['last']} &nbsp;·&nbsp; {p['sessions_week']} sesiones esta semana</div>
                    </div>
                    <div style="text-align:right;min-width:110px;">
                        <div style="font-family:'Fraunces',serif;font-size:1.6rem;font-weight:300;
                                    color:{score_color(p['score_week'])};">{p['score_week']}%</div>
                        <div style="font-size:0.8rem;">{trend_html}</div>
                    </div>
                    <div>
                        <span class="status-badge {p['status']}">
                            {'Estable' if p['status']=='stable' else 'Atención' if p['status']=='concern' else 'Día difícil'}
                        </span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with col_action:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Ver", key=f"view_{p['name']}", use_container_width=True):
                    st.info(f"📋 Vista de detalle del paciente para **{p['name']}** — integración completa con EHR en producción.")

    # ── ANALYTICS TAB ──
    with tabs[1]:
        c1, c2, c3, c4 = st.columns(4)
        facility_metrics = [
            ("4.2", "Sesiones / paciente", "#3d5a80", "esta semana"),
            ("64%", "Precisión promedio del centro", score_color(64), "↑ 3% vs la semana pasada"),
            ("2", "Pacientes que necesitan revisión", "#c4503a", "Robert y James"),
            ("83%", "Tasa de finalización de sesiones", "#2d7a5f", "↑ 5% vs la semana pasada"),
        ]
        for col, (val, label, color, sub) in zip([c1, c2, c3, c4], facility_metrics):
            with col:
                st.markdown(f"""
                <div class="analytics-card">
                    <div class="analytics-number" style="color:{color};">{val}</div>
                    <div class="analytics-label">{label}</div>
                    <div style="font-size:0.75rem;color:#a0b0c0;margin-top:0.3rem;">{sub}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col_chart, col_dist = st.columns([3, 2], gap="large")

        with col_chart:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📅 Precisión semanal por paciente</div>', unsafe_allow_html=True)
            # Mini bar chart via HTML
            chart_html = '<div style="display:flex;flex-direction:column;gap:0.6rem;">'
            for p in patients:
                bar_color = score_color(p['score_week'])
                chart_html += f"""
                <div style="display:flex;align-items:center;gap:0.8rem;font-size:0.85rem;">
                    <span style="min-width:90px;color:#4a5060;">{p['name'].split()[0]} {p['name'].split()[1][0]}.</span>
                    <div style="flex:1;background:#f0f2f5;border-radius:100px;height:10px;">
                        <div style="width:{p['score_week']}%;background:{bar_color};border-radius:100px;height:10px;"></div>
                    </div>
                    <span style="min-width:38px;text-align:right;font-weight:600;color:{bar_color};">{p['score_week']}%</span>
                </div>
                """
            chart_html += '</div>'
            st.markdown(chart_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_dist:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🩺 Distribución de estados</div>', unsafe_allow_html=True)
            
            # CORRECCIÓN AQUÍ: Claves en inglés para coincidir con la base de datos
            statuses = {"stable": 0, "concern": 0, "hard": 0}
            for p in patients:
                statuses[p["status"]] += 1
            total_p = len(patients)
            
            for status, count in statuses.items():
                # CORRECCIÓN AQUÍ: Traducción visual al iterar
                label = {"stable": "Estable 🟢", "concern": "Necesita atención 🟡", "hard": "Día difícil 🔴"}[status]
                color = {"stable": "#2d7a5f", "concern": "#b87d0d", "hard": "#c4503a"}[status]
                pct = int(count / total_p * 100) if total_p > 0 else 0
                
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:0.8rem;font-size:0.88rem;">
                    <span style="min-width:120px;color:#4a5060;">{label}</span>
                    <div style="flex:1;background:#f0f2f5;border-radius:100px;height:8px;">
                        <div style="width:{pct}%;background:{color};border-radius:100px;height:8px;"></div>
                    </div>
                    <span style="min-width:20px;font-weight:600;color:{color};">{count}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ── CONFIGURATION TAB ──
    with tabs[2]:
        col_cfg1, col_cfg2 = st.columns(2, gap="large")
        with col_cfg1:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🏥 Predeterminados del centro</div>', unsafe_allow_html=True)
            st.selectbox("Dificultad predeterminada", ["Fácil", "Medio", "Difícil"], index=1)
            st.slider("Sesiones predeterminadas por día", 1, 5, 2)
            st.slider("Preguntas predeterminadas por sesión", 5, 20, 10)
            st.toggle("Permitir que la familia ajuste la configuración", value=True)
            st.toggle("Marcar automáticamente a los pacientes por debajo del 40%", value=True)
            if st.button("Guardar predeterminados del centro", type="primary"):
                st.success("Predeterminados guardados en todos los pacientes ✓")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_cfg2:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📤 Informes y alertas</div>', unsafe_allow_html=True)
            st.toggle("Enviar informe PDF semanal al equipo médico", value=True)
            st.toggle("Alertar sobre sesiones perdidas (más de 2 días)", value=True)
            st.toggle("Enviar resumen diario al personal de atención", value=False)
            st.text_input("Email del equipo médico", value="[EMAIL_ADDRESS]")
            st.selectbox("Entrega de informes", ["Semanal (lunes)", "Diario", "Mensual"])
            if st.button("Guardar configuración de informes"):
                st.success("Configuración de informes actualizada ✓")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">👤 Ajustes de override por paciente</div>', unsafe_allow_html=True)
        sel_patient = st.selectbox("Seleccionar paciente", [p["name"] for p in patients])
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.selectbox("Dificultad", ["Fácil", "Medio", "Difícil"], key="p_diff")
        with col_p2:
            st.slider("Sesiones / día", 1, 5, 2, key="p_sess")
        with col_p3:
            st.slider("Preguntas / sesión", 5, 20, 10, key="p_qlen")
        if st.button(f"Aplicar a {sel_patient}", type="primary"):
            st.success(f"Ajustes aplicados a {sel_patient} ✓")
        st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
import random
import datetime
from core.utils import topbar, questions, score_color

def show_family():
    topbar("Portal Familiar 🏡", "family")

    st.markdown(f"""
    <div class="family-header">Hola familia 👋  </div>
    <div style="color:#6a8070;font-size:1rem;margin-bottom:1.5rem;">
        Aquí tienes un resumen de cómo está <strong>{st.session_state.elder_name}</strong> esta semana.
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["📊  Resumen", "📬  Enviar una nota", "⚙️  Configuración"])

    # ── OVERVIEW TAB ──
    with tabs[0]:
        sessions = st.session_state.sessions
        correct_list = [s["score"] for s in sessions]
        total_correct = sum(correct_list)
        total_q = sum(s["total"] for s in sessions)
        avg_pct = int(total_correct / total_q * 100) if total_q else 0
        streak = sum(1 for s in sessions if s["score"] / s["total"] >= 0.6)

        c1, c2, c3, c4 = st.columns(4)
        metrics = [
            (str(len(sessions)), "Sesiones esta semana", "#2d7a5f"),
            (f"{avg_pct}%", "Precisión media", score_color(avg_pct)),
            (str(streak), "Días por encima del 60%", "#3d5a80"),
            ("12 min", "Duración media", "#b87d0d"),
        ]
        for col, (val, label, color) in zip([c1, c2, c3, c4], metrics):
            with col:
                st.markdown(f"""
                <div class="analytics-card">
                    <div class="analytics-number" style="color:{color};">{val}</div>
                    <div class="analytics-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col_hist, col_mood = st.columns([2, 1], gap="large")

        with col_hist:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📅 Session History</div>', unsafe_allow_html=True)
            for s in sessions:
                pct = int(s["score"] / s["total"] * 100)
                color = score_color(pct)
                bar_w = pct
                st.markdown(f"""
                <div class="session-row">
                    <span style="min-width:60px;color:#6a6060;">{s['date']}</span>
                    <span style="flex:1;margin:0 1rem;">
                        <div style="background:#f0ebe3;border-radius:100px;height:8px;">
                            <div style="width:{bar_w}%;background:{color};border-radius:100px;height:8px;"></div>
                        </div>
                    </span>
                    <span style="color:{color};font-weight:600;min-width:40px;">{pct}%</span>
                    <span style="min-width:28px;">{s['mood']}</span>
                    <span style="color:#b0a090;font-size:0.8rem;min-width:60px;">{s['duration']}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_mood:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">💬 Recent Notes</div>', unsafe_allow_html=True)
            for note in st.session_state.notes[:3]:
                st.markdown(f"""
                <div class="note-bubble" style="margin-top:1.2rem;">
                    {note['text']}
                    <div style="font-size:0.75rem;color:#b0a090;margin-top:0.5rem;">
                        {note['from']} · {note['time']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ── NOTES TAB ──
    with tabs[1]:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">📬 Enviar una nota a {st.session_state.elder_name}</div>',
                    unsafe_allow_html=True)
        st.caption("Tu nota aparecerá en su pantalla durante la próxima sesión, un pequeño recordatorio cariñoso de que la quieres.")
        note_text = st.text_area("Escribe tu mensaje…", height=100, placeholder="Hola mamá, ¡pensando en ti! 💛",
                                 label_visibility="collapsed")
        col_a, col_b = st.columns([1, 3])
        with col_a:
            if st.button("Enviar nota 💌", type="primary", use_container_width=True):
                if note_text.strip():
                    new_note = {
                        "from": "Familia",
                        "text": note_text.strip(),
                        "time": "Justo ahora"
                    }
                    st.session_state.notes.insert(0, new_note)
                    st.success("✅ Tu nota fue enviada. Aparecerá en la próxima sesión.")
                else:
                    st.warning("Por favor, escribe algo antes.")
        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.notes:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📜 Notas enviadas</div>', unsafe_allow_html=True)
            for note in st.session_state.notes:
                st.markdown(f"""
                <div class="note-bubble" style="margin-top:1.2rem;">
                    {note['text']}
                    <div style="font-size:0.75rem;color:#b0a090;margin-top:0.5rem;">
                        {note['from']} · {note['time']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ── SETTINGS TAB ──
    with tabs[2]:
        col_s1, col_s2 = st.columns(2, gap="large")
        with col_s1:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🎛️ Ajustes de sesión</div>', unsafe_allow_html=True)
            st.session_state.difficulty = st.selectbox(
                "Nivel de dificultad",
                ["Fácil", "Normal", "Difícil"],
                index=["Fácil", "Normal", "Difícil"].index(st.session_state.difficulty)
            )
            st.session_state.daily_sessions = st.slider(
                "Sesiones por día", 1, 5, st.session_state.daily_sessions
            )
            st.session_state.session_length = st.slider(
                "Preguntas por sesión", 5, 20, st.session_state.session_length
            )
            if st.button("Guardar cambios", type="primary"):
                st.success("Ajustes actualizados ✓")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_s2:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🔔 Notificaciones</div>', unsafe_allow_html=True)
            st.toggle("Enviar resumen diario por email", value=True)
            st.toggle("Enviar alerta si se pierde una sesión", value=True)
            st.toggle("Enviar alerta si la precisión baja del 40%", value=False)
            st.text_input("Tu email", value="[EMAIL_ADDRESS]")
            if st.button("Guardar notificaciones"):
                st.success("Preferencias de notificación guardadas ✓")
            st.markdown('</div>', unsafe_allow_html=True)
    pass
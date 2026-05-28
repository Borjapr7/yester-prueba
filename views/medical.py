import streamlit as st
import random
import datetime
from core.utils import topbar, questions, score_color

def show_medical():
    topbar("Care Team 🏥", "medical")

    st.markdown("""
    <div class="medical-header">Patient Overview</div>
    <div style="color:#8a9ab0;font-size:0.95rem;margin-bottom:1.5rem;">
        Cedar Grove Memory Care Centre · Week of {week}
    </div>
    """.format(week=datetime.datetime.now().strftime("%b %d, %Y")), unsafe_allow_html=True)

    tabs = st.tabs(["👥  All Patients", "📈  Analytics", "⚙️  Configuration"])

    patients = st.session_state.patients

    # ── ALL PATIENTS TAB ──
    with tabs[0]:
        col_filter, _ = st.columns([2, 3])
        with col_filter:
            status_filter = st.selectbox("Filter by status", ["All", "Stable", "Needs Attention", "Hard Day"],
                                         label_visibility="collapsed")

        status_map = {"All": None, "Stable": "stable", "Needs Attention": "concern", "Hard Day": "hard"}
        filtered = patients if status_filter == "All" else [p for p in patients if p["status"] == status_map[status_filter]]

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
                        <div class="patient-meta">Last session: {p['last']} &nbsp;·&nbsp; {p['sessions_week']} sessions this week</div>
                    </div>
                    <div style="text-align:right;min-width:110px;">
                        <div style="font-family:'Fraunces',serif;font-size:1.6rem;font-weight:300;
                                    color:{score_color(p['score_week'])};">{p['score_week']}%</div>
                        <div style="font-size:0.8rem;">{trend_html}</div>
                    </div>
                    <div>
                        <span class="status-badge {p['status']}">
                            {'Stable' if p['status']=='stable' else 'Attention' if p['status']=='concern' else 'Hard Day'}
                        </span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with col_action:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("View", key=f"view_{p['name']}", use_container_width=True):
                    st.info(f"📋 Patient detail view for **{p['name']}** — full EHR integration in production.")

    # ── ANALYTICS TAB ──
    with tabs[1]:
        c1, c2, c3, c4 = st.columns(4)
        facility_metrics = [
            ("4.2", "Avg sessions / patient", "#3d5a80", "this week"),
            ("64%", "Facility avg. accuracy", score_color(64), "↑ 3% vs last week"),
            ("2", "Patients needing review", "#c4503a", "Robert & James"),
            ("83%", "Session completion rate", "#2d7a5f", "↑ 5% vs last week"),
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
            st.markdown('<div class="section-title">📅 Weekly Accuracy per Patient</div>', unsafe_allow_html=True)
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
            st.markdown('<div class="section-title">🩺 Status Distribution</div>', unsafe_allow_html=True)
            statuses = {"stable": 0, "concern": 0, "hard": 0}
            for p in patients:
                statuses[p["status"]] += 1
            total_p = len(patients)
            for status, count in statuses.items():
                label = {"stable": "Stable 🟢", "concern": "Needs Attention 🟡", "hard": "Hard Day 🔴"}[status]
                color = {"stable": "#2d7a5f", "concern": "#b87d0d", "hard": "#c4503a"}[status]
                pct = int(count / total_p * 100)
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
            st.markdown('<div class="section-title">🏥 Facility Defaults</div>', unsafe_allow_html=True)
            st.selectbox("Default difficulty", ["Easy", "Medium", "Hard"], index=1)
            st.slider("Default sessions per day", 1, 5, 2)
            st.slider("Default questions per session", 5, 20, 10)
            st.toggle("Allow family to adjust settings", value=True)
            st.toggle("Auto-flag patients below 40%", value=True)
            if st.button("Save Facility Defaults", type="primary"):
                st.success("Defaults saved across all patients ✓")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_cfg2:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📤 Reports & Alerts</div>', unsafe_allow_html=True)
            st.toggle("Weekly PDF report to medical team", value=True)
            st.toggle("Alert on missed sessions (2+ days)", value=True)
            st.toggle("Daily summary to care staff", value=False)
            st.text_input("Medical team email", value="team@cedargrove.care")
            st.selectbox("Report delivery", ["Weekly (Monday)", "Daily", "Monthly"])
            if st.button("Save Report Settings"):
                st.success("Report settings updated ✓")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">👤 Override Settings per Patient</div>', unsafe_allow_html=True)
        sel_patient = st.selectbox("Select patient", [p["name"] for p in patients])
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.selectbox("Difficulty", ["Easy", "Medium", "Hard"], key="p_diff")
        with col_p2:
            st.slider("Sessions / day", 1, 5, 2, key="p_sess")
        with col_p3:
            st.slider("Questions / session", 5, 20, 10, key="p_qlen")
        if st.button(f"Apply to {sel_patient}", type="primary"):
            st.success(f"Settings applied to {sel_patient} ✓")
        st.markdown('</div>', unsafe_allow_html=True)
    pass
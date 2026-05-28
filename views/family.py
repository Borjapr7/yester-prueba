import streamlit as st
import random
import datetime
from core.utils import topbar, questions, score_color

def show_family():
    topbar("Family View 🏡", "family")

    st.markdown(f"""
    <div class="family-header">Hi Susan 👋</div>
    <div style="color:#6a8070;font-size:1rem;margin-bottom:1.5rem;">
        Here's how <strong>{st.session_state.elder_name}</strong> is doing this week.
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["📊  Overview", "📬  Send a Note", "⚙️  Settings"])

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
            (str(len(sessions)), "Sessions this week", "#2d7a5f"),
            (f"{avg_pct}%", "Avg. accuracy", score_color(avg_pct)),
            (str(streak), "Days above 60%", "#3d5a80"),
            ("12 min", "Avg. duration", "#b87d0d"),
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
        st.markdown(f'<div class="section-title">📬 Send a message to {st.session_state.elder_name}</div>',
                    unsafe_allow_html=True)
        st.caption("Your note will appear on her screen during her next session — a little warm reminder she's loved.")
        note_text = st.text_area("Write your message…", height=100, placeholder="Hi Mum, thinking of you! 💛",
                                 label_visibility="collapsed")
        col_a, col_b = st.columns([1, 3])
        with col_a:
            if st.button("Send Note 💌", type="primary", use_container_width=True):
                if note_text.strip():
                    new_note = {
                        "from": "Susan (daughter)",
                        "text": note_text.strip(),
                        "time": "Just now"
                    }
                    st.session_state.notes.insert(0, new_note)
                    st.success("✅ Your note was sent! It will appear on her next session.")
                else:
                    st.warning("Please write something first.")
        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.notes:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📜 Sent Notes</div>', unsafe_allow_html=True)
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
            st.markdown('<div class="section-title">🎛️ Session Settings</div>', unsafe_allow_html=True)
            st.session_state.difficulty = st.selectbox(
                "Difficulty level",
                ["Easy", "Medium", "Hard"],
                index=["Easy", "Medium", "Hard"].index(st.session_state.difficulty)
            )
            st.session_state.daily_sessions = st.slider(
                "Sessions per day", 1, 5, st.session_state.daily_sessions
            )
            st.session_state.session_length = st.slider(
                "Questions per session", 5, 20, st.session_state.session_length
            )
            if st.button("Save Settings", type="primary"):
                st.success("Settings updated ✓")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_s2:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🔔 Notifications</div>', unsafe_allow_html=True)
            st.toggle("Email me daily summary", value=True)
            st.toggle("Alert if session is missed", value=True)
            st.toggle("Alert if score drops below 40%", value=False)
            st.text_input("Your email", value="susan@example.com")
            if st.button("Save Notifications"):
                st.success("Notification preferences saved ✓")
            st.markdown('</div>', unsafe_allow_html=True)
    pass
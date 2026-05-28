import streamlit as st
import random
import datetime
import time

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Memoria",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  GLOBAL STYLES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;0,600;1,300&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background: #faf7f2;
}
header[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}
/* Hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
div[data-testid="stToolbar"] { display: none; }

/* ── LANDING ── */
.landing-hero {
    text-align: center;
    padding: 3rem 1rem 2rem;
}
.landing-logo {
    font-family: 'Fraunces', serif;
    font-size: 4rem;
    font-weight: 300;
    color: #2d2318;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.landing-logo span { color: #c4753a; }
.landing-tagline {
    font-size: 1.1rem;
    color: #8a7060;
    font-weight: 300;
    margin-bottom: 3rem;
    font-style: italic;
}
.mode-card {
    background: white;
    border-radius: 20px;
    padding: 2.2rem 1.8rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.25s ease;
    border: 2px solid transparent;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    height: 100%;
}
.mode-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}
.mode-card.elder { border-color: #e8c4a0; }
.mode-card.family { border-color: #a8c4b8; }
.mode-card.medical { border-color: #a0aec0; }
.mode-icon { font-size: 3rem; margin-bottom: 1rem; }
.mode-title {
    font-family: 'Fraunces', serif;
    font-size: 1.6rem;
    font-weight: 400;
    color: #2d2318;
    margin-bottom: 0.5rem;
}
.mode-desc { font-size: 0.9rem; color: #8a7060; line-height: 1.5; }

/* ── TOPBAR ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.8rem 1.5rem;
    background: white;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.topbar-logo {
    font-family: 'Fraunces', serif;
    font-size: 1.6rem;
    font-weight: 400;
    color: #2d2318;
}
.topbar-logo span { color: #c4753a; }
.topbar-mode {
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 100px;
}
.topbar-mode.elder { background: #fef3e8; color: #c4753a; }
.topbar-mode.family { background: #e8f4ef; color: #2d7a5f; }
.topbar-mode.medical { background: #edf2f7; color: #3d5a80; }

/* ── ELDER MODE ── */
.elder-greeting {
    font-family: 'Fraunces', serif;
    font-size: 2.6rem;
    font-weight: 300;
    color: #2d2318;
    text-align: center;
    margin-bottom: 0.4rem;
}
.elder-subtext {
    font-size: 1.25rem;
    color: #8a7060;
    text-align: center;
    margin-bottom: 2rem;
}
.photo-frame {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
    text-align: center;
}
.photo-placeholder {
    width: 100%;
    height: 280px;
    background: linear-gradient(135deg, #fde8d0 0%, #f5cfa8 50%, #e8b88a 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.photo-question {
    font-family: 'Fraunces', serif;
    font-size: 1.8rem;
    font-weight: 400;
    color: #2d2318;
    margin-bottom: 1.5rem;
    line-height: 1.3;
}
.answer-btn-correct {
    background: #2d7a5f !important;
    color: white !important;
    border-radius: 14px !important;
    font-size: 1.1rem !important;
    padding: 0.7rem !important;
    border: none !important;
    width: 100%;
    font-family: 'DM Sans', sans-serif;
}
.answer-btn-wrong {
    background: #f5f5f5 !important;
    color: #2d2318 !important;
    border-radius: 14px !important;
    font-size: 1.1rem !important;
    padding: 0.7rem !important;
    border: 2px solid #e5e5e5 !important;
    width: 100%;
    font-family: 'DM Sans', sans-serif;
}
.feedback-success {
    background: linear-gradient(135deg, #e8f5ee, #d0eedd);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    border-left: 5px solid #2d7a5f;
}
.feedback-fail {
    background: linear-gradient(135deg, #fef5ee, #fde8d8);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    border-left: 5px solid #c4753a;
}
.feedback-emoji { font-size: 3rem; }
.feedback-text {
    font-family: 'Fraunces', serif;
    font-size: 1.6rem;
    color: #2d2318;
    margin-top: 0.5rem;
}
.streak-bar {
    background: white;
    border-radius: 16px;
    padding: 1rem 1.5rem;
    display: flex;
    gap: 0.6rem;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}
.streak-dot {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: inline-block;
}
.streak-dot.correct { background: #2d7a5f; }
.streak-dot.wrong { background: #c4753a; }
.streak-dot.empty { background: #e5e0d8; }

/* ── FAMILY MODE ── */
.family-header {
    font-family: 'Fraunces', serif;
    font-size: 2rem;
    font-weight: 400;
    color: #1a3830;
    margin-bottom: 0.3rem;
}
.section-card {
    background: white;
    border-radius: 20px;
    padding: 1.8rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    margin-bottom: 1rem;
}
.section-title {
    font-family: 'Fraunces', serif;
    font-size: 1.2rem;
    font-weight: 400;
    color: #2d2318;
    margin-bottom: 1rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid #f0ebe3;
}
.stat-chip {
    background: #e8f4ef;
    color: #2d7a5f;
    border-radius: 100px;
    padding: 0.3rem 0.9rem;
    font-size: 0.85rem;
    font-weight: 600;
    display: inline-block;
    margin: 0.2rem;
}
.stat-chip.warn {
    background: #fef3e8;
    color: #c4753a;
}
.stat-chip.info {
    background: #edf2f7;
    color: #3d5a80;
}
.note-bubble {
    background: #fffbf5;
    border: 1px solid #f0e4d0;
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
    font-size: 0.95rem;
    color: #4a3728;
    position: relative;
}
.note-bubble::before {
    content: '📝';
    position: absolute;
    top: -10px;
    left: 14px;
    font-size: 1.1rem;
}
.session-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.7rem 0;
    border-bottom: 1px solid #f5f0e8;
    font-size: 0.9rem;
}
.session-row:last-child { border-bottom: none; }
.progress-ring {
    text-align: center;
    padding: 1rem;
}
.big-number {
    font-family: 'Fraunces', serif;
    font-size: 3.5rem;
    font-weight: 300;
    color: #2d7a5f;
    line-height: 1;
}
.big-label {
    font-size: 0.8rem;
    color: #8a7060;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.3rem;
}

/* ── MEDICAL MODE ── */
.medical-header {
    font-family: 'Fraunces', serif;
    font-size: 2rem;
    font-weight: 400;
    color: #1a2a3a;
    margin-bottom: 0.3rem;
}
.patient-card {
    background: white;
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 0.8rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    gap: 1rem;
    border-left: 4px solid transparent;
}
.patient-card.stable { border-color: #2d7a5f; }
.patient-card.concern { border-color: #e6a817; }
.patient-card.hard { border-color: #c4503a; }
.status-badge {
    border-radius: 100px;
    padding: 0.25rem 0.8rem;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    white-space: nowrap;
}
.status-badge.stable { background: #e8f4ef; color: #2d7a5f; }
.status-badge.concern { background: #fef8e8; color: #b87d0d; }
.status-badge.hard { background: #fef0ee; color: #c4503a; }
.patient-avatar {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    flex-shrink: 0;
}
.patient-name {
    font-weight: 600;
    font-size: 1rem;
    color: #1a2a3a;
}
.patient-meta {
    font-size: 0.8rem;
    color: #8a9ab0;
    margin-top: 0.1rem;
}
.analytics-card {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    text-align: center;
}
.analytics-number {
    font-family: 'Fraunces', serif;
    font-size: 2.8rem;
    font-weight: 300;
    color: #3d5a80;
    line-height: 1;
}
.analytics-label {
    font-size: 0.78rem;
    color: #8a9ab0;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 0.4rem;
}
.trend-up { color: #2d7a5f; font-size: 0.85rem; }
.trend-down { color: #c4503a; font-size: 0.85rem; }

/* ── BUTTONS OVERRIDE ── */
.stButton > button {
    border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
}

/* Sidebar-style nav tabs */
div[data-testid="stTabs"] [data-baseweb="tab"] {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
}

/* inputs */
.stTextInput input, .stSelectbox select, .stTextArea textarea {
    border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
    border-color: #e5ddd3 !important;
}
.stSelectbox [data-baseweb="select"] {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SESSION STATE INIT
# ─────────────────────────────────────────────
def init_state():
    defaults = {
        "mode": None,
        "elder_name": "Margaret",
        "q_index": 0,
        "answers": [],
        "show_feedback": False,
        "last_correct": None,
        "notes": [
            {"from": "Susan (daughter)", "text": "We miss you Mum! See you Sunday 🌸", "time": "Today, 9:12 AM"},
            {"from": "Dr. Rivera", "text": "Great job this week, keep up the exercises!", "time": "Yesterday"},
        ],
        "sessions": [
            {"date": "Today", "score": 7, "total": 10, "duration": "12 min", "mood": "😊"},
            {"date": "Yesterday", "score": 5, "total": 10, "duration": "9 min", "mood": "😐"},
            {"date": "Mon", "score": 8, "total": 10, "duration": "14 min", "mood": "😊"},
            {"date": "Sun", "score": 4, "total": 10, "duration": "7 min", "mood": "😔"},
            {"date": "Sat", "score": 9, "total": 10, "duration": "15 min", "mood": "😊"},
        ],
        "patients": [
            {"name": "Margaret T.", "age": 78, "avatar": "👵", "status": "stable",
             "score_week": 74, "trend": "+5%", "last": "Today", "sessions_week": 5},
            {"name": "Robert H.", "age": 83, "avatar": "👴", "status": "concern",
             "score_week": 51, "trend": "-8%", "last": "2 days ago", "sessions_week": 3},
            {"name": "Elena V.", "age": 71, "avatar": "👩‍🦳", "status": "stable",
             "score_week": 82, "trend": "+2%", "last": "Today", "sessions_week": 6},
            {"name": "James O.", "age": 87, "avatar": "🧓", "status": "hard",
             "score_week": 38, "trend": "-15%", "last": "4 days ago", "sessions_week": 1},
            {"name": "Dorothy M.", "age": 74, "avatar": "👵", "status": "stable",
             "score_week": 69, "trend": "+1%", "last": "Yesterday", "sessions_week": 4},
        ],
        "difficulty": "Medium",
        "daily_sessions": 2,
        "session_length": 10,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ─────────────────────────────────────────────
#  MOCK DATA — Memory Questions
# ─────────────────────────────────────────────
questions = [
    {
        "photo_emoji": "👩‍👧",
        "photo_bg": "linear-gradient(135deg,#fde8d0,#f5cfa8,#e8b88a)",
        "question": "Who is next to you in this picture?",
        "correct": "Susan (your daughter)",
        "options": ["Susan (your daughter)", "Your neighbour Carol", "Your sister Anne", "A friend from church"],
    },
    {
        "photo_emoji": "👴🐕",
        "photo_bg": "linear-gradient(135deg,#d8ecd4,#b8dab2,#90c490)",
        "question": "Who are you walking with here?",
        "correct": "Your husband George",
        "options": ["Your husband George", "Your son Michael", "A friend from the centre", "Your brother Paul"],
    },
    {
        "photo_emoji": "🎂👨‍👩‍👧‍👦",
        "photo_bg": "linear-gradient(135deg,#ddd8f0,#c0b8e0,#a098d0)",
        "question": "Whose birthday is being celebrated?",
        "correct": "Your grandson Liam",
        "options": ["Your grandson Liam", "Your daughter Susan", "Your neighbour Carol", "Yourself"],
    },
    {
        "photo_emoji": "🏡☀️",
        "photo_bg": "linear-gradient(135deg,#fff0c8,#ffe0a0,#ffc878)",
        "question": "Where was this photo taken?",
        "correct": "Your garden at home",
        "options": ["Your garden at home", "The community centre", "Susan's house", "The park near the church"],
    },
    {
        "photo_emoji": "👩‍⚕️💊",
        "photo_bg": "linear-gradient(135deg,#d0eef8,#b0d8f0,#88c0e8)",
        "question": "Who is this person helping you?",
        "correct": "Your nurse, Ana",
        "options": ["Your nurse, Ana", "Your daughter Susan", "A volunteer", "Dr. Rivera"],
    },
]

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def topbar(mode_label, mode_class, back=True):
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if back and st.button("← Back", key="back_btn"):
            st.session_state.mode = None
            st.session_state.q_index = 0
            st.session_state.answers = []
            st.session_state.show_feedback = False
            st.rerun()
    with col2:
        st.markdown(f"""
        <div class="topbar">
            <span class="topbar-logo">Memo<span>ria</span></span>
            <span class="topbar-mode {mode_class}">{mode_label}</span>
        </div>
        """, unsafe_allow_html=True)

def score_color(score):
    if score >= 70: return "#2d7a5f"
    if score >= 50: return "#b87d0d"
    return "#c4503a"

# ─────────────────────────────────────────────
#  LANDING PAGE
# ─────────────────────────────────────────────
def show_landing():
    st.markdown("""
    <div class="landing-hero">
        <div class="landing-logo">Memo<span>ria</span></div>
        <div class="landing-tagline">Gentle memory care, every day</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div class="mode-card elder">
            <div class="mode-icon">🌸</div>
            <div class="mode-title">My Space</div>
            <div class="mode-desc">For residents — gentle photo exercises and daily memory activities at your own pace.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Enter My Space", key="elder_btn", use_container_width=True,
                     type="primary"):
            st.session_state.mode = "elder"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="mode-card family">
            <div class="mode-icon">🏡</div>
            <div class="mode-title">Family View</div>
            <div class="mode-desc">For families — check on your loved one, send notes, and adjust their settings.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Family Dashboard", key="family_btn", use_container_width=True):
            st.session_state.mode = "family"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="mode-card medical">
            <div class="mode-icon">🏥</div>
            <div class="mode-title">Care Team</div>
            <div class="mode-desc">For clinicians — patient overview, analytics, trends, and care configuration.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Care Portal", key="medical_btn", use_container_width=True):
            st.session_state.mode = "medical"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; color:#b0a090; font-size:0.8rem; font-style:italic;'>
        Memoria — Compassionate cognitive support · MVP Demo
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  ELDER MODE
# ─────────────────────────────────────────────
def show_elder():
    topbar("My Space 🌸", "elder")

    name = st.session_state.elder_name
    hour = datetime.datetime.now().hour
    greeting = "Good morning" if hour < 12 else ("Good afternoon" if hour < 17 else "Good evening")

    st.markdown(f"""
    <div class="elder-greeting">{greeting}, {name} 🌸</div>
    <div class="elder-subtext">Let's do a little memory exercise together.</div>
    """, unsafe_allow_html=True)

    # Streak bar
    answers = st.session_state.answers
    streak_html = '<div class="streak-bar"><span style="font-size:0.85rem;color:#8a7060;margin-right:0.4rem;">Today:</span>'
    for i in range(len(questions)):
        if i < len(answers):
            cls = "correct" if answers[i] else "wrong"
        else:
            cls = "empty"
        streak_html += f'<span class="streak-dot {cls}"></span>'
    streak_html += f'<span style="margin-left:auto;font-size:0.85rem;color:#8a7060;">{len([a for a in answers if a])}/{len(questions)} correct</span></div>'
    st.markdown(streak_html, unsafe_allow_html=True)

    q_idx = st.session_state.q_index

    # All done
    if q_idx >= len(questions):
        correct = sum(1 for a in st.session_state.answers if a)
        total = len(questions)
        pct = int(correct / total * 100)
        if pct >= 70:
            emoji, msg, bg = "🎉", "Wonderful job today!", "linear-gradient(135deg,#e8f5ee,#d0eedd)"
        elif pct >= 40:
            emoji, msg, bg = "💛", "Good effort, keep going!", "linear-gradient(135deg,#fef8e8,#fde8c0)"
        else:
            emoji, msg, bg = "🌱", "We'll practise together tomorrow.", "linear-gradient(135deg,#fef5ee,#fde8d8)"
        st.markdown(f"""
        <div style="background:{bg};border-radius:24px;padding:3rem;text-align:center;margin-top:1rem;">
            <div style="font-size:4rem;">{emoji}</div>
            <div style="font-family:'Fraunces',serif;font-size:2.2rem;color:#2d2318;margin:0.8rem 0;">{msg}</div>
            <div style="font-size:1.3rem;color:#5a4030;margin-bottom:1.5rem;">
                You got <strong>{correct} out of {total}</strong> — {pct}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄  Play Again", use_container_width=True, type="primary"):
                st.session_state.q_index = 0
                st.session_state.answers = []
                st.session_state.show_feedback = False
                st.rerun()
        return

    q = questions[q_idx]

    # Show feedback overlay first
    if st.session_state.show_feedback:
        correct_ans = st.session_state.last_correct
        if correct_ans:
            st.markdown("""
            <div class="feedback-success">
                <div class="feedback-emoji">✅</div>
                <div class="feedback-text">That's right! Well done!</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="feedback-fail">
                <div class="feedback-emoji">💛</div>
                <div class="feedback-text">That was <em>{q['correct']}</em>. No worries!</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Next Question →", use_container_width=True, type="primary", key="next_q"):
                st.session_state.q_index += 1
                st.session_state.show_feedback = False
                st.rerun()
        return

    # Question card
    col_main, col_side = st.columns([2, 1], gap="large")

    with col_main:
        st.markdown(f"""
        <div class="photo-frame">
            <div class="photo-placeholder" style="background:{q['photo_bg']};">
                <span style="font-size:5rem;">{q['photo_emoji']}</span>
            </div>
            <div class="photo-question">{q['question']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_side:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="font-family:'Fraunces',serif;font-size:1.1rem;color:#8a7060;margin-bottom:1rem;">
            Question {q_idx + 1} of {len(questions)}
        </div>
        """, unsafe_allow_html=True)

        options = q["options"].copy()
        random.seed(q_idx * 42)
        random.shuffle(options)

        for opt in options:
            is_correct = opt == q["correct"]
            if st.button(f"  {opt}", key=f"opt_{q_idx}_{opt}", use_container_width=True):
                st.session_state.answers.append(is_correct)
                st.session_state.last_correct = is_correct
                st.session_state.show_feedback = True
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        # Notes from family
        if st.session_state.notes:
            st.markdown(f"""
            <div style="background:#fffbf5;border:1px solid #f0e4d0;border-radius:14px;padding:1rem;">
                <div style="font-size:0.8rem;font-weight:600;color:#c4753a;letter-spacing:0.05em;
                            text-transform:uppercase;margin-bottom:0.6rem;">📬 Message for you</div>
                <div style="font-size:0.9rem;color:#4a3728;">
                    {st.session_state.notes[0]['text']}
                </div>
                <div style="font-size:0.75rem;color:#b0a090;margin-top:0.4rem;">
                    — {st.session_state.notes[0]['from']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FAMILY MODE
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
#  MEDICAL / CARE TEAM MODE
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
#  ROUTER
# ─────────────────────────────────────────────
mode = st.session_state.mode

if mode is None:
    show_landing()
elif mode == "elder":
    show_elder()
elif mode == "family":
    show_family()
elif mode == "medical":
    show_medical()

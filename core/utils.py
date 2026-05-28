# core/utils.py
import streamlit as st
import datetime

def apply_styles():
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
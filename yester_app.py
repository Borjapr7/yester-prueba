# app.py
import streamlit as st

# 1. Page Config (Debe ser la primera orden de Streamlit)
st.set_page_config(
    page_title="Yester",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Importaciones de tus módulos
from core.utils import apply_styles, init_state
from views.elder import show_elder
from views.family import show_family
from views.medical import show_medical

# 3. Inicializar entorno y aplicar tu estilo global
apply_styles()
init_state()

# 4. Landing Page
def show_landing():
    st.markdown("""
    <div class="landing-hero">
        <div class="landing-logo">Yester<span></span></div>
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
        Yester — Compassionate cognitive support · MVP Demo
    </div>
    """, unsafe_allow_html=True)

# 5. Router / Enrutador
mode = st.session_state.mode

if mode is None:
    show_landing()
elif mode == "elder":
    show_elder()
elif mode == "family":
    show_family()
elif mode == "medical":
    show_medical()
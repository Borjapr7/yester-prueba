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
        <div class="landing-tagline">Cuidamos tus recuerdos cada día</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div class="mode-card elder">
            <div class="mode-icon">🌸</div>
            <div class="mode-title">Portal del Paciente</div>
            <div class="mode-desc">Ejercicios suaves con fotos y actividades diarias para mantener la mente activa y feliz.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Comenzar", key="elder_btn", use_container_width=True,
                     type="primary"):
            st.session_state.mode = "elder"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="mode-card family">
            <div class="mode-icon">🏡</div>
            <div class="mode-title">Para la Familia</div>
            <div class="mode-desc">Recibe actualizaciones, comparte mensajes y acompaña el bienestar de tu ser querido.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Acceder a unidad familiar", key="family_btn", use_container_width=True):
            st.session_state.mode = "family"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="mode-card medical">
            <div class="mode-icon">🏥</div>
            <div class="mode-title">Para el Equipo Clínico</div>
            <div class="mode-desc">Seguimiento del bienestar, análisis de progreso y configuración de cuidados centrados en la persona.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Acceder a portal clínico", key="medical_btn", use_container_width=True):
            st.session_state.mode = "medical"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; color:#b0a090; font-size:0.8rem; font-style:italic;'>
        Yester — Apoyo cognitivo respetuoso· MVP Demo
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
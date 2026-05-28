import streamlit as st
import random
import datetime
from core.utils import topbar, questions, score_color

def show_elder():
    topbar("Mi espacio 🌸", "elder")

    name = st.session_state.elder_name
    hour = datetime.datetime.now().hour
    greeting = "Buenos días" if hour < 12 else ("Buenas tardes" if hour < 17 else "Buenas noches")

    st.markdown(f"""
    <div class="elder-greeting">{greeting}, {name} 🌸</div>
    <div class="elder-subtext">Vamos a hacer un ejercicio de memoria juntos.</div>
    """, unsafe_allow_html=True)

    # Usar las preguntas personalizadas si las hay, si no, usar las por defecto
    lista_preguntas = st.session_state.custom_questions if "custom_questions" in st.session_state and len(st.session_state.custom_questions) > 0 else questions

    # Streak bar
    answers = st.session_state.answers
    streak_html = '<div class="streak-bar"><span style="font-size:0.85rem;color:#8a7060;margin-right:0.4rem;">Hoy:</span>'
    for i in range(len(lista_preguntas)):
        if i < len(answers):
            cls = "correct" if answers[i] else "wrong"
        else:
            cls = "empty"
        streak_html += f'<span class="streak-dot {cls}"></span>'
    streak_html += f'<span style="margin-left:auto;font-size:0.85rem;color:#8a7060;">{len([a for a in answers if a])}/{len(lista_preguntas)} correct</span></div>'
    st.markdown(streak_html, unsafe_allow_html=True)

    q_idx = st.session_state.q_index

    # All done
    if q_idx >= len(lista_preguntas):
        correct = sum(1 for a in st.session_state.answers if a)
        total = len(lista_preguntas)
        pct = int(correct / total * 100) if total > 0 else 0
        if pct >= 70:
            emoji, msg, bg = "🎉", "¡Lo has hecho genial hoy!", "linear-gradient(135deg,#e8f5ee,#d0eedd)"
        elif pct >= 40:
            emoji, msg, bg = "💛", "¡Buen esfuerzo, sigue así!", "linear-gradient(135deg,#fef8e8,#fde8c0)"
        else:
            emoji, msg, bg = "🌱", "Practicaremos juntos mañana.", "linear-gradient(135deg,#fef5ee,#fde8d8)"
        st.markdown(f"""
        <div style="background:{bg};border-radius:24px;padding:3rem;text-align:center;margin-top:1rem;">
            <div style="font-size:4rem;">{emoji}</div>
            <div style="font-family:'Fraunces',serif;font-size:2.2rem;color:#2d2318;margin:0.8rem 0;">{msg}</div>
            <div style="font-size:1.3rem;color:#5a4030;margin-bottom:1.5rem;">
                Has acertado <strong>{correct} de {total}</strong> — {pct}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄  Volver a empezar", use_container_width=True, type="primary"):
                st.session_state.q_index = 0
                st.session_state.answers = []
                st.session_state.show_feedback = False
                st.rerun()
        return

    q = lista_preguntas[q_idx]

    # Show feedback overlay first
    if st.session_state.show_feedback:
        correct_ans = st.session_state.last_correct
        if correct_ans:
            st.markdown("""
            <div class="feedback-success">
                <div class="feedback-emoji">✅</div>
                <div class="feedback-text">¡Eso es! ¡Muy bien hecho!</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="feedback-fail">
                <div class="feedback-emoji">💛</div>
                <div class="feedback-text">Era <em>{q['correct']}</em>. ¡No pasa nada!</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Siguiente pregunta →", use_container_width=True, type="primary", key="next_q"):
                st.session_state.q_index += 1
                st.session_state.show_feedback = False
                st.rerun()
        return

    # Question card
    col_main, col_side = st.columns([2, 1], gap="large")

    with col_main:
        st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
        
        # Comprobar si es una pregunta con imagen real (subida) o un mock por defecto
        if "image_file" in q:
            # Mostramos la imagen subida
            st.image(q["image_file"], use_container_width=True)
        else:
            # Mostramos el degradado por defecto
            st.markdown(f"""
            <div class="photo-placeholder" style="background:{q['photo_bg']};">
                <span style="font-size:5rem;">{q['photo_emoji']}</span>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown(f'<div class="photo-question" style="margin-top:1.5rem;">{q["question"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_side:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="font-family:'Fraunces',serif;font-size:1.1rem;color:#8a7060;margin-bottom:1rem;">
            Pregunta {q_idx + 1} de {len(lista_preguntas)}
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
                            text-transform:uppercase;margin-bottom:0.6rem;">📬 Un mensaje para ti</div>
                <div style="font-size:0.9rem;color:#4a3728;">
                    {st.session_state.notes[0]['text']}
                </div>
                <div style="font-size:0.75rem;color:#b0a090;margin-top:0.4rem;">
                    — {st.session_state.notes[0]['from']}
                </div>
            </div>
            """, unsafe_allow_html=True)
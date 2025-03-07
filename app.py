import streamlit as st
import random

# Streamlit page config
st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")

# CSS for styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            color: white;
            text-align: center;
        }
        .title {
            font-size: 30px;
            font-weight: bold;
            color: white;
            text-align: center;
        }
        .guess {
            font-size: 20px;
            color: white;
        }
        .winner {
            font-size: 24px;
            font-weight: bold;
            color: #00ff00;
        }
        .lost {
            font-size: 24px;
            font-weight: bold;
            color: #ff0000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Game state (stored in session_state)
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Title
st.markdown("<div class='title'>🎯 Number Guessing Game 🎯</div>", unsafe_allow_html=True)
st.write("Guess a number between **1 and 100**.")

# User input for guessing
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to submit guess
if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.target:
            st.markdown("<div class='guess'>🔺 Try a higher number!</div>", unsafe_allow_html=True)
        elif guess > st.session_state.target:
            st.markdown("<div class='guess'>🔻 Try a lower number!</div>", unsafe_allow_html=True)
        else:
            st.session_state.game_over = True
            st.markdown(f"<div class='winner'>🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts! 🎉</div>", unsafe_allow_html=True)

# Reset game button
if st.button("Restart Game"):
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()  # ✅ Updated Fix (instead of st.experimental_rerun())

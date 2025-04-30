import streamlit as st
import random

# Session state to store values between interactions
if 'num_to_guess' not in st.session_state:
    st.session_state.num_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.title("🎯 Number Guessing Game")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it?")

if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.num_to_guess:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.num_to_guess:
            st.warning("Too high! Try again.")
        else:
            st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True
else:
    if st.button("Play Again"):
        st.session_state.num_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

        
    
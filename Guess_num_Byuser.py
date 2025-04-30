import streamlit as st

st.title("Guess the Number Game")

num_to_guess = st.number_input("Enter the number I'm thinking of (between 1 and 100):", min_value=1, max_value=100, key="target")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, key="guess")

if 'result' not in st.session_state:
    st.session_state.result = ""

if st.button("Submit Guess"):
    if guess < num_to_guess:
        st.session_state.result = "Too low! Try again."
    elif guess > num_to_guess:
        st.session_state.result = "Too high! Try again."
    else:
        st.session_state.result = "🎉 Congratulations! You guessed it right!"

st.write(st.session_state.result)

    
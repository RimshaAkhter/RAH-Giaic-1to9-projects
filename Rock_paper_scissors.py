import random
import streamlit as st

# Streamlit UI
st.title("Rock Paper Scissors Game")

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

# Dropdown for user to select Rock, Paper, or Scissors
user_choice = st.selectbox("Choose Rock, Paper, or Scissors", options)

if st.button("Play!"):
    if user_choice == computer_choice:
        st.write(f"Oh! It's a tie. Both chose {computer_choice}.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        st.write(f"Yeah! Congratulations! You win! Computer chose {computer_choice}.")
    else:
        st.write(f"Oh no! You lose! Computer chose {computer_choice}.")


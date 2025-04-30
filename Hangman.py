import streamlit as st
import random

# Function to start the Hangman game
def hangman():
    words = ["python", "programming", "hangman", "challenge", "development"]
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    st.title("🎮 Hangman Game")
    st.write("Guess the word by guessing individual letters.")
    st.write(f"Word to guess: {'_ ' * len(chosen_word)}")

    if 'guessed_letters' not in st.session_state:
        st.session_state.guessed_letters = []
        st.session_state.attempts = attempts
        st.session_state.game_over = False
        st.session_state.current_progress = '_ ' * len(chosen_word)

    # Display current progress
    st.write(f"Current progress: {st.session_state.current_progress}")

    if not st.session_state.game_over:
        # User input for guess
        guess = st.text_input("Guess a letter:", max_chars=1).lower()

        if guess and guess not in st.session_state.guessed_letters:
            if guess in chosen_word:
                st.session_state.guessed_letters.append(guess)
                st.success("Good guess!")
            else:
                st.session_state.guessed_letters.append(guess)
                st.session_state.attempts -= 1
                st.warning(f"Wrong guess! You have {st.session_state.attempts} attempts left.")

            # Update current progress
            st.session_state.current_progress = ''.join([letter if letter in st.session_state.guessed_letters else '_ ' for letter in chosen_word])

            # Check for win or loss
            if "_" not in st.session_state.current_progress:
                st.success("Congratulations! You've guessed the word!")
                st.session_state.game_over = True
            elif st.session_state.attempts == 0:
                st.error(f"You've run out of attempts! The word was '{chosen_word}'.")
                st.session_state.game_over = True
    else:
        # Play again option
        if st.button("Play Again"):
            st.session_state.guessed_letters = []
            st.session_state.attempts = attempts
            st.session_state.game_over = False
            st.session_state.current_progress = '_ ' * len(chosen_word)

# Run the game
hangman()

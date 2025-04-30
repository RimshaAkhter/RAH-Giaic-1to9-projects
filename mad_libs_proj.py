
import streamlit as st

# Function to create the Mad Libs story
def mad_libs():
    st.title("Mad Libs Game")
    st.write("Fill in the blanks to create your own story!")

    # Inputs for the story
    noun1 = st.text_input("Enter a noun:")
    adj1 = st.text_input("Enter an adjective:")
    verb1 = st.text_input("Enter a verb:")

    noun2 = st.text_input("Enter another noun:")
    adj2 = st.text_input("Enter another adjective:")

    if noun1 and adj1 and verb1 and noun2 and adj2:
        story = (
            f"Once upon a time, there was a {adj1} {noun1} that loved to {verb1}. "
            f"One day, it met a {adj2} {noun2} and they became best friends."
        )
        st.subheader("Your Mad Libs Story:")
        st.write(story)
    else:
        st.write("Please fill in all the fields to create your story!")

# Run the Mad Libs game
mad_libs()

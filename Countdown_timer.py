import streamlit as st
import time

st.title("Countdown Timer")

seconds = st.number_input("Enter time in seconds:", min_value=1, max_value=3600, step=1)

if st.button("Start Timer"):
    with st.empty():
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.write(f"⏳ Time Left: {timer}")
            time.sleep(1)
        st.write("✅ Time's up!")

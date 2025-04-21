import streamlit as st
import random

# Motivational Quotes
quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "The only person you are destined to become is the person you decide to be.",
    "Mistakes are proof that you are trying.",
    "Every expert was once a beginner.",
    "Difficult roads often lead to beautiful destinations.",
    "Success is the ability to go from one failure to another with no loss of enthusiasm.",
    "The only limit to our realization of tomorrow is our doubts of today."
]

# Daily Challenges
challenges = [
     "Write down one thing you struggled with today and how you can improve.",
    "Teach someone something you recently learned.",
    "Write a blog post on a topic of your choice.",
    "Complete a coding project on a topic of your choice.",
     "Try something new that scares you a little.",
    "Ask for feedback on your work.",
    "Read a book on a topic of your choice.",
    "Write a song about a topic of your choice.",
    "Reflect on a recent mistake and what it taught you."
    "Draw a picture of a topic of your choice."
]

# Streamlit app

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered", initial_sidebar_state="expanded")

st.title("🌱 Growth Mindset Challenge")
st.write("Welcome! This app is designed to help you build a **growth mindset** through daily reflection and positive challenges.")

st.header("💡 What is a Growth Mindset?")
st.markdown("""
A growth mindset is a mindset that emphasizes the importance of continuous learning, growth, and personal development.
It is characterized by a positive attitude towards learning, a willingness to take risks, and a focus on personal growth and development.
""")

st.header("🎯 Daily Challenge")
if st.button("Generate Today's Challenge"):
    st.success(random.choice(challenges))

st.header("🧠 Quick Reflection Quiz")
with st.form("reflection_quiz"):
    q1 = st.radio("When I fail at something, I tend to:", ["Give up", "Try again and learn from it"])
    q2 = st.radio("I believe intelligence is:", ["Fixed", "Something that can grow"])
    q3 = st.radio("If I lose hope, I tend to:", ["Motivate yourself", "Give up"])
    q4 = st.radio("When things get hard, I:", ["Feel stuck", "See it as a challenge"])
    q5 = st.radio("When I face some errors in my work, I tend to:",["Leave it and move on", "Try to fix it and learn from it"])


    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("You selected:")
        st.write(f"Question 1: {q1}")
        st.write(f"Question 2: {q2}")
        st.write(f"Question 3: {q3}")
        st.write(f"Question 4: {q4}")
        st.write(f"Question 5: {q5}")

        score = sum([q == "Try again and learn from it" for q in [q1]]) \
                + sum([q == "Something that can grow" for q in [q2]]) \
                + sum([q == "Motivate yourself" for q in [q3]]) \
                + sum([q == "See it as a challenge" for q in [q4]]) \
                + sum([q == "Try to fix it and learn from it" for q in [q5]])


        if score >= 2:
            st.success("👏 You’re on the path to a growth mindset!")
        else:
            st.info("Keep going! Growth mindset takes time and practice.")

st.header("📢 Motivation for You")
if st.button("Inspire Me"):
    st.info(random.choice(quotes))

st.write("---")
st.caption("Made with 💙 for the Growth Mindset Challenge.")

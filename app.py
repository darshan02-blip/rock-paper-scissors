import streamlit as st
import random
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Title
st.title("🧠 AI Rock Paper Scissors")
st.write("Play against a simple AI that learns your moves!")

# Choices
choices = ['Rock', 'Paper', 'Scissors']

# Session State
if 'user_moves' not in st.session_state:
    st.session_state.user_moves = []
if 'ai_moves' not in st.session_state:
    st.session_state.ai_moves = []
if 'model' not in st.session_state:
    st.session_state.model = MultinomialNB()

# Encode choices
def encode_move(move):
    return {'Rock': [1, 0, 0], 'Paper': [0, 1, 0], 'Scissors': [0, 0, 1]}[move]

def get_winner(user, ai):
    if user == ai:
        return "It's a tie!"
    elif (user == 'Rock' and ai == 'Scissors') or \
         (user == 'Paper' and ai == 'Rock') or \
         (user == 'Scissors' and ai == 'Paper'):
        return "You win! 🎉"
    else:
        return "AI wins! 🤖"

# User input
user_choice = st.radio("Your move:", choices)

if st.button("Play"):
    st.session_state.user_moves.append(user_choice)

    # Train AI if enough data
    if len(st.session_state.user_moves) > 5:
        # Create training data
        X = np.array([encode_move(m) for m in st.session_state.user_moves[:-1]])
        y = [choices.index(m) for m in st.session_state.user_moves[1:]]
        st.session_state.model.fit(X, y)

        # Predict next move
        last_move = np.array([encode_move(st.session_state.user_moves[-1])])
        prediction = st.session_state.model.predict(last_move)[0]
        predicted_user_move = choices[prediction]

        # AI chooses the move that beats predicted move
        counter_moves = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
        ai_choice = counter_moves[predicted_user_move]
    else:
        ai_choice = random.choice(choices)

    st.session_state.ai_moves.append(ai_choice)

    st.markdown(f"**Your move:** {user_choice}")
    st.markdown(f"**AI move:** {ai_choice}")
    st.markdown(f"**Result:** {get_winner(user_choice, ai_choice)}")

    st.divider()
    st.markdown("### History")
    for i in range(len(st.session_state.user_moves)):
        st.write(f"Round {i+1}: You - {st.session_state.user_moves[i]}, AI - {st.session_state.ai_moves[i]}")

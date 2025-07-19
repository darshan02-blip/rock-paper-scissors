# phase4_rps_ai.py

import streamlit as st
import random
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load
import os

# Initialize session state
if "user_moves" not in st.session_state:
    st.session_state.user_moves = []
    st.session_state.ai_moves = []
    st.session_state.results = []
    st.session_state.model = None

# Game logic
def determine_winner(user, ai):
    if user == ai:
        return "Draw"
    elif (user == "rock" and ai == "scissors") or \
         (user == "scissors" and ai == "paper") or \
         (user == "paper" and ai == "rock"):
        return "You Win!"
    else:
        return "AI Wins!"

# Train model if we have enough data
def train_model(user_moves, ai_moves):
    if len(user_moves) < 10:
        return None
    df = pd.DataFrame({
        'prev_move': user_moves[:-1],
        'next_move': user_moves[1:]
    })
    le = LabelEncoder()
    df['prev_move_encoded'] = le.fit_transform(df['prev_move'])
    df['next_move_encoded'] = le.fit_transform(df['next_move'])
    
    model = DecisionTreeClassifier()
    model.fit(df[['prev_move_encoded']], df['next_move_encoded'])
    dump((model, le), 'rps_model.joblib')
    return model, le

# Predict user move
def predict_next_move(model, le, last_move):
    if model is None or last_move is None:
        return random.choice(['rock', 'paper', 'scissors'])
    last_move_encoded = le.transform([last_move])[0]
    predicted = model.predict([[last_move_encoded]])[0]
    predicted_label = le.inverse_transform([predicted])[0]
    
    # AI plays what beats the predicted move
    counter = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    return counter[predicted_label]

# UI
st.title("🤖 Phase 4: Rock-Paper-Scissors with AI Prediction")

user_move = st.selectbox("Choose your move:", ['rock', 'paper', 'scissors'])
if st.button("Play"):

    last_move = st.session_state.user_moves[-1] if st.session_state.user_moves else None

    # Load or train model
    model, le = None, None
    if os.path.exists('rps_model.joblib'):
        model, le = load('rps_model.joblib')
    elif len(st.session_state.user_moves) > 10:
        model, le = train_model(st.session_state.user_moves, st.session_state.ai_moves)

    # AI move
    ai_move = predict_next_move(model, le, last_move)

    # Save moves
    st.session_state.user_moves.append(user_move)
    st.session_state.ai_moves.append(ai_move)

    # Decide winner
    result = determine_winner(user_move, ai_move)
    st.session_state.results.append(result)

    st.write(f"🤖 AI chose: `{ai_move}`")
    st.write(f"🎯 Result: **{result}**")

    st.line_chart(pd.DataFrame({
        'You': pd.Series(st.session_state.user_moves),
        'AI': pd.Series(st.session_state.ai_moves),
    }))

    st.write("📊 History:")
    st.dataframe(pd.DataFrame({
        'You': st.session_state.user_moves,
        'AI': st.session_state.ai_moves,
        'Result': st.session_state.results
    }))

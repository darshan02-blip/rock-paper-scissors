import streamlit as st
import random

st.title("🧠 Rock Paper Scissors - Phase 3: Pattern Prediction AI")

moves = ['Rock', 'Paper', 'Scissors']
transition_table = {
    'Rock': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
    'Paper': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
    'Scissors': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
}

if 'prev_move' not in st.session_state:
    st.session_state.prev_move = None

if 'transition_table' not in st.session_state:
    st.session_state.transition_table = transition_table

if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.result = ""

def predict_next_move():
    prev = st.session_state.prev_move
    if prev is None:
        return random.choice(moves)
    
    next_moves = st.session_state.transition_table[prev]
    predicted_player_move = max(next_moves, key=next_moves.get)
    
    # AI counters predicted move
    counter_move = {
        'Rock': 'Paper',
        'Paper': 'Scissors',
        'Scissors': 'Rock'
    }
    return counter_move[predicted_player_move]

def play(player_move):
    # AI predicts and plays
    ai_move = predict_next_move()
    
    # Update transition table
    prev = st.session_state.prev_move
    if prev is not None:
        st.session_state.transition_table[prev][player_move] += 1

    # Update previous move
    st.session_state.prev_move = player_move

    # Determine winner
    if player_move == ai_move:
        st.session_state.result = "It's a Tie!"
    elif (player_move == 'Rock' and ai_move == 'Scissors') or \
         (player_move == 'Paper' and ai_move == 'Rock') or \
         (player_move == 'Scissors' and ai_move == 'Paper'):
        st.session_state.player_score += 1
        st.session_state.result = "You Win!"
    else:
        st.session_state.ai_score += 1
        st.session_state.result = "AI Wins!"

    st.write(f"🧍 You chose: {player_move}")
    st.write(f"🤖 AI chose: {ai_move}")
    st.write(f"📣 Result: {st.session_state.result}")
    st.write(f"🏆 Score: You {st.session_state.player_score} - AI {st.session_state.ai_score}")

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Rock'):
        play('Rock')
with col2:
    if st.button('Paper'):
        play('Paper')
with col3:
    if st.button('Scissors'):
        play('Scissors')

if st.button("🔁 Reset Game"):
    st.session_state.prev_move = None
    st.session_state.transition_table = {
        'Rock': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
        'Paper': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
        'Scissors': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
    }
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.result = ""
    st.success("Game Reset!")


import streamlit as st
import random


st.title("FACE OFF!")
st.header("Your Classic Game of Rock Paper Scissor!")

if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'tie_score' not in st.session_state:
    st.session_state.tie_score = 0

#logic
def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
        st.session_state.tie_score += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        st.session_state.user_score += 1
    else:
        result = "Computer wins!"
        st.session_state.computer_score += 1

    return user_choice, computer_choice, result

st.title("Let's Play")
st.write("Choose your move and see if you can beat the computer!")

user_choice = st.selectbox("Choose your move:", ["rock", "paper", "scissors"])

if st.button("Play"):
    user_choice, computer_choice, result = play_game(user_choice)
    
    st.write(f"**Your choice:** {user_choice}")
    st.write(f"**Computer's choice:** {computer_choice}")
    st.write(f"**Result:** {result}")
    
    # Display the scores
    st.write(f"**Your score:** {st.session_state.user_score}")
    st.write(f"**Computer's score:** {st.session_state.computer_score}")
    st.write(f"**Ties:** {st.session_state.tie_score}")
    
# Option to reset the scores
if st.button("Reset Scores"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.tie_score = 0
    st.write("Scores have been reset!")


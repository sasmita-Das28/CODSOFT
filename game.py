import tkinter as tk
import random

# Start with both scores as 0
user_score = 0
computer_score = 0

# This function runs whenever a user clicks rock, paper, or scissors
def determine_winner(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Tell user and computer's choices
    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"

    # Decide the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win this round!"
        user_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    # Update the result and score on the screen
    result_text += result
    result_label.config(text=result_text)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

# Set up the game window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="pink")

# Game title
title = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"), bg="pink", fg="black")
title.pack(pady=10)

# Label to show what happened
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", justify="center")
result_label.pack(pady=20)

# Score display
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Helvetica", 12, "bold"), bg="white")
score_label.pack(pady=10)

# Buttons to choose rock/paper/scissors
btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, height=2, command=lambda: determine_winner("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text=" Paper", width=10, height=2, command=lambda: determine_winner("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text=" Scissors", width=10, height=2, command=lambda: determine_winner("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Exit button
exit_btn = tk.Button(root, text="Quit Game", bg="grey", fg="pink", width=15, command=root.quit)
exit_btn.pack(pady=20)

# Start the app
root.mainloop()

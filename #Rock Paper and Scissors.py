#Rock Paper and Scissors
import tkinter as tk
import random

# Set up main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("420x400")
window.configure(bg="#e6f7ff")

# Game variables
player_points = 0
cpu_points = 0

# Core functions
def cpu_pick():
    return random.choice(["rock", "paper", "scissors"])

def check_result(player, cpu):
    if player == cpu:
        return "draw"
    elif (player == "rock" and cpu == "scissors") or \
         (player == "scissors" and cpu == "paper") or \
         (player == "paper" and cpu == "rock"):
        return "player"
    else:
        return "cpu"

def start_game(choice):
    global player_points, cpu_points

    bot_choice = cpu_pick()
    outcome = check_result(choice, bot_choice)

    message = f"🎮 You chose: {choice}\n🤖 Computer chose: {bot_choice}\n"

    if outcome == "draw":
        message += "⚖️ It's a draw!"
        result_display.config(fg="blue")
    elif outcome == "player":
        player_points += 1
        message += "✅ You won this round!"
        result_display.config(fg="green")
    else:
        cpu_points += 1
        message += "❌ Computer wins this round."
        result_display.config(fg="red")

    result_display.config(text=message)
    update_score()

def update_score():
    score_display.config(text=f"Score → You: {player_points} | Computer: {cpu_points}")

def restart():
    global player_points, cpu_points
    player_points = 0
    cpu_points = 0
    result_display.config(text="Ready to play?", fg="black")
    update_score()

# UI Elements
header = tk.Label(window, text="Rock 🪨 Paper 📄 Scissors ✂️", font=("Arial", 16, "bold"), bg="#e6f7ff")
header.pack(pady=15)

result_display = tk.Label(window, text="Ready to play?", font=("Arial", 12), bg="#e6f7ff")
result_display.pack(pady=20)

btn_frame = tk.Frame(window, bg="#e6f7ff")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="🪨 Rock", width=12, command=lambda: start_game("rock"))
paper_btn = tk.Button(btn_frame, text="📄 Paper", width=12, command=lambda: start_game("paper"))
scissors_btn = tk.Button(btn_frame, text="✂️ Scissors", width=12, command=lambda: start_game("scissors"))

rock_btn.grid(row=0, column=0, padx=8, pady=5)
paper_btn.grid(row=0, column=1, padx=8, pady=5)
scissors_btn.grid(row=0, column=2, padx=8, pady=5)

score_display = tk.Label(window, text="Score → You: 0 | Computer: 0", font=("Arial", 12), bg="#e6f7ff")
score_display.pack(pady=20)

reset_btn = tk.Button(window, text="🔄 Reset Game", command=restart)
reset_btn.pack(pady=10)

# Run the app
window.mainloop()

import tkinter as tk
import random
import time 

root = tk.Tk()
root.title("Reaction time test for RRT units")
root.geometry("550x400")
title_label = tk.Label(root, text="Reaction Time test for RRT units", font=("Arial", 21))
title_label.pack(pady=10)
info_label = tk.Label(root, text="Press start to begin for a 4 piece chicken mcnugget", font=("Arial",14))
info_label.pack(pady=20)

start_btn = tk.Button(root, text="start", width=10)
start_btn.pack(pady=5)
stop_btn = tk.Button(root, text="stop", width=10, state="disabled")
stop_btn.pack(pady=5)


game_running = False
start_time = 0
def start_game():
    global agme_running, start_time
    info_label.config(text="wait for green...", fg="black")
    root.config(bg="red")
    start_btn.config(state="disabled")
    stop_btn.config(state="disabled")
    game_running = False

    wait = random.randint(2000, 5000)
    root.after(wait, turn_green)

def turn_green():
    global game_running,start_time
    root.config(bg="green")
    info_label.config(text="CLICK STOP!", fg="white")
    stop_btn.config(state="normal")
    start_time = time.time()
    game_running = True

def stop_game():
    global game_running
    if not game_running:
        info_label.config(text="Do ten push ups! wait for it to turn green.", fg="blue")
        return
    game_running =False
    end_time = time.time()
    reaction = round((end_time - start_time) * 1000)
    info_label.config(text=f"Your time: {reaction} ms", fg="blue")
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")
    root.config(bg="SystemButtonFace")

start_btn.config(command=start_game)
stop_btn.config(command=stop_game)

root.mainloop()

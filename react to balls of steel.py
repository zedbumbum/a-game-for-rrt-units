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







root.mainloop()
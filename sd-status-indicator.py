# Copyright (C) 2024 alby13
# Release v1.0 - April 25, 2024
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# sd-status-indicator_v1.py
# Stable Diffusion Status Indicator Utility
# A Python utility to monitor CPU and GPU usage to notify the 
# user if Stable Diffusion is ready to be used or not.

#!/usr/bin/python3
import tkinter as tk
import psutil
import time
import GPUtil

print("")
print("SD Status Indicator is running.")
print("The window will turn red when GPU usage is above ~70%")
print("Close the status window to quit the program.")

# Create Status Indicator Window
win = tk.Tk()
win.title(" ")
win.geometry("210x210+0+0")
canvas001 = tk.Canvas(win, width=180, height=180, bg="black", highlightthickness=0)
oval001 = canvas001.create_oval(5, 5, 180, 180, fill="black")
canvas001.pack()
win.configure(bg='black')
win.attributes("-topmost", True)
mylabel001=tk.Label(win,text=" ",font=("ubuntu",10,"bold"), fg = "white", bg="black")

# Logic for dragging the window by grabbing with the mouse
def start_drag(event):
    win.x = event.x
    win.y = event.y

def drag(event):
    deltax = event.x - win.x
    deltay = event.y - win.y
    x = win.winfo_x() + deltax
    y = win.winfo_y() + deltay
    win.geometry(f"+{x}+{y}")

win.bind("<ButtonPress-1>", start_drag)
win.bind("<B1-Motion>", drag)

# Initialize the CPU and GPU usage monitoring
def tmp_update():
    gpus = GPUtil.getGPUs()
    cpu_usage = psutil.cpu_percent()
    cpu_usage = cpu_usage * 4
    if cpu_usage > 100:
        cpu_usage = 100
    gpu_usage = gpus[0].load * 100
    gpu_usage = int(gpu_usage)
    #print(cpu_usage)
    #print(gpu_usage)
    temp_var = "CPU:" + str(cpu_usage) + "% | " + "GPU:" + str(gpu_usage) + "% "
    return temp_var, gpu_usage

# Update the window with usage and color changing functions
def update_usage():
    win.after(1000, update_usage)
    var = tmp_update()
    gpu_usage=var[1]
    mylabel001.config(text=var[0],font=("ubuntu",10,"bold"), fg = "white", bg="black")
    mylabel001.pack()
    if gpu_usage < 69:
        canvas001.itemconfig(oval001, fill='green')
        win.title("Ready")
    else:
        canvas001.itemconfig(oval001, fill='red')
        mylabel001.pack()
        win.title("Wait")

update_usage() 
#mylabel.pack()
win.mainloop()
print("")
print("Quitting SD Status Indicator.")

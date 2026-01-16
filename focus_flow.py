'''
An app called Focus Flow that is focused on implementing studying methods such as the Pomodoro method with tools such as a timer, history log, and via

1. Pomodoro timer 
2. Session logging
3. Build analytics view
4. Add study history view
5. Polish the UI

'''

from tkinter import *

time_left = 1500
timer_running = False

# creates the tkinter window for Focus Flow
window = Tk()
window.title("Focus Flow")
window.geometry("400x300")

# adds the timer label
timer_label = Label(window, text="25:00", font=("Arial", 48))
timer_label.pack(pady=50)

# function to start the timer


def start_timer():
    global timer_running

    if not timer_running:
        timer_running = True
        countdown(time_left)

# function for timer countdown


def countdown(seconds):
    global timer_running, time_left

    if seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        window.after(1000, countdown, seconds - 1)
    else:
        timer_label.config(text="Done!")
        print("Work session complete!")
        timer_running = False
        time_left = 1500


# adds the start button
start_button = Button(window, text="Start", font=(
    "Arial", 16), command=start_timer)
start_button.pack(pady=50)


# runs the window indefinitely
window.mainloop()

'''
An app called Focus Flow that is focused on implementing studying methods such as the Pomodoro method with tools such as a timer, history log, and via

1. Pomodoro timer 
2. Session logging
3. Build analytics view
4. Add study history view
5. Polish the UI

'''

from tkinter import *
import json
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


time_left = 1500  # 1500
timer_running = False
work_time = 1500  # 1500
break_time = 300  # 300
is_break = False
current_subject = ""

# creates the tkinter window for Focus Flow
window = Tk()
window.title("Focus Flow")
window.geometry("500x400")

# display the time
timer_label = Label(window, text=work_time, font=("Arial", 48))
timer_label.pack(pady=50)

# display the current subject being studied
session_label = Label(window, text="", font=("Arial", 12))
session_label.pack(pady=5)

# display the subject box where user will type and enter subject
subject_label = Label(window, text="Subject:", font=("Arial", 14))
subject_label.pack(pady=5)

subject_entry = Entry(window, font=("Arial", 14), width=20)
subject_entry.pack(pady=5)

# function to start the timer


def start_timer():
    global timer_running, current_subject

    if not timer_running:
        current_subject = subject_entry.get()

        if current_subject.strip() == "":
            current_subject = "Unknown"

        print(f"Starting study session for: {current_subject}")
        session_label.config(text=f"Studying: {current_subject} ")
        timer_running = True
        countdown(work_time)

# start the timer countdown


def countdown(seconds):
    global timer_running, time_left, is_break

    if seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        window.after(1000, countdown, seconds - 1)
    else:
        if not is_break:
            print("WORK SESSION COMPLETE!")
            timer_label.config(text="BREAK TIME!")
            save_session()
            is_break = True
            window.after(2000, lambda: countdown(break_time))
        else:
            print("BREAK COMPLETE!")
            timer_label.config(text="BACK TO WORK!")
            is_break = False
            window.after(2000, reset_timer)

# reset time after break is complete


def reset_timer():
    global timer_running, time_left, is_break

    work_mins = work_time // 60
    work_secs = work_time % 60
    timer_label.config(text=f"{work_mins:02d}:{work_secs:02d}")
    timer_running = False
    is_break = False
    time_left = work_time
    session_label.config(text="")

# save after a full session (work + break)


def save_session():
    session_data = {
        "Subject": current_subject,
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Duration": work_time // 60
    }

    try:
        with open("study_history.json", "r") as file:
            sessions = json.load(file)
    except FileNotFoundError:
        sessions = []

    sessions.append(session_data)
    with open("study_history.json", "w") as file:
        json.dump(sessions, file, indent=4)

    print(f"Session saved: {session_data}")

# a separate window for a dashboard to analyze the study sessions


def view_analytics():
    print("Analytics button clicked!")

    # create the window
    analytics_window = Toplevel(window)
    analytics_window.title("Study Sessions Analytics")
    analytics_window.geometry("600x400")

    # add a test label
    test_label = Label(
        analytics_window, text="Analytics Dashboard", font=("Arial", 20))
    test_label.pack(pady=20)

    # test if json file exists for study session
    try:
        with open("study_history.json", "r") as file:
            sessions = json.load(file)
    except FileNotFoundError:
        sessions = []

    '''
    if the number of sessions is 0, print a message
    otherwise, print the total number of sessions
    '''
    if len(sessions) == 0:
        no_data_label = Label(
            analytics_window, text="No study sessions yet!", font=("Arial", 16))
        no_data_label.pack(pady=20)
        return
    else:
        total_sessions = len(sessions)
        total_minutes = 0
        for session in sessions:
            total_minutes += session["Duration"]
        total_hours = total_minutes // 60

    # calculate hours per subject
    subject_data = {}
    for session in sessions:
        subject = session["Subject"]
        duration = session["Duration"]

        if subject in subject_data:
            subject_data[subject] += duration
        else:
            subject_data[subject] = duration

    print(f"Total sessions: {total_sessions}")
    print(f"Total hours: {total_hours}")
    print(f"Subject data: {subject_data}")

    # display analytics in Tk window
    stats_text = f"Total Sessions: {total_sessions} \n Total Hours: {total_hours}"
    stats_label = Label(analytics_window, text=stats_text, font=("Arial", 14))
    stats_label.pack(pady=10)

    # Create bar chart
    subjects = list(subject_data.keys())
    # Convert minutes to hours
    hours = [subject_data[s] / 60 for s in subjects]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(subjects, hours)
    ax.set_xlabel("Subject")
    ax.set_ylabel("Hours")
    ax.set_title("Study Time by Subject")

    fig.tight_layout()

    # Embed chart in Tkinter window
    canvas = FigureCanvasTkAgg(fig, analytics_window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    # a button to view history of study sessions
    history_button = Button(analytics_window, text="VIEW SESSION HISTORY", font=(
        "Arial", 12), command=lambda: show_history(sessions))
    history_button.pack(pady=10)

# show history of sessions


def show_history(sessions):
    history_window = Toplevel(window)
    history_window.title("Study History")
    history_window.geometry("500x400")

    history_label = Label(
        history_window, text="Session History", font=("Arial", 10))
    history_label.pack(pady=10)

    for session in sessions:
        session_text = f"{session['Date']} {session['Time']} - {session['Subject']} ({session['Duration']} min)"
        session_label = Label(
            history_window, text=session_text, font=("Arial", 20))
        session_label.pack(anchor='w', padx=20)


# organize button to be placed side by side

button_frame = Frame(window)
button_frame.pack(pady=20)

# add the start button
start_button = Button(button_frame, text="START", font=(
    "Arial", 16), command=start_timer)
start_button.pack(side=LEFT, padx=20)

# add the analytics button
analytics_button = Button(button_frame, text="VIEW ANALYTICS", font=(
    "Arial", 16), command=view_analytics)
analytics_button.pack(side=LEFT, padx=20)


# runs the window indefinitely
window.mainloop()

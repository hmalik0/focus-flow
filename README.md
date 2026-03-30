# Focus Flow

A study productivity application built with Python that helps students maximize focus and build better study habits using the Pomodoro Technique. Features real-time session tracking, analytics visualization, and study history management.

## Features

- **Pomodoro Timer**: 25-minute focused work sessions with automatic 5-minute breaks
- **Subject Tracking**: Tag each study session by subject (Math, CS, History, etc.)
- **Session Logging**: Automatically saves all completed sessions with timestamps
- **Analytics Dashboard**: 
  - Total sessions and study hours
  - Bar chart visualization of time invested per subject
  - Study session history with full details
- **Clean UI**: Simple, distraction-free interface built with Tkinter

## Tech Stack

- **Python 3** - Core application logic
- **Tkinter** - GUI framework
- **Matplotlib** - Data visualization for analytics
- **JSON** - Local data persistence
- **Datetime** - Session timestamp management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hmalik0/focus-flow.git
cd focus-flow
```

2. Install dependencies:
```bash
pip install matplotlib
```

Or if using Anaconda:
```bash
conda install matplotlib
```

## Usage

Run the application:
```bash
python3 focus_flow.py
```

**Workflow:**
1. Enter the subject you're studying
2. Click START to begin a 25-minute work session
3. Timer automatically starts a 5-minute break after work completes
4. Click VIEW ANALYTICS to see your study patterns and history

## Project Structure
```
focus-flow/
├── focus_flow.py          # Main application
├── study_history.json     # Session data (auto-generated)
└── README.md
```

## Why I Built This

As a CS student preparing for internships, I struggled with maintaining focus during study sessions and understanding where my time was actually going. Focus Flow solves both problems by enforcing structured study intervals while providing data-driven insights into study habits.

## Key Learning Outcomes

- **GUI Development**: Built interactive multi-window application with Tkinter
- **Data Visualization**: Integrated Matplotlib charts into Tkinter interface
- **State Management**: Handled complex timer states (work/break modes, global variables)
- **File I/O**: Implemented JSON-based data persistence
- **Software Design**: Structured code with clear separation of concerns

## Future Enhancements

- Additional study techniques (Feynman, Active Recall, Spaced Repetition)
- Export study data to CSV
- Weekly/monthly progress reports
- Customizable timer durations
- Desktop notifications

---

**Built by Hamdaan Malik** | [GitHub](https://github.com/hmalik0) | Computer Science Student
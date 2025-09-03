# 🧠 Login Keylogger App – Colorful Keystroke Visualizer

This project is a GUI-based login interface built with Python's Tkinter that logs and visualizes keystrokes in real-time. It was created as part of a cybersecurity learning exercise to understand input monitoring, event handling, and secure logging.

> ⚠️ **Disclaimer:** This tool is intended strictly for educational and ethical use. Do not deploy or distribute it for unauthorized keylogging or surveillance.

---

## 🎯 Project Objective

Build a simple login interface that:
- Captures and logs keystrokes from username and password fields
- Displays keystrokes in real-time with color-coded formatting
- Saves logs to timestamped `.txt` files for review

---

## 🛠 Features

- ✅ Real-time keystroke logging
- 🎨 Color-coded display:
  - Blue for timestamps
  - Green for regular characters
  - Red for special keys (Enter, Backspace, etc.)
- 📁 Logs saved to uniquely named files (e.g., `keylog_2025-09-03_15-55-00.txt`)
- 🖥️ Responsive GUI built with Tkinter and ttk

---

## 📦 Technologies Used

- Python 3
- Tkinter (GUI)
- ttk (Themed widgets)
- datetime (Timestamping)

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Login-Keylogger-App.git
   cd Login-Keylogger-App
   
2. Run the script:
bash
python keylogger_app.py

3. Type in the username and password fields. Keystrokes will be logged and displayed in real-time.

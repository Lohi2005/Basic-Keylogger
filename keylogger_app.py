import tkinter as tk
from tkinter import ttk
import datetime

log_file = f"keylog_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

class LoginKeyLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page with Colorful Keylogging")

        # Set window size
        self.root.geometry("900x600")

        # Use monospace font for logs
        self.log_font = ("Consolas", 11)

        # Username label and entry
        ttk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=10, sticky='w')
        self.username_entry = ttk.Entry(root, width=40)
        self.username_entry.grid(row=0, column=1, padx=5, pady=10, sticky='w')
        self.username_entry.focus()

        # Password label and entry
        ttk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=10, sticky='w')
        self.password_entry = ttk.Entry(root, width=40, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=10, sticky='w')

        # Login button
        self.login_button = ttk.Button(root, text="Login", command=self.stop_logging)
        self.login_button.grid(row=2, column=1, sticky='e', padx=5, pady=10)

        # Labels and text boxes for live keystroke logs
        ttk.Label(root, text="Username Keystrokes:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.username_log = tk.Text(root, height=20, width=50, state='disabled', bg="#fff9c4", font=self.log_font)
        self.username_log.grid(row=4, column=0, padx=5, pady=5)

        ttk.Label(root, text="Password Keystrokes:").grid(row=3, column=1, padx=5, pady=5, sticky='w')
        self.password_log = tk.Text(root, height=20, width=50, state='disabled', bg="#b2ebf2", font=self.log_font)
        self.password_log.grid(row=4, column=1, padx=5, pady=5)

        # Configure tags for colors
        for text_widget in [self.username_log, self.password_log]:
            text_widget.tag_configure("timestamp", foreground="blue")
            text_widget.tag_configure("char", foreground="green")
            text_widget.tag_configure("special", foreground="red")

        # Start logging flags
        self.logging = True

        # Bind keypress events ONLY to username and password entries
        self.username_entry.bind('<KeyPress>', self.log_username_key)
        self.password_entry.bind('<KeyPress>', self.log_password_key)

        # Open file for appending logs
        self.logfile_handle = open(log_file, "a")

    def log_username_key(self, event):
        if not self.logging:
            return
        self._log_key(event, self.username_log, "Username")

    def log_password_key(self, event):
        if not self.logging:
            return
        self._log_key(event, self.password_log, "Password")

    def _log_key(self, event, text_widget, field_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        char = event.char if event.char else f"Key.{event.keysym}"
        is_special = False
        if not event.char or event.keysym in ("Return", "BackSpace", "Tab", "Escape", "Delete", "Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R"):
            is_special = True

        # Write to file
        log_line = f"{timestamp} - {char}\n"
        self.logfile_handle.write(f"{field_name}: {log_line}")
        self.logfile_handle.flush()

        # Insert to Text widget with colors
        text_widget.config(state='normal')

        # Insert timestamp
        text_widget.insert(tk.END, timestamp, "timestamp")
        text_widget.insert(tk.END, " - ")

        # Insert char or special key in color
        if is_special:
            text_widget.insert(tk.END, char, "special")
        else:
            text_widget.insert(tk.END, f"'{char}'", "char")

        text_widget.insert(tk.END, "\n")
        text_widget.see(tk.END)
        text_widget.config(state='disabled')

    def stop_logging(self):
        self.logging = False
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Login attempt:\nUsername: {username}\nPassword: {password}")
        self.append_log(self.username_log, "\nLogging stopped.\n")
        self.append_log(self.password_log, "\nLogging stopped.\n")

        self.username_entry.config(state='disabled')
        self.password_entry.config(state='disabled')
        self.login_button.config(state='disabled')

        self.logfile_handle.close()

    def append_log(self, text_widget, text):
        text_widget.config(state='normal')
        text_widget.insert(tk.END, text)
        text_widget.see(tk.END)
        text_widget.config(state='disabled')

def main():
    root = tk.Tk()
    app = LoginKeyLoggerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

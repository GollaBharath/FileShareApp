import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys
import shutil

def is_frozen():
    return getattr(sys, 'frozen', False)

def get_resource_path(filename: str) -> str:
    if is_frozen():
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(__file__), filename)

def launch_script(script_name: str):
    try:
        script_path = get_resource_path(script_name)

        # Extract to temp dir if frozen
        if is_frozen():
            temp_path = os.path.join(os.environ["TEMP"], script_name)
            shutil.copyfile(script_path, temp_path)
            subprocess.Popen([sys.executable, temp_path])
        else:
            subprocess.Popen([sys.executable, script_path])

    except Exception as e:
        messagebox.showerror("Error", f"Failed to open {script_name}: {e}")

def launch_sender():
    launch_script("client.py")

def launch_receiver():
    launch_script("server.py")

root = tk.Tk()
root.title("File Transfer App")
root.geometry("300x180")

tk.Label(root, text="Welcome to File Share", font=("Helvetica", 14)).pack(pady=10)

send_btn = tk.Button(root, text="Send File", width=20, command=launch_sender)
send_btn.pack(pady=10)

receive_btn = tk.Button(root, text="Receive File", width=20, command=launch_receiver)
receive_btn.pack(pady=5)

root.mainloop()

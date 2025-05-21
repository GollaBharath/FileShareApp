import tkinter as tk
from tkinter import ttk
from client import start_client
from server import start_server

def launch_client():
    start_client()

def launch_server():
    start_server()

root = tk.Tk()
root.title("File Transfer App")
root.geometry("300x200")

send_button = ttk.Button(root, text="Send File", command=launch_client)
send_button.pack(pady=20)

receive_button = ttk.Button(root, text="Receive File", command=launch_server)
receive_button.pack(pady=20)

root.mainloop()

import socket
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import struct

def send_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    ip = ip_entry.get().strip()
    if not ip:
        messagebox.showwarning("Missing IP", "Enter the receiver's IP address.")
        return

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, 5001))
        log_box.insert(tk.END, f"Connected to {ip}\n")

        # Prepare filename
        filename = os.path.basename(file_path)
        filename_bytes = filename.encode()
        filename_len = struct.pack('!I', len(filename_bytes))

        # Send filename length and filename
        client.sendall(filename_len)
        client.sendall(filename_bytes)

        log_box.insert(tk.END, f"Sending file: {filename}\n")

        # Send file content
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                client.sendall(data)

        log_box.insert(tk.END, f"File '{filename}' sent successfully!\n\n")
        client.close()

    except Exception as e:
        messagebox.showerror("Send Error", f"Error: {e}")

    log_box.see(tk.END)

root = tk.Tk()
root.title("File Sender")

tk.Label(root, text="Receiver IP Address:").pack(pady=(10, 0))
ip_entry = tk.Entry(root, width=40)
ip_entry.pack(pady=(0, 10))

send_button = tk.Button(root, text="Choose File and Send", command=send_file)
send_button.pack(pady=5)

log_box = scrolledtext.ScrolledText(root, width=50, height=15)
log_box.pack(padx=10, pady=10)

root.mainloop()

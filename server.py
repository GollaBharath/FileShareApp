def start_server():
    import socket
    import tkinter as tk
    from tkinter import scrolledtext, messagebox
    import threading
    import struct

    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    HOST = '0.0.0.0'
    PORT = 5001

    def start_server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((HOST, PORT))
                s.listen(1)
                log_box.insert(tk.END, f"Server started, listening on port {PORT}\n")
                log_box.insert(tk.END, f"Your LAN IP: {LAN_IP}\n")
                log_box.see(tk.END)

                while True:
                    log_box.insert(tk.END, "Waiting for connection...\n")
                    log_box.see(tk.END)
                    conn, addr = s.accept()
                    with conn:
                        log_box.insert(tk.END, f"Connected by {addr}\n")
                        log_box.see(tk.END)

                        # Receive filename length (4 bytes)
                        raw_len = conn.recv(4)
                        if not raw_len:
                            log_box.insert(tk.END, "Connection closed by sender.\n")
                            return
                        filename_len = struct.unpack('!I', raw_len)[0]

                        # Receive filename
                        filename = conn.recv(filename_len).decode()
                        log_box.insert(tk.END, f"Receiving file: {filename}\n")
                        log_box.see(tk.END)

                        # Receive file content
                        with open(filename, 'wb') as f:
                            while True:
                                data = conn.recv(4096)
                                if not data:
                                    break
                                f.write(data)

                        log_box.insert(tk.END, f"File '{filename}' received successfully!\n\n")
                        log_box.see(tk.END)

            except Exception as e:
                messagebox.showerror("Server Error", f"Error: {e}")

    def on_start_receiving():
        start_button.config(state=tk.DISABLED)
        threading.Thread(target=start_server, daemon=True).start()

    root = tk.Tk()
    root.title("File Receiver")

    log_box = scrolledtext.ScrolledText(root, width=50, height=15)
    log_box.pack(padx=10, pady=10)

    start_button = tk.Button(root, text="Start Receiving", command=on_start_receiving)
    start_button.pack(pady=5)

    LAN_IP = get_local_ip()

    root.mainloop()

if __name__ == "__main__":
    start_server()

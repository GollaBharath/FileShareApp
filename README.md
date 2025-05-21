# File Transfer App

A simple file sharing tool built in Python using sockets and tkinter. Works over the same Wi-Fi.

## How to Use

1. Run `main_app.py`
2. Choose to **Send** or **Receive**
3. Devices must be on the same Wi-Fi
4. Sender enters the receiver’s IP and port

## Build `.exe` (Optional)

```bash
pyinstaller --noconsole --onefile --add-data "client.py;." --add-data "server.py;." main_app.py
```

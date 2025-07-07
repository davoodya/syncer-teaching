from settings import *
from pyperclip import copy
import socket

def send_clipboard(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            sock.sendall(data.encode('utf-8'))
        print("[✅] Send Clipboard to Linux Server")
    except Exception as e:
        print(f"[❌] Error sending clipboard to Linux Server:\nError: {e}")


if __name__ == "__main__":
    texts = ''
    while texts != "exit":
        texts = input('enter text for send to linux\n:: ')
        send_clipboard(texts)
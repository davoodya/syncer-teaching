import socket

from settings import SERVER_IP, SERVER_PORT, CLIENT_RECEIVE_PORT

last_clipboard = ""


def send_clipboard(text):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(text.encode('utf-8'))
            print(f"Data({text}) Send to Server.")

    except Exception as e:
        print(f"Error while sending data: {e}")


if __name__ == "__main__":
    while True:
        text = input("enter text to send: ")
        send_clipboard(text)

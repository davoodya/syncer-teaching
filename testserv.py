import socket
from threading import Thread
from pyperclip import paste, copy
from settings import WINDOWS_CLIENT_IP, CLIENT_RECEIVE_PORT

last_clipboard = ''


def start_receive_server(port=65432):
    server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"Listening for Windows Clipboard on Port: {port}")

    while True:
        conn, addr = server.accept()
        Thread(target=handle_client_connection, args=(conn, addr)).start()

def handle_client_connection(conn, addr):
    #  step 0: receive data from windows client
    data = conn.recv(4096)

    # step 1: decode data
    try:
        decoded = data.decode("utf-8")
    except Exception as e:
        decoded = f"Error when decoding data.\nError: {e}"
        print(f"Error when decoding data:\nError: {e}")

    print(f"Received '{decoded}' from Windows(IP: {addr[0]}, PORT: {addr[1]}).")

    # step 2: copy to clipboard
    with open("PC_Received.txt", "a", encoding="utf-8") as f:
        f.write(decoded + "\n\n")

    # step 3: copy to clipboard
    copy(decoded)

    print(f"Data({decoded}) written to PC_Received.txt and pasted to clipboard")

    # step 4: close connection
    conn.close()

if __name__ == "__main__":
    start_receive_server()
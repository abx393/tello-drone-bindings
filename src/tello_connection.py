"""
Script to interact with the DJI Ryze Tello Drone in a CLI
"""

import threading
import socket
import sys
import time

HOST = ""
PORT = 7100
LOCAL_ADDRESS = (HOST, PORT)
TELLO_ADDRESS = ("192.168.10.1", 8889)


def recv():
    pass


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(LOCAL_ADDRESS)

    print("\n\nTello Python Demo.\n")

    recvThread = threading.Thread(target=recv)
    recvThread.start()

    while True:
        try:
            message = input("")

            if not message:
                break

            if "end" in message:
                print("...")
                sock.close()
                break

            # Send data to Tello
            message = message.encode(encoding="UTF-8")
            sent = sock.sendto(message, TELLO_ADDRESS)

        except KeyboardInterrupt:
            print("\n . . . \n")
            sock.close()
            break


if __name__ == "__main__":
    main()

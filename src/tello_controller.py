"""
Python wrapper class to interact with the DJI Ryze Tello drone using keyboard
input
"""

import sys
import time
import numpy as np

import threading
import socket
import keyboard
import warnings

import h264decoder
import cv2

from key_bindings import check_key_press

# TODO: test responsiveness of key held down


class TelloController:
    def __init__(
        self,
        local_udp_port=3000,
        local_video_udp_port=11111,
        tello_ip="192.168.10.1",
        tello_command_udp_port=8889,
    ):

        self.local_udp_port = local_udp_port
        self.local_video_udp_port = local_video_udp_port
        self.tello_ip = tello_ip
        self.tello_command_udp_port = tello_command_udp_port

        self.command_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.command_socket.bind(("", self.local_udp_port))

        self.video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.video_socket.bind(("", self.local_video_udp_port))

        self.video_decoder = h264decoder.H264Decoder()

        self.listening = False
        self.mode = "idle"
        self.airborne = False

    def receive_command_socket(self):
        while True:
            try:
                data, server = self.command_socket.recvfrom(1518)
                data_decoded = data.decode("utf-8")
                print(data_decoded)
            except Exception or KeyboardInterrupt:
                break

    def h264_decode(self, packet_data):
        frames_decoded = []
        frames = self.video_decoder.decode(packet_data)
        for frame_data in frames:
            (frame, width, height, line_size) = frame_data
            if frame is not None:
                frame = np.fromstring(frame, dtype=np.ubyte, count=len(frame), sep="")
                frame = frame.reshape((height, line_size // 3, 3))
                frame = frame[:, :width, :]
                frames_decoded.append(frame)

        return frames_decoded

    def receive_video_socket(self):
        packet_data = b""
        while True:
            try:
                res_string, ip = self.video_socket.recvfrom(4096)
                packet_data += res_string

                # if end of current frame is reached
                if len(res_string) != 1460:
                    for frame in self.h264_decode(packet_data):
                        cv2.imshow("Tello POV", frame)
                        cv2.waitKey(25)
                    packet_data = b""

            except KeyboardInterrupt:
                cv2.destroyAllWindows()
                break
            except socket.error as err:
                print("Caught exception socket.error : " + str(err))
                cv2.destroyAllWindows()
                break

    def send(self, message):
        self.command_socket.sendto(
            message.encode("UTF-8"), (self.tello_ip, self.tello_command_udp_port)
        )

    def command(self):
        if not self.listening:
            warnings.warn(
                "Must activate receiver thread (ie., controller.start()) "
                + "before activating 'command' mode."
            )
        print("command ", end="")
        self.send("command")
        self.mode = "command"

    def streamon(self):
        self.send("streamon")

    def takeoff(self):
        if not self.mode == "command":
            warnings.warn("Must be in 'command' mode to takeoff.")
        print("takeoff ", end="")
        self.send("takeoff")
        self.airborne = True

    def land(self):
        if not self.mode == "command":
            warnings.warn("Must be in 'command' mode to land.")
        print("land ", end="")
        self.send("land")
        self.airborne = False

    def ascend(self, height):
        if not self.airborne:
            warnings.warn("Must takeoff first.")
        self.send("up " + str(height))

    def descend(self, height):
        if not self.airborne:
            warnings.warn("Must takeoff first.")
        self.send("down " + str(height))

    def yaw_right(self, angle):
        self.send("cw " + str(angle))

    def yaw_left(self, angle):
        self.send("ccw " + str(angle))

    def roll_left(self, dist):
        if not self.airborne:
            warnings.warn("Must takeoff first.")
        self.send("left " + str(dist))

    def roll_right(self, dist):
        if not self.airborne:
            warnings.warn("Must takeoff first.")
        self.send("right " + str(dist))

    def pitch_forward(self, dist):
        if not self.airborne:
            warnings.warn("Must takeoff first.")
        self.send("forward " + str(dist))

    def pitch_backward(self, dist):
        if not self.airborne:
            warnings.warn("Must takeoff first.")
        self.send("back " + str(dist))

    def flip(self, direction="f"):
        self.send("flip " + direction)

    def start(self):
        self.listening = True
        print("Listening...")
        self.command()
        self.streamon()
        self.receive_command_thread = threading.Thread(
            target=self.receive_command_socket
        )
        self.receive_command_thread.start()

        self.receive_video_thread = threading.Thread(target=self.receive_video_socket)
        self.receive_video_thread.start()

        while True:
            try:
                check_key_press(
                    self.takeoff,
                    self.land,
                    self.ascend,
                    self.descend,
                    self.yaw_right,
                    self.yaw_left,
                    self.roll_right,
                    self.roll_left,
                    self.pitch_forward,
                    self.pitch_backward,
                    self.flip,
                )
            except KeyboardInterrupt:
                print("Exiting...")
                self.video_socket.close()
                self.command_socket.close()
                break

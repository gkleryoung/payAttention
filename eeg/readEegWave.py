import serial
import time

# Create a serial object to represent the connection.
ser = serial.Serial("/dev/cu.usbmodem101", 9600)
time.sleep(2)  # wait for the serial connection to initialize.

with open("wave_data.txt", "a") as file:
    while True:
        if ser.in_waiting > 0:
            line = (
                ser.readline().decode("utf-8").rstrip()
            )  # read a byte string and decode it to a string.
            print(line)
            timestamp = time.strftime("%H:%M:%S")
            file.write(timestamp + " " + line + "\n")
            file.flush()
            time.sleep(0.15)

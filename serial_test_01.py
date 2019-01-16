import serial
import time

ser = serial.Serial('/dev/ttyS0', 115200, timeout=0)

def start_serial():
    ser.write(b'\r\r')
    time.sleep(0.5)
    ser.flushInput()


def read_msg(msg):
    response = ""
    ser.flushOutput()
    msg = msg + "\r"
    msg=msg.encode()
    ser.write(msg)
    time.sleep(0.1)
    while response != "".encode():
        response = ser.readline()
        time.sleep(0.1)
        if response != "dwm> ".encode() and response.decode().strip() != msg.decode().strip():
            # do whatever you want with this response
            print(response.decode().strip())
    ser.flushInput()

# Start serial and send double \r to enter shell
start_serial()
# read anchors list
read_msg("la")
# read unit modes
read_msg("nmg")
# read accelerometer values
read_msg("av")


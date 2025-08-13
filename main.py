import eel
import serial
import webview

# Start serial communication to arduino
# *** Make sure your port and baud rate is correct ***
ser = serial.Serial('COM9', 115200) # This line is for PC testing purposes
# ser = serial.Serial("/dev/ttyACM0", 115200) # This line is for Raspberry Pi 

# Initialize Eel Library
eel.init('web')

# Eel API allows data to be sent on serial communication
@eel.expose
def send_data(message):
    ser.write((message + '\n').encode())
    print(f"Sent to Arduino: {message}")

webview.create_window(
    "Assistive Technology Remote",
    "web/index.html",
    width=480,
    height=800,
    resizable=False
)

webview.start()
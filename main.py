import eel
import serial

# Start serial communication to arduino
# *** Make sure your port and baud rate is correct ***
# ser = serial.Serial('COM9', 115200, timeout=None) # This line is for PC testing purposes (Should be commented before commits)
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=None) # This line is for Raspberry Pi (Should be used for raspberry pi in dev)

# Initialize Eel Library
eel.init('web')

# Eel API allows data to be sent on serial communication
@eel.expose
def send_data(message):
    ser.write((message + '\n').encode())
    print(f"Sent to Arduino: {message}")

# Start hosting index.html with Eel
eel.start('index.html', size=(480, 800), port=5000)
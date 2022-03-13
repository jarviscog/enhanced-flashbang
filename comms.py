import serial
import struct

arduino = serial.Serial()
arduino.port = 'COM4'  # TODO: ensure this is the correct port for the arduino
arduino.baudrate=9600
arduino.timeout=0.1
arduino.open()

# this will send a signal to the arduino to turn the lights on for a few seconds
def turn_on_lights():
    arduino.write(struct.pack('>1B', int(7)))


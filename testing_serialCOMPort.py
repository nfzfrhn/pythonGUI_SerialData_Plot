from serial import *
import serial.tools.list_ports

#print([comport.device for comport in serial.tools.list_ports.comports()])

#ports = serial.tools.list_ports.comports()

#for port, desc in sorted(ports):
#    print("{}: {}".format(port.device, desc))

#print(ports)

#print([serial.tools.list_ports.comports()])

ser = Serial()
ser.baudrate=115200
ser.port = 'COM11'

if ser.isOpen():
    ser.close()
ser.open()    
if ser.isOpen():
    print("Connection success!")
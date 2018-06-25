import serial
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600


for i in range(100):

    for x in range(0, 254, 1):
        ser.write(x.to_bytes(1, byteorder='big'))
        time.sleep(0.01)
        #read_ser=ser.readline()
        #print(read_ser)


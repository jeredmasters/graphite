from multiprocessing import Process, Value
from flask import Flask, render_template
import datetime
import serial
import time
import struct

app = Flask(__name__)
status = 0

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   toggle()
   return render_template('index.html', **templateData)

def webserver(s):
    global status
    status = s
    app.run(debug=True, port=80, host='0.0.0.0', threaded=True)

def toggle():
    global status
    if (status.value == 0):
        status.value = 254
    else:
        status.value = 0

def ledLoop(status):
    ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
    ser.baudrate=9600

    prev_status = 100
    while True:
        if status.value != prev_status:
            by = status.value.to_bytes(1, byteorder='big')
            print(by)
            ser.write(status.value.to_bytes(1, byteorder='big'))
            prev_status = status.value
        time.sleep(0.05)

if __name__ == '__main__':
    s = Value('i', 0)
    Process(target=ledLoop, args=(s,)).start()
    Process(target=webserver, args=(s,)).start()



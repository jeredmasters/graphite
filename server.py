from multiprocessing import Process, Value
from flask import Flask, render_template
from datetime import datetime, timedelta
import time
import serial
import time
import struct
import platform

app = Flask(__name__)
status = 0

@app.route("/")
def hello():
   now = datetime.now()
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

def writeLed(value):
    global ser
    print(value)
    if ser != 0:
        ser.write(value.to_bytes(1, byteorder='big'))

def ledLoop(s):
    global status
    global ser
    status = s
    
    if platform.system() == "Windows":
        ser=0
    else:
        ser=serial.Serial("/dev/ttyACM0",9600)
        ser.baudrate=9600

    

    prev_status = 100
    while True:
        time.sleep(0.01)
        alarm()
        if status.value != prev_status:
            prev_status = status.value
            writeLed(status.value)            

def alarm():
    global status
    now = datetime.now() + timedelta(hours = 8)
    h = now.time().hour
    m = now.time().minute
    s = now.time().second
    if h == 5:
        if m >= 30:
            s = s + (m - 30) * 60
            status.value = int((s * 255) / 1860)
    if h == 6:
        status.value = 254

if __name__ == '__main__':
    s = Value('i', 0)
    Process(target=ledLoop, args=(s,)).start()
    Process(target=webserver, args=(s,)).start()



import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")
   
print('This is a Countdown timer!')
sec = input("How many seconds? > ")
countdown(int(sec))
# app.py

from flask import Flask, render_template, request
import RPi.GPIO as GPIO

PIN1 = 17
PIN2 = 22
PIN3 = 23
PIN4 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.form['input_data']

    # Process the data as needed (you can print it for now)

    # add code manipulating GPIO pins here

    # WASD controls
    if data.upper() == "W":
        GPIO.output(PIN1, GPIO.LOW)
        GPIO.output(PIN2, GPIO.HIGH)
        GPIO.output(PIN3, GPIO.HIGH)
        GPIO.output(PIN4, GPIO.LOW)

    elif data.upper() == "A":
        GPIO.output(PIN1, GPIO.HIGH)
        GPIO.output(PIN2, GPIO.LOW)
        GPIO.output(PIN3, GPIO.HIGH)
        GPIO.output(PIN4, GPIO.LOW)

    elif data.upper() == "S":
        GPIO.output(PIN1, GPIO.HIGH)
        GPIO.output(PIN2, GPIO.LOW)
        GPIO.output(PIN3, GPIO.LOW)
        GPIO.output(PIN4, GPIO.HIGH)

    elif data.upper() == "D":
        GPIO.output(PIN1, GPIO.LOW)
        GPIO.output(PIN2, GPIO.HIGH)
        GPIO.output(PIN3, GPIO.LOW)
        GPIO.output(PIN4, GPIO.HIGH)
    
    # sound / taunts   

    elif data.upper() == "F":
        print("Trigger a sound to play if F is pressed")
    
    elif data.upper() == "G":
        print("Trigger a sound to play if G is pressed")

    elif data.upper() == "H":
        print("Trigger a sound to play if H is pressed")


    print(f"Received data: {data}")
    #return 'OK'

if __name__ == '__main__':
    app.run(debug=True)

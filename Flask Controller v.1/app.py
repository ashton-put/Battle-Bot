from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

PINS = {17,22,23,24}


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PINS, GPIO.OUT)
GPIO.setup(PINS, GPIO.OUT)

app = Flask(__name__)

@app.route("/forward_on", methods=["POST"])
def responseR1():
	GPIO.output(PINS, GPIO.HIGH)
	print("FORWARD")
	return "ok"


@app.route("/backward_on", methods=["POST"])
def responseY1():
	GPIO.output(PINS, GPIO.HIGH)
	print("BACKWARD")
	return "ok"


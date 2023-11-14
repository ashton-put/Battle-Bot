from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

RPIN = 18
YPIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RPIN, GPIO.OUT)
GPIO.setup(YPIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/Rled_on", methods=["POST"])
def responseR1():
	GPIO.output(RPIN, GPIO.HIGH)
	print("LED on")
	return "ok"

@app.route("/Rled_off", methods=["POST"])
def responseR0():
	GPIO.output(RPIN, GPIO.LOW)
	print("LED off")
	return "ok"

@app.route("/Yled_on", methods=["POST"])
def responseY1():
	GPIO.output(YPIN, GPIO.HIGH)
	print("LED on")
	return "ok"

@app.route("/Yled_off", methods=["POST"])
def responseY0():
	GPIO.output(YPIN, GPIO.LOW)
	print("LED off")
	return "ok"

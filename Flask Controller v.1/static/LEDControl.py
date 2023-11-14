from flask import Flask, render_template

app = Flask(__name__)

@app.route("/forward_on", methods=["POST"])
def led_on_r():
    print("FORWARD")
    return "ok"

@app.route("/backward_on", methods=["POST"])
def led_off_r():
    print("BACKWARD")
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Ashton Putnam")
    
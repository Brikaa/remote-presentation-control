from flask import Flask, render_template
from pynput.keyboard import Key, Controller

keyboard = Controller()

app = Flask(__name__)

def press_once(key):
  keyboard.press(key)
  keyboard.release(key)

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/right")
def right():
  press_once(Key.right)
  return ""

@app.route("/left")
def left():
  press_once(Key.left)
  return ""

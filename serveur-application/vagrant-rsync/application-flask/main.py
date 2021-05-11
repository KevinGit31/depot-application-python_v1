from flask import Flask
import crud
import Machine
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Kevin"

@app.route("/machine", methods=["POST"])
def create_machine():
  pass

@app.route("/machines", methods=["GET"])
def liste_machine():
    return crud.get_machines()

app.run()


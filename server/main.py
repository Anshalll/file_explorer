from flask import Flask, Response, jsonify
import os

app = Flask(__name__)


@app.route('/' , methods=["GET" , "POST"])
def INDEX():
    return jsonify(message= "project starts")

@app.route("/hello")
def Sendpath():
    return jsonify(path=os.getcwd())



app.run(debug=True)

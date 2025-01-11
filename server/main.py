from flask import Flask, Response, jsonify
app = Flask(__name__)


@app.route('/' , methods=["GET" , "POST"])
def INDEX():
    return jsonify(message= "project starts")



app.run(debug=True)

from flask import Flask, Response, jsonify
import os
import psutil

app = Flask(__name__)


@app.route('/' , methods=["GET" , "POST"])
def INDEX():
    return jsonify(message= "project starts")

@app.route("/getdata")
def Sendpath():
    
    drive_array= []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        drive_array.append(partition.device)

        
    
    return jsonify(data=drive_array)




app.run(debug=True)

from flask import Flask, Response, jsonify
import os
import shutil
import psutil
app = Flask(__name__)


@app.route('/' , methods=["GET" , "POST"])
def INDEX():
    return jsonify(message= "project starts")

@app.route("/getdata")
def Sendpath():
    
    drive_array= []
    
    for partition in psutil.disk_partitions():
    
       data = shutil.disk_usage(partition.device)

       converted_total = data.total / 1073741824
       converted_used = data.used / 1073741824
       converted_free = data.free / 1073741824
     
       fileinpath = os.listdir(partition.device)
       
       dict = {"partition_name": partition.device, "total": converted_total, "used": converted_used, "free": converted_free , "fileindir" : fileinpath}
       
       drive_array.append(dict)
        
       
    return jsonify(data=drive_array)


app.run(debug=True)

from flask import Flask, Response, jsonify, request
import os
import shutil
import psutil
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor
app = Flask(__name__)
CORS(app , origins=["http://localhost:3000"])

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

@app.route('/getpath/<string:path>' , methods=["GET" , "POST"])
def get_directory(path):
    try:
        data = os.listdir(path)
        
        return jsonify(pathdata = data)
    except:
        return jsonify(error="An error occured!")


@app.route("/rename" , methods=["PATCH"])
def renamepath():
        
        data = request.get_json() 
       
        full_existing = data["fullpath"] + data["name"] 
        full_new = data["fullpath"] + data["new"]
        os.rename(full_existing , full_new)

        return jsonify(message=f"Renamed {full_existing} to {full_new}")
    

@app.route('/delete' , methods=["DELETE"])
def delete():
    data = request.get_json()
    try:
        full_existing = data["fullpath"] + data["name"]  
        os.remove(full_existing)
        return jsonify(message=f"Deleted file {full_existing}")
    except:
        return jsonify(error=f"the file is invailid {full_existing}")
    

@app.route('/copy' , methods=["PUT"])
def copy():
    try:
        data = request.get_json()
        full_existing = data["fullpath"] + data["file"] 
        destination_path = data["endpath"]
        shutil.copy(full_existing, destination_path)
        return jsonify(message=f"{full_existing} copied to {destination_path}")
    except:
        return jsonify(error="the error has occured!")
    
@app.route('/move' , methods=["PUT"])
def move():
    try:
        data = request.get_json()
        full_existing = data["fullpath"] + data["file"] 
        destination_path = data["endpath"]
        shutil.move(full_existing, destination_path)
        return jsonify(message=f" {full_existing} moved to {destination_path} ")
    except:
        return jsonify(error="the error has occured!")
 
@app.route('/multi_del' , methods=["DELETE"])
def multi_del():
    try:
      data = request.get_json()
      for i in data["files"]:
          pathname = data["fullpath"] +  i
          shutil.rmtree(pathname)
      return jsonify(message=f"All files are deleted.")
    except Exception as e :
        print(e)
        return jsonify(error= "An error occured")

@app.route('/multi_copy' , methods=["PUT"])
def multi_copy():
    try:
        data = request.get_json()
        for i in data["files"]:
            pathname = data["fullpath"] +  i
            os.chmod(pathname, 0o666)
            shutil.copy(pathname, data["destination"])
        return jsonify(message="copyed successfully!")
    except Exception as e :
        print(e)
        return jsonify(error="An error occured!")
    
@app.route('/multi_move' , methods=["PUT"])
def multi_move():
    try:
        data = request.get_json()
        for i in data["files"]:
            pathname = data["fullpath"] +  i
            os.chmod(pathname, 0o666)
            shutil.move(pathname, data["destination"])
        return jsonify(message="moved successfully!")
    except: 
        return jsonify(error="An error occured!")
    

def MainThreadFind(args):
    root, dir_name, file_name, search = args
    
   
    result = []
    
    if search in dir_name:
        result.append({"dirname": dir_name , "root" : root  })
        
    if search in file_name:
        result.append({"filename" : file_name , "root" : root})
    
    return result 

@app.route('/search' , methods=["POST"])
def search():
    try: 
        data = request.get_json()
        search = data["searched"]
        findings = []

        
        partitions = psutil.disk_partitions()
        for i in partitions:

                
            
                for root, dirs, files in os.walk(i.mountpoint): 
                        args = [(root, dir_name, file_name , search  ) for dir_name in dirs for file_name in files ]

                        if len(findings) >= 500:
                             break
                        
                        
                        with ThreadPoolExecutor(max_workers=12) as exe:
                            results = exe.map(MainThreadFind, args)
                            
                            
                            for result in results:
                                if len(findings) >= 500:
                                    break
                                if result:
                                    findings.extend(result) 

                                    
        return jsonify(data=findings)
    except Exception as e:
        print(e)
        return jsonify(error="An error occured")

    
    
app.run(debug=True)
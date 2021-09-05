from logging import debug
from typing_extensions import Required
from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route("/")
def helloworld():
    return  "helloworld"

tasks=[
    {
        'Contact':"9987644456",
        'Name':"Raju",
        'done':False
    }
]
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        }, 400)
    task={
    'Contact':tasks[-1]['Contact']+1,
    'Name':request.json['title'],
    'done':False
    
    }
    tasks.append(task)
    return jsonify({
    "status":"success",
    "message":"task added successfully"
    })
@app.route("get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__=="__main__"):
    app.run(debug=True)
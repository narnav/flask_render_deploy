from flask import Flask,request
from flask_cors import CORS
api = Flask(__name__)
CORS(api)
myData=[{"name":"eli","age":12},{"name":"ana","age":10}]

@api.route('/')
def hello():
    return 'Hello, World!'

@api.route('/students/<del_stu>',methods=['GET','POST','DELETE','PUT'])
@api.route('/students/',methods=['GET','POST','DELETE','PUT'])
def students(del_stu=''):
    if request.method == "GET":
        return myData
    if request.method == "POST":
        request_data = request.get_json()
        name= request_data["name"]
        age= request_data["age"]

        myData.append({"name":name,"age":age})
        return myData
    if request.method == "DELETE":
        myData.remove(del_stu)
        return myData
    if request.method == "PUT":
        return myData
 
if __name__ == '__main__':
    api.run(debug=True)
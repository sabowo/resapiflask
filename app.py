from flask import Flask, request
from werkzeug.wrappers import response
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi object flask h
app = Flask(__name__)

# inisiasi object flask_restful
api = Api(app)

# inisiasi object flask_cors
CORS(app)

#inisiasi variable null type dictionary
identitas = {} #this variable global, this dictionary = json

#create class Resource
class ContohResource(Resource):
    #create method get
    def get(self):
       # response = {"msg":"this restful api"}
       # return response
       return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg": "success create data"}
        return response
#setup resource
api.add_resource(ContohResource, "/api", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)

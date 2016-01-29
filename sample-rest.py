import example

'''
pip install Flask
pip install flask-restful

quad@quad-ThinkPad-T420:~$ curl http://localhost:5000/a -d "data=vfgffbbfvbcdjbfjkdbdhjedbjhcvdjkbjkdv" -X PUT
quad@quad-ThinkPad-T420:~$ curl http://localhost:5000/b -d "data=cdjbfjkdbdhjedbjhcv2f34533433djkbjkdv" -X PUT
quad@quad-ThinkPad-T420:~$ curl http://localhost:5000/c -d "data=bhjhvjvgghbjh2cvd3cvgr32cgf442jkbjkdv" -X PUT

quad@quad-ThinkPad-T420:~$ curl http://localhost:5000/a
{"a": "vfgffbbfvbcdjbfjkdbdhjedbjhcvdjkbjkdv"}

quad@quad-ThinkPad-T420:~$ curl http://localhost:5000/b
{"b": "cdjbfjkdbdhjedbjhcv2f34533433djkbjkdv"}

quad@quad-ThinkPad-T420:~$ curl http://localhost:5000/c
{"c": "bhjhvjvgghbjh2cvd3cvgr32cgf442jkbjkdv"}

'''

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import subprocess

messages = {

	'IllegalInputRequest_DATA': {
					  'NoData': "Input data error.",
					  'status': 411,
		        	    },


	'ResourceAddedSuccessfully':  {
					  'ResourceAdded': "Resource was successfully added.",
					  'status': 412,
				      },
			 			  
	 			  
	'ResourceDoesNotExist':  {
				    'NoResource': "A resource with that ID no longer exists.",
				    'status': 404,
				 },
}

app = Flask(__name__)
api = Api(app, errors = messages)

# Files dictionary
Files = {}

# File-resource-Manager
# This class provides the methods to manipulate the resources
# as per the REST protocol
class File(Resource):

	##########################################################
	# Request parser 
	# This method parses the input request to ensure proper
	# form of the input request
	def parse_request(void):
		parser = reqparse.RequestParser()
		parser.add_argument('data', required=True)
		args = parser.parse_args(strict=True)	

	##########################################################
	# GET request
	def get(self, file_id):
		print "\n*** GET_SYS_CALL ***" ## GET
		ID   = str(file_id)
		example.mySyscall("\n ID: " + ID + "\n") ## Call C-function
		return {file_id: Files[file_id]}

	
	##########################################################
	# PUT request		
	def put(self, file_id):
		print "\n*** PUT_SYS_CALL ***" ## PUT
		ID   = str(file_id)
		Data = str(request.form['data']) 
		example.mySyscall("\n ID: " + ID + ",	Data: " + Data + "\n") ## Call C-function
		Files[file_id] = request.form['data']
		return { file_id : "Done"}, 412 

	##########################################################		
	# DELETE request	
	def delete(self, file_id):
		del Files[file_id]
		


api.add_resource(File, '/<string:file_id>')

if __name__ == '__main__':
	
	app.run()
	#app.run(debug=True)
	
	

import os.path
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import subprocess

app = Flask(__name__)
api = Api(app)

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
		
		buf = bytearray(os.path.getsize(file_id))
    		with open(str(file_id), 'rb') as f:
         		f.readinto(buf)
		resp = Response(buf, status=200, mimetype='application/octet-stream')
		print buf
		return buf

	
	##########################################################
	# PUT request		
	def post(self, file_id):
		print "\n*** PUT_SYS_CALL ***" ## PUT
		
		f = open(str(file_id), 'wb')
      		f.write(request.data)
                f.close()
                
		return { file_id : "Done"}

	##########################################################		
	# DELETE request	
	def delete(self, file_id):
		del Files[file_id]
		
api.add_resource(File, '/<string:file_id>', methods = ['GET', 'POST'])		
		
if __name__ == '__main__':
	
	app.run()
	#app.run(debug=True)

	

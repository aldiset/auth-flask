import json
from flask import Flask, request, jsonify
from flask import make_response

from app.auth.auth import token_required, login
from app.base.crud import CRUDUser
from app.database import session_manager
from flask import Response

# creates Flask object
app = Flask(__name__)


@app.route('/user', methods =['GET'])
@token_required
def get_all_users(user):
	with session_manager() as db:
		users = CRUDUser.get_users(db=db)
	return jsonify({"users":[dict(user) for user in users]})

@app.route('/me', methods = ['POST'])
@token_required
def get_me(user):
	return jsonify({"data":user.name})

@app.route('/login', methods =['POST'])
def sigin():
	return login(auth=request.form)

@app.route('/signup', methods =['POST'])
def signup():
	with session_manager() as db:
		user = CRUDUser.create(db=db, data=request.form)
		response = "Successfully registered."
		status_code = 201

		if not user:
			response = "User already exists. Please Log in."
			status_code = 202
	return Response(response=response, status=status_code)

if __name__ == "__main__":
	app.run(debug = True)

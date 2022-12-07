import jwt
from flask import request, jsonify
from functools import wraps
from flask import make_response
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash

from app.database.models.users import User
from app.config import SECRET_KEY
from app.base.crud import CRUDUser
from app.database import session_manager


# decorator for verifying the JWT
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		request.authorization
		if 'Authorization' in request.headers:
			token = request.headers['Authorization'].replace("Bearer ","")
		if not token:
			return jsonify({'message' : 'Token is missing !!'}), 401

		try:
			with session_manager() as db:
				data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256")
				current_user = CRUDUser.get_user_by_public_id(db=db, public_id=data.get("public_id"))
		except:
			return jsonify({
				'message' : 'Token is invalid !!'
			}), 401

		return f(current_user, *args, **kwargs)
	return decorated

def login(auth: dict):
	with session_manager() as db:
		user = CRUDUser.get_user_by_email(db=db, email=auth.get("email"))
		if not user:
			return make_response('Could not verify',401,{'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'})
		if check_password_hash(user.password, auth.get('password')):
			token = jwt.encode({
				'public_id': user.public_id,
				'exp' : datetime.utcnow() + timedelta(minutes = 30)
				}, SECRET_KEY)
			return make_response(jsonify({'token' : token}), 201)
    
    # returns 403 if password is wrong
	return make_response('Could not verify',403,{'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'})
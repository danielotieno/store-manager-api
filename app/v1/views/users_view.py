""" A resource for user view """
import datetime
import re
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, jwt_required)

from app.v1.models.user import User
from utlis.required import required, admin_required


class Signup(Resource):
    """
    Resource for user registering a new user
    Add Parser for required fields
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,
                        help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True,
                        help='Email cannot be blank', type=str)
    parser.add_argument('password', required=True,
                        help='Password cannot be blank', type=str)

    @jwt_required
    @admin_required
    def post(self):
        """ Method to register a user """
        args = Signup.parser.parse_args()
        username = args.get('username')
        email = args.get('email')
        password = args.get('password')

        email_format = re.compile(
            r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$)")
        username_format = re.compile(r"(^[A-Za-z]+$)")

        if not (re.match(username_format, username)):
            return {'message': 'Invalid username'}, 400
        if not (re.match(email_format, email)):
            return {'message': 'Invalid email. Ensure email is of the form example@mail.com'}, 400
        if len(username) < 4:
            return {'message': 'Username should be atleast 4 characters'}, 400
        if required(password) or required(username) or required(email):
            return {'message': 'All fields are required'}, 400
        if len(password) < 8:
            return {'message': 'Password should be atleast 8 characters'}, 400

        username_exists = User.get_user_by_username(username=args['username'])
        email_exists = User.get_user_by_email(email=args['email'])

        if username_exists or email_exists:
            return {'message': 'User already exists'}, 203

        user = User(username=args.get('username'),
                    email=args.get('email'), password=password)

        user = user.save()
        return {'message': 'registration successful, now login', 'user': user}, 201


class Login(Resource):
    """ Resource for user login """
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True,
                        help='Email field cannot be blank', type=str)
    parser.add_argument('password', required=True,
                        help='Password cannot be blank')

    def post(self):
        """ Method for registered user to login """
        args = Login.parser.parse_args()
        email = args["email"]
        password = args["password"]
        if required(email) or required(password) == '':
            return {'message': 'All fields are required'}, 400

        user = User.get_user_by_email(email)
        if not user:
            return {'message': 'User unavailable'}, 404
        if user.validate_password(password):
            expires = datetime.timedelta(minutes=30)
            token = create_access_token(
                user.to_json(), expires_delta=expires)
            return {'token': token, "message": "You are successfully logged in", 'user': user.view()}, 200
        return {"message": "Email or password is wrong."}, 401

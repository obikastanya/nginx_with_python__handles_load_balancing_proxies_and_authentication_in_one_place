import traceback
from datetime import datetime, timedelta

from flask import Blueprint, request
import jwt

api = Blueprint('public_api', __name__)
JWT_ACCESS_TOKEN_SECRET_KEY = 'supersecretkey'


@api.post('/login')
def login():
    try:
        users =[
            {
                'username':'admin',
                'role':'admin',
                'password':'123456'
            },
            {
                'username':'gues',
                'role':'gues',
                'password':'123456'
            }
        ]

        auth = request.authorization
        if not auth:
            return  {'message':'Bad Request'}, 400
        
        login_status = False

        matched_user = {}
        for user in users:
            if auth.username == user.get('username'): matched_user = user
        
        login_status = matched_user.get('username') == auth.username and matched_user.get('password') == auth.password

        if  not login_status:
            return { 'message': 'Bad Request'}, 400
        
        payload = {
            'username':matched_user.get('username'),
            'role':matched_user.get('role'),
            'iat':datetime.utcnow(),
            'exp':datetime.utcnow() + timedelta(minutes=60)
        }
        token = jwt.encode(
            payload,
            JWT_ACCESS_TOKEN_SECRET_KEY,
            algorithm='HS256'
        )
        return {
            'token':token,
            'message':'OK'
        }, 200
    except:
        traceback.print_exc()
        return { 'message' : 'Internal Server Error'}, 500
        

@api.post('/logout')
def logout():
    # Implement token revocation
    ...
    return {
        'message':'Success'
    }, 200


@api.get('/permissions')
def get_permissions():
    role_permissions = [
        {
            'role':'admin',
            'permissions':[
                'product:view',
                'product:update',
                'product:delete',
                'product:create'
            ]
        },
        {
            'role':'gues',
            'permissions':[]
        }
    ]
    role = request.args.get('role')
    
    if not role:
        return {
            'message':'Bad Request',
            'data':[]
        }, 400

    matched_role = {}
    for record in role_permissions: 
        if record.get('role') == role: matched_role = record

    
    if not matched_role:
        return {
            'message':'Not Found',
            'data':[]
        }, 400
    
    return {
        'data':matched_role.get('permissions'),
        'message':'OK'
    }, 200


@api.get('/token/info')
def get_token_info():

    jwt_access_token = request.args.get('access_token')
    if not jwt_access_token:
        return { 'message': 'Bad Request'}, 400
    
    try:
        payload = jwt.decode(
            jwt_access_token,
            JWT_ACCESS_TOKEN_SECRET_KEY,
            algorithms = ['HS256'],
            verify = True
        )
        return { 'message': 'OK', 'data': payload }, 200
    except jwt.exceptions.ExpiredSignatureError:
        return { 'message': 'Bad Request'}, 400
    except jwt.exceptions.InvalidTokenError:
        return { 'message' : 'Bad Request'}, 400
    except:
        traceback.print_exc()
        return { 'message' : 'Internal Server Error'}, 500
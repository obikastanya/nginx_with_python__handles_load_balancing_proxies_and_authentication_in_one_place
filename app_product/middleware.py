import traceback
from functools import wraps

from flask import request
import requests as http_request



def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        auth = request.authorization
        if not auth: return {'message':'Unauthorized'}, 401
        
        jwt_access_token = auth.token
        if not jwt_access_token: return {'message':'Unauthorized'}, 401
        
        try:
            resp = http_request.get('http://host.docker.internal:8881/public/auth/token/info',{'access_token':jwt_access_token})
            _resp = resp.json()

            if resp.status_code != 200:
                return _resp
            
            request.x_auth_user = _resp.get('data', {}).get('username')
            request.x_auth_role = _resp.get('data', {}).get('role')
            
            return func(*args, **kwargs)
        except:
            traceback.print_exc()
            return {'message':'Internal Server Error'}, 500
    return wrapper

def require_permission(required_permission: None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            role = request.x_auth_role
            if not role:
                return {'message':'Forbidden'}, 403
            
            try:
                resp = http_request.get('http://host.docker.internal:8881/public/auth/permissions',{'role':role})
                _resp = resp.json()

                permissions = _resp.get('data',[])    
                if required_permission in permissions:
                    return func(*args, **kwargs)
            except:
                traceback.print_exc()
                return {'message':'Internal Server Error'}, 500

            return {'message':'Forbidden'}, 403

        return wrapper
    return decorator
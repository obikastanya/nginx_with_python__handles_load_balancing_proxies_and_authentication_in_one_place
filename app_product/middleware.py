import traceback
from functools import wraps

from flask import request
import requests as http_request



def require_permission(required_permission: None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            role = role = request.headers.get('X-Auth-Role')
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
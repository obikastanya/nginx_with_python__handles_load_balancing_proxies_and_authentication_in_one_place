import os

from flask import Blueprint

api = Blueprint('public_api', __name__)
HOST_NAME = os.environ.get('HOST_NAME')

@api.get('/all')
def public_get_product():
    return {
        'data':[
            
            {
                'id': '7',
                'title': 'iPhone 9',
                'description': 'An apple mobile which is nothing like apple'
            },
            {
                'id': '8',
                'title': 'Microsoft Surface Laptop 4',
                'description': 'Style and speed. Stand out on ...'
            },
            {
                'id': '9',
                'title': 'Infinix INBOOK',
                'description': 'Infinix Inbook X1 Ci3 10th 8GB...'
}
        ],
         'source':HOST_NAME
    }, 200
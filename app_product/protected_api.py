import os

from flask import Blueprint

from middleware import require_permission

api = Blueprint('protected_api', __name__)
HOST_NAME = os.environ.get('HOST_NAME')


@api.get('/<product_id>/')
@require_permission('product:view')
def get_product(product_id):
    products = [
         {
            'id': '9',
            'title': 'Infinix INBOOK',
            'description': 'Infinix Inbook X1 Ci3 10th 8GB...',
            'price': 1099,
            'discountPercentage': 11.83,
            'rating': 4.54,
            'stock': 96,
            'brand': 'Infinix',
            'category': 'laptops',
            'thumbnail': 'https://i.dummyjson.com/data/products/9/thumbnail.jpg',
            'images': [
                'https://i.dummyjson.com/data/products/9/1.jpg',
                'https://i.dummyjson.com/data/products/9/2.png',
                'https://i.dummyjson.com/data/products/9/3.png',
                'https://i.dummyjson.com/data/products/9/4.jpg',
                'https://i.dummyjson.com/data/products/9/thumbnail.jpg'
            ]
        },
        {
            'id': '10',
            'title': 'HP Pavilion 15-DK1056WM',
            'description': 'HP Pavilion 15-DK1056WM Gaming...',
            'price': 1099,
            'discountPercentage': 6.18,
            'rating': 4.43,
            'stock': 89,
            'brand': 'HP Pavilion',
            'category': 'laptops',
            'thumbnail': 'https://i.dummyjson.com/data/products/10/thumbnail.jpeg',
            'images': [
                'https://i.dummyjson.com/data/products/10/1.jpg',
                'https://i.dummyjson.com/data/products/10/2.jpg',
                'https://i.dummyjson.com/data/products/10/3.jpg',
                'https://i.dummyjson.com/data/products/10/thumbnail.jpeg'
            ]
        },
    ]
    
    matched_product ={}
    for product in products:
        if product.get('id') == product_id: matched_product = product
    
    if not matched_product:
        return {
            'message': 'Not Found',
            'data':{},
             'source':HOST_NAME
        }, 404
    
    return {
        'message':'OK',
        'data':matched_product,
        'source':HOST_NAME
    }, 200 
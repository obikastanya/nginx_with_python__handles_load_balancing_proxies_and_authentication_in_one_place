from flask import Flask

from protected_api import api as protected_api
from public_api import api as public_api

app = Flask(__name__)
app.register_blueprint(public_api, url_prefix='/public/product')
app.register_blueprint(protected_api, url_prefix='/protected/product')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
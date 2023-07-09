
from flask import Flask

from public_api import api as public_api

app = Flask(__name__)
app.register_blueprint(public_api, url_prefix='/public/auth')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
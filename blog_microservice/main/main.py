from flask import Flask, jsonify, abort, render_template
import os
import requests
import json
from flask_cors import CORS


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )
CORS(app)

@app.route('/', methods=['GET'])
def home():
    try:
        data = requests.get('http://172.17.0.1:8000/api/blogs/')
        data = data.json()
        print(data)
        return render_template('index.html', blogs=data)
    except requests.exceptions.ConnectionError:
        return ('Connection refused')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
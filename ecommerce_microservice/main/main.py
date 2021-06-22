from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    product_id: int
    name: str
    image: str
    price: int
    num_sold: int
    quantity_available: int
    rating: int
    discount: bool

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(200))
    image = db.Column(db.String(200))
    price = db.Column(db.Integer)
    quantity_available = db.Column(db.Integer)
    num_sold = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    discount = db.Column(db.Boolean)


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://172.17.0.1:8000/api/user')
    json = req.json()

    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
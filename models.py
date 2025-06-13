from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(50))
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=False)
    cost_price = db.Column(db.Float)
    added_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Product {self.name}>'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Customer {self.name}>'

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    quantity = db.Column(db.Integer, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float)

    product = db.relationship('Product', backref='sales')
    customer = db.relationship('Customer', backref='purchases')

    def __repr__(self):
        return f'<Sale {self.id}>'


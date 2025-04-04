from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#main application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#database object
db = SQLAlchemy(app)

#associate table
customer_product = db.Table(
    "customer_product",
    db.Column("customer_id", db.Integer, db.ForeignKey("customers.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"))
)
#customer class
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    items = db.relationship('Product',backref='owners', secondary=customer_product)
    
    def __repr__(self):
        return f'Customer({self.name}, {self.email})'
        
#product class
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Product({self.name}, {self.price})'


#server run
if __name__ == '__main__':
    app.run(debug=True)
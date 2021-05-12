from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.242.189.33:3306/instance' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string, nullable = False)
    product = db.relationship('product', backref='product') 

class products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')
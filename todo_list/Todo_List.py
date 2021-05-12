from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.123.240:3306/instance' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object
@app.route('/')
@app.route('/home')
def home():
    return 'This is a to do list!'
@app.route('/todolist')
def todolist():
    
    return str(todo)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Task= db.Column(db.String(30), nullable=False)
    Complete = db.Column(db.Boolean, nullable=False)
'''
class details():
    Steps = db.column(db.integer)
'''
if __name__=='__main__':
    app.run(debug=True)

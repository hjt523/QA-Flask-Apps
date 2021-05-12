from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object
@app.route('/')
def index():
    all_todo = todo.query.all()
    todos_string = ''
    return all_todo
@app.route('/home')
def home():
    return 'This is a to do list!'
@app.route('/todolist')
def todolist():
    
    return str(todo)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Task= db.Column(db.String(30), nullable=False)
    Complete = db.Column(db.Boolean, nullable=False, default=False)

@app.route("/add")
def add():
    new_todo = todo( Task = " New Todo")
    db.session.add(new_todo)
    db.session.commit()
    return " New task added"

@app.route("/complete/<int:todoid>")
def complete(todoid):
    todos = todo.query.get(todoid)
    todos.complete = True
    db.session.commit()
    return " Task Completed"
@app.route("/delete/<int:todoid>")
def delete(todoid):
    todel = todo.query.get(todoid)
    db.session.delete(todel)
    db.session.commit()
    return (" Task  Deleted ")
'''
class details():
    Steps = db.column(db.integer)
'''
if __name__=='__main__':
    app.run(debug=True)

from flask import Flask, redirect, render_template, request,url_for # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'edfghjkl'

db = SQLAlchemy(app) # create SQLALchemy object

@app.route('/')
def index():
    
    form = nameadd()
    """
    if form.validate_on_submit():
        ntask = todo(Task=form.name.data)
        db.session.add(ntask)
        db.session.commit()
        """
    tasks = todo.query.all()
    return render_template("index.html",tasks = tasks, form=form)

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

class nameadd(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')



@app.route("/add",methods=['GET',"POST"])
def add():
    error = ""
    form = nameadd()

    if request.method == "POST":
        Task = form.name.data
        if len(Task) == 0 :
            error = "Please supply a task"
        else:
            ntask = todo(Task=Task, Complete = False)
            db.session.add(ntask)
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('add.html', form=form, message=error)
@app.route("/update/<int:todoid>",methods=['GET',"POST"])
def update(todoid):
    error = ""
    form = nameadd()
    entry = todo.query.get(todoid)
    if request.method == "POST":
        Task = form.name.data
        if len(Task) == 0 :
            error = "Please supply a task"
        else:
            entry.Task = Task
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('update.html', form=form, message=error)


@app.route("/complete/<int:todoid>")
def complete(todoid):
    todos = todo.query.get(todoid)
    todos.Complete = True
    db.session.commit()
   
    return  redirect(url_for('index'))
@app.route("/incomplete/<int:todoid>")
def incomplete(todoid):
    todos = todo.query.get(todoid)
    todos.Complete = False
    db.session.commit()
   
    return  redirect(url_for('index'))
@app.route("/delete/<int:todoid>")
def delete(todoid):
    todel = todo.query.get(todoid)
    db.session.delete(todel)
    db.session.commit()
    
    return redirect( url_for('index'))
'''
class details():
    Steps = db.column(db.integer)
'''
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

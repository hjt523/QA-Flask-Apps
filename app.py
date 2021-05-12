from flask import Flask

app = Flask(__name__)
'''
app.config["SQL"]


'''

@app.route('/')
@app.route('/home')
def home():
    return 'Hello World!'
@app.route('/numwang/<int:number>')
def numwang(number):
    number = number**2
    number = str(number) + "? Thats Numberwang!"
    return number

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Nichelle Columba! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/signin')
def signin():  # put application's code here
    return render_template('signin.html')

@app.route('/signup1')
def signup1():  # put application's code here
    return render_template('signup1.html')

@app.route('/signup2')
def signup2():  # put application's code here
    return render_template('signup2.html')

@app.route('/changepassword')
def changepassword():  # put application's code here
    return render_template('changepassword.html')

if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask(__name__)


#@ signifies a decoator - way to wrapa function and modifying its behaviour
@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/luna')
def luna():
    return '<h2>This is luna home page.</h2>'


@app.route('/profile/<username>')
def profile(username):
    return "<h3>Hey there %s</h3>" % username

@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h3>Post Id is %s</h3>" % post_id



if __name__ == "__main__":
    app.run(debug=True)

#### when you run this code , browse below http://127.0.0.1:5000 on browser
"""
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
"""

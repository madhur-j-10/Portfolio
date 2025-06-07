

from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/rough')
# def rough():
#     return render_template('rough.html')

@app.route('/about-me')
def about():
    return render_template('about.html')

@app.route('/rock-paper-scissors')
def rps():
    return render_template('rock-paper-scissors.html')

@app.route('/to-do-list')
def todolist():
    return render_template('to-do-list.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)
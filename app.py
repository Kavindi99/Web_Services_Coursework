# pip install Flask

# python --version

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Web Services Coursework</h1>'

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=80) 





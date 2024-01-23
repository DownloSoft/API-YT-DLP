# app.py
from flask import Flask
from api.ytvideo import ytvideo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello, this is the home route!"

app.register_blueprint(ytvideo)

if __name__ == '__main__':
    app.run(debug=False)

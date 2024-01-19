# app.py
from flask import Flask
from api.ytVideo import ytvideo

app = Flask(__name__)

app.register_blueprint(ytvideo)

if __name__ == '__main__':
    app.run(debug=True)

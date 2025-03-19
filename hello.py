from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    print("Starting server at http://0.0.0.0:8080")
    serve(app, host='0.0.0.0', port=8080)

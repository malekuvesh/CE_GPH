from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    from waitress import serve
    print("Starting server at http://0.0.0.0:8080")
    serve(app, host='0.0.0.0', port=8080)

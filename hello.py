import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.debug("Hello route has been hit")
    return "Hello, World!"

if __name__ == "__main__":
    from waitress import serve
    app.logger.debug("Starting server")
    serve(app, host='0.0.0.0', port=8080)

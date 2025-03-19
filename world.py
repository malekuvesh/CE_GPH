from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Define a simple route
@app.route('/')
def hello():
    return "Hello, World!"

# Run the application using waitress
if __name__ == "__main__":
    from waitress import serve
    print("Starting server at http://0.0.0.0:8080")  # Print the server URL
    serve(app, host='0.0.0.0', port=8080)

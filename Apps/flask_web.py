from flask import Flask, jsonify

app = Flask(__name__)  # creating the flask app


@app.route('/')  # First default route
def index():
    return jsonify({'hi': 'alex'})  # hi alex presented on the page


@app.route('/my-endpoint')  # second route
def endpoint():
    return 'hello world'  # hello world presented on the page


if __name__ == '__main__':
    app.run()


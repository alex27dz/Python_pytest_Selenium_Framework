from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run()
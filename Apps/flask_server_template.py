from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)  # Flask setup
# CORS(app)
'''
# test connection function
@app.route("/", methods=["POST", "GET"])
def home():
    return "test"

# function under /address tag operating only after POST or GET requests configured, the /address function is waiting for POST request from front end
@app.route('/address', methods=["POST", "GET"])
def address():
    # creating dictionary to fill in the params from POST request
    flask_addr = {
        'street': '',
        'city': '',
        'short_state': '',
        'state': ''
    }
    if request.method == "POST":
        print('Address automation was activated :)')
        print('The input parameters are: {}'.format(request.json))  # request params in json
        # converting params
        flask_addr['street'] = request.json.get('street')
        flask_addr['city'] = request.json.get('city')
        flask_addr['short_state'] = request.json.get('short_state')
        flask_addr['state'] = request.json.get('state')
        # running the run file function using params from Front converting to json format
        # datalist = address_data_automate_tool(flask_addr['street'], flask_addr['city'], flask_addr['short_state'], flask_addr['state'], 'Dani')
        # converting the data_list list into beautiful string the string representing all dicts in the list and print the back same as on console
        datalist = ['alex', 'dezho']
        data2json = json.dumps(datalist, indent=4, separators=(". ", " = "))
        print('Results type: {}'.format(type(data2json)))
        print('Results: \n {}'.format(data2json))  # printing the results
        return data2json  # return all dictionaries in one list in jason format, printed on home page
    else:
        return 'alex'

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'input1': request.form.get('input1'),
            'input2': request.form.get('input2'),
            'input3': request.form.get('input3'),
            'input4': request.form.get('input4')
        }
        print(data)
        print(type(data))
        print(type(jsonify(data)))
        return jsonify(data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify

app = Flask(__name__)

# This will store the string received from the POST request
data_store = {"data": None}

@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    data_store["data"] = data.get('data', None)
    return jsonify({"message": "Data stored successfully"}), 200

@app.route('/receive', methods=['GET'])
def receive_data():
    is_data_present = data_store["data"] is not None
    return jsonify({"data_present": is_data_present
    ,"data": data_store}), 200

if __name__ == '__main__':
    app.run(debug=True)
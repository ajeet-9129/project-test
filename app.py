from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, Flask!")

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(received=data)

if __name__ == '__main__':
    app.run(debug=False windows)

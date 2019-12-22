from flask import Flask

app = Flask(__name__)

@app.route('/json', methods=['POST', 'GET'])
def test_json():
    return '{"code": 1, "message": "Hello, World!" }'
   
# Run in HTTP
if __name__ == "__main__":
    # Only for debugging while developing
	app.run(host='0.0.0.0', debug=True, port='5000')  
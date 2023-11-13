from flask import Flask, jsonify
from flask_cors import CORS
from datavisweek3api import get_graph

app = Flask(__name__)
CORS(app)
@app.route('/api/data', methods=['GET'])
def get_data():
    print("Fetched Data!")
    img_path = get_graph()
    return jsonify({'img_path': str(img_path)})

if __name__ == "__main__":
    app.run(port = 5000)
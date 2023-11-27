from flask import Flask, jsonify
from flask_cors import CORS
from datavisweek3json import get_graph

app = Flask(__name__)
CORS(app)
print(get_graph())
@app.route('/api/data', methods=['GET'])
def get_data():
    # 
    # Your Flask API logic here
    # return {'data': 'Hello from Flask!'}
    
    print("Fetched Data!")
    img_path = get_graph()
    return jsonify({'img_path': img_path})
    # return {"message": "hello"}

if __name__ == "__main__":
    app.run(port = 5000)
from flask import Flask, jsonify
from flask_cors import CORS
from datavisweek3api import get_graph
from mockChargeRate import fake_num

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
    dummy = fake_num()
    return jsonify({'img_path': img_path}, {'dummy': dummy})
    # return {"message": "hello"}

if __name__ == "__main__":
    app.run(port = 5000)
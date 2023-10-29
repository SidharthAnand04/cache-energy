from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Your Flask API logic here
    # return {'data': 'Hello from Flask!'}
    print("Fetched Data!")
    return {"message": "hello"}

if __name__ == "__main__":
    app.run(port = 5000)
from flask import Flask, jsonify, request
from randomforestchargeratetest import prediction
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Your existing code...

@app.route('/api/predict', methods=['POST'])
@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def predict_endpoint():
    if request.method == 'OPTIONS':
        # Handle OPTIONS request (preflight check)
        response = app.make_default_options_response()
    else:
        try:
            # Extract features from the JSON request
            features = request.json.get('features', [])

            # Call your existing prediction function
            prediction_result = prediction(*features)
            print("Fetched Data!")
            #Convert NumPy array to Python list
            prediction_result_list = prediction_result.tolist()

            # Return the result as JSON
            response = jsonify({'prediction': prediction_result_list})

        except Exception as e:
            # Log the exception details
            print(f"Exception: {str(e)}")
            # Return a JSON response with the error message
            response = jsonify({'error': str(e)})
            response.status_code = 500

    # Add CORS headers to the response
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')

    return response

if __name__ == '__main__':
     app.run(port = 5000)

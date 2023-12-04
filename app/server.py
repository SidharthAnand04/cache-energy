from flask import Flask, jsonify
from flask_cors import CORS
from datavisweek3api import get_graph
from final_interval_charge_rate import fig1, fig2, fig3, fig4, fig_TvE



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
    path_fig1 = fig1()
    path_fig2 = fig2()
    path_fig3 = fig3()
    path_fig4 = fig4()
    path_figTvE = fig_TvE()
    return jsonify({'img_path': img_path}, {'fig1_path' : path_fig1}, {'fig2_path' : path_fig2}, {'fig3_path' : path_fig3}, {'fig4_path' : path_fig4}, {'figTvE_path' : path_figTvE})
    # return {"message": "hello"}

if __name__ == "__main__":
    app.run(port = 5000)
# server.py
from blood_calculator import check_HDL
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/", methods =["GET"])
def status():
    return "Server On"

@app.route("/hdl_check", methods = ["POST"])
def check_HDL_from_internet():
    """
    input_jason = {"name": <patient_name_string>,
                   "hdl_result": <hdl_int>}
    """
    in_data = request.get_json()
    hdl_value = in_data["hdl_result"]
    answer = check_HDL(hdl_value)
    return answer

@app.route("/add", methods =["POST"])
def add():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    answer_json = [in_data["a"], in_data["b"], answer]
    return jsonify(answer_json)


if __name__ == '__main__':
    app.run()


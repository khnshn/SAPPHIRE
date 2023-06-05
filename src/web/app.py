from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import simulate as sim_web
import numpy as np
from io import BytesIO
import joblib

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    params = [
        (item[0].replace("_", " ").strip(), str(item[1]), type(item[1]).__name__)
        for item in sim_web.get_simulation_params()
        if item[0].startswith("_")
    ]
    return render_template("index.html", params=params)


@app.route("/simulate", methods=["POST"])
def simulate():
    if request.args.get("type") == "default":
        return jsonify(sim_web.simulate_get_data()), 200
    elif request.args.get("type") == "custom":
        params = [(x, request.args.get(x)) for x in request.args]
        params.remove(params[0])  # to remove type=custom; irrelevant for the simulator
        upload_data = {}
        for file in request.files:
            if request.files[file].filename.endswith(".csv"):
                contents = BytesIO(request.files[file].read())
                data = np.genfromtxt(contents, delimiter=",")
                upload_data[file] = data
            elif request.files[file].filename.endswith(".joblib"):
                contents = BytesIO(request.files[file].read())
                clf = joblib.load(contents)
            else:
                return "Unknown simulation type", 400
            print(params)
        return jsonify(sim_web.simulate_custom_get_data(params)), 200
    return "Unknown simulation type", 400

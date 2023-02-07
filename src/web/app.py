from flask import Flask
from flask import render_template
from flask import request
import simulate as sim_web

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    params = [
        str(item[0]).replace("_", " ").strip()
        for item in sim_web.get_simulation_params()
    ]
    return render_template("index.html", params=params)


@app.route("/simulate", methods=["POST"])
def simulate():
    if request.args.get("type") == "default":
        return str(sim_web.simulate_base64()), 200
    return "Unknown simulation type", 400

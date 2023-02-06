from flask import Flask
from flask import render_template
from flask import request
import simulate as sim_web

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/simulate", methods=["POST"])
def simulate():
    if request.args.get("type") == "default":
        return str(sim_web.simulate_base64()), 200
    return "Unknown simulation type", 400

from flask import Flask
from flask import  request
from flask import jsonify
from utils import models
import time
from utils.models import MyJSONEncoder

app= Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route("/health_result")
def get_health_result():
    dt=time.strftime("%Y-%m-%d %X")
    UnitNo=request.values.get("UnitNo")
    lineNo=request.values.get("lineNo")
    trainNo=request.values.get("trainNo")
    cv=models.result_rule(UnitNo,dt,lineNo,trainNo)
    return jsonify({"cv_value":cv})



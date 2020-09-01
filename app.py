from flask import Flask
from flask import  request
from flask import jsonify
import time
from Utils.Models.rule_base import MyJSONEncoder
from Utils.Models.health_score import health_result_score
import os

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
    root_path=os.path.join(os.getcwd(),'Utils','Models')
    path_list=[os.path.join(root_path,path) for path in ['model_df_train_M1.pkl','model_df_train_M2.pkl','model_df_train_MP1.pkl','model_df_train_MP2.pkl','model_df_train_TC1.pkl']]
    score=health_result_score(dt,UnitNo,lineNo,trainNo,path_list)
    return jsonify({"cv_value":score})



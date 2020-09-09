from Utils.gmm_hs import gmm_cv_score,GMM_HS
from Utils.rule_base import rule_score
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import datetime
import time
from Utils.rule_base import MyJSONEncoder
import os


def health_result_score(dt,UnitNo,lineNo,trainNo,model_path,CarrageNo='M1',roll_step=30,use_rule=False):
    score=0.0
    if use_rule:
        score=rule_score(UnitNo,dt,lineNo,trainNo)
    
    else:
        score=gmm_cv_score(dt,UnitNo,lineNo,trainNo,model_path,CarrageNo)[0]  
    return score





app= Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/health_result/')
def health_score():
    dt="2020-9-9 10:10:00"
    root_path=os.path.join(os.getcwd(),'Utils','Models')
    model_path=os.path.join(root_path,'model_df_train_M1.pkl')
    score=health_result_score(dt,"1#","5L","534",model_path)
    return jsonify({"cv_value":score})
















if __name__ == "__main__":
    app.run()
    # import argparse
    # import datetime
    # import os
    # dt= datetime.datetime.now()
    # dt_str = datetime.datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')

    # parser=argparse.ArgumentParser(description='Train Health AssessMent')
    # parser.add_argument('--UnitNo',type=str,default='1#',help='Air Condition Unit Number',choices=['1#','2#'])
    # parser.add_argument('--lineNo',type=str,default='5L',help='Subway Line Number')
    # parser.add_argument('--trainNo',type=str,default='534',help='Subway Train Number')
    # args = parser.parse_args()

    # root_path=os.path.join(os.getcwd(),'Utils','Models')
    # model_path=os.path.join(root_path,'model_df_train_M1.pkl')
    # res=health_result_score(dt_str,args.UnitNo,args.lineNo,args.trainNo,model_path,use_rule=False)
    # print('{:*^30}'.format('健康评估分数'))  # 使用“*”填充
    # print("score:",res)
    # print()
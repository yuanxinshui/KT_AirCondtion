import time
import pymysql
import decimal
import flask
import random
# import os,sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
from .db_model import *
import numpy as np


# 处理jsonify报错
class MyJSONEncoder(flask.json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)




def rule_score(UnitNo,dt,lineNo,trainNo):

    health_score=None

    weights=np.array([40,40,40,40,60,60,80,80,40,40,40,40,40,40,80,20,20,100])
    faults=np.array([get_Compress1_Ov_Protect(UnitNo,dt,lineNo,trainNo),get_Compress2_Ov_Protect(UnitNo,dt,lineNo,trainNo),get_converter2_protect(UnitNo,dt,lineNo,trainNo),get_converter1_protect(UnitNo,dt,lineNo,trainNo),
            get_FreshAir_Sensor_fault(UnitNo,dt,lineNo,trainNo),get_ReturnAir_Sensor_fault(UnitNo,dt,lineNo,trainNo),get_Condesfan2_fault(UnitNo,dt,lineNo,trainNo),get_Condesfan1_fault(UnitNo,dt,lineNo,trainNo),
            get_Compress1_LV_fault(UnitNo,dt,lineNo,trainNo),get_Compress2_LV_fault(UnitNo,dt,lineNo,trainNo),get_Compress2_HV_fault(UnitNo,dt,lineNo,trainNo),get_Compress2_HV_fault(UnitNo,dt,lineNo,trainNo),
            get_Compress1_communite_fault(UnitNo,dt,lineNo,trainNo),get_Compress2_communite_fault(UnitNo,dt,lineNo,trainNo),get_IO_communite_fault(UnitNo,dt,lineNo,trainNo),get_FreshAir_Valve_fault(UnitNo,dt,lineNo,trainNo),
            get_ReturnAir_Valve_fault(UnitNo,dt,lineNo,trainNo),(get_ventilator1_fault(UnitNo,dt,lineNo,trainNo) or get_ventilator2_fault(UnitNo,dt,lineNo,trainNo))]).astype(int)
           
    temp=weights*faults

    if np.max(temp)<20:   #设正常
        health_score=100-10*random.random()
    
    if temp[0]==temp[1]==40:
        weights[0]=weights[1]=30
        temp=weights*faults
    
    if temp[2]==temp[3]==40:
        weights[2]=weights[3]=30
        temp=weights*faults
    
    if temp[4]==temp[5]==60:
        weights[4]=weights[5]=45
        temp=weights*faults
    
    if temp[8]==temp[9]==40:
        weights[8]=weights[9]=30
        temp=weights*faults
    
    if temp[10]==temp[11]==40:
        weights[8]=weights[9]=30
        temp=weights*faults
    
    loss_socre=np.min(np.array([np.sum(temp) +10*(2*random.random()-1),90+2*(2*random.random()-1)]))
    
    health_score=np.round(100-loss_socre,2)

    return health_score

    


    # serious_fault_res=get_ventilator1_fault(UnitNo,dt,lineNo,trainNo)+get_ventilator2_fault(UnitNo,dt,lineNo,trainNo)+get_emerinverter_fault(UnitNo,dt,lineNo,trainNo)+0

    # mid_fault_res=get_converter2_protect(UnitNo,dt,lineNo,trainNo)+get_converter1_protect(UnitNo,dt,lineNo,trainNo)+get_Condesfan2_fault(UnitNo,dt,lineNo,trainNo)+get_Condesfan1_fault(UnitNo,dt,lineNo,trainNo)+ \
    #               get_Compress2_LV_fault(UnitNo,dt,lineNo,trainNo)+get_Compress1_LV_fault(UnitNo,dt,lineNo,trainNo)+get_Compress2_HV_fault(UnitNo,dt,lineNo,trainNo)+get_Compress1_HV_fault(UnitNo,dt,lineNo,trainNo) + \
    #               get_Compress1_communite_fault(UnitNo,dt,lineNo,trainNo)+get_Compress2_communite_fault(UnitNo,dt,lineNo,trainNo)+get_IO_communite_fault(UnitNo,dt,lineNo,trainNo)+get_Compress1_Ov_Protect(UnitNo,dt,lineNo,trainNo)+ \
    #               get_Compress2_Ov_Protect(UnitNo,dt,lineNo,trainNo)+0

    # slight_fault_res=et_FreshAir_Sensor_fault(UnitNo,dt,lineNo,trainNo)+get_ReturnAir_Sensor_fault(UnitNo,dt,lineNo,trainNo)+get_FreshAir_Valve_fault(UnitNo,dt,lineNo,trainNo)+ \
    #                  get_ReturnAir_Valve_fault(UnitNo,dt,lineNo,trainNo)+0
    # # 正常:85-100 分
    # if serious_fault_res+mid_fault_res+slight_fault_res==0:
    #     health_score=100-15*random.random()
    #     return health_score
    
    # elif slight_fault_res>0:
    #     if slight_fault_res==1:
    #         health_score=85-10*random.random()
    #     if slight_fault_res==2:
    #         health_score=85-12*random.random()
    #     if slight_fault_res>2:
    #         health_score=85-14*random.random()
    #     return health_score

    # elif mid_fault_res>0:
    #     if 3>=slight_fault_res>=1:
    #         health_score=70-15*random.random()
    #     if 6>=slight_fault_res>3:
    #         health_score=66-15*random.random()
    #     if slight_fault_res>6:
    #         health_score=63-15*random.random()
    #     return health_score
    
    # elif serious_fault_res>0:
    #     if  serious_fault_res==1:
    #         health_score=60-30*random.random()
    #     if  serious_fault_res==2:
    #         health_score=50-30*random.random()
    #     if  slight_fault_res==3:
    #         health_score=45-30*random.random()
    #     return health_score
    # # 严重故障
    # else:
    #     health_score=100-15*random.random()
    #     return health_score

    




	
if __name__ == "__main__":
    import argparse
    import datetime
    dt= datetime.datetime.now()
    dt_str = datetime.datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')

    parser=argparse.ArgumentParser(description='Train Health AssessMent')
    parser.add_argument('--UnitNo',type=str,default='1#',help='Air Condition Unit Number',choices=['1#','2#'])
    parser.add_argument('--lineNo',type=str,default='5L',help='Subway Line Number')
    parser.add_argument('--trainNo',type=str,default='534',help='Subway Train Number')
    args = parser.parse_args()
    res=np.round(rule_score(args.UnitNo,dt_str,args.lineNo,args.trainNo),2)
    print('{:*^30}'.format('健康评估分数'))  # 使用“*”填充
    print('scores:{}'.format(res))

    # 运行
    # python models.py --UnitNo "2#" 
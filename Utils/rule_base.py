import time
import pymysql
import decimal
import flask
import random
import db_model


# 处理jsonify报错
class MyJSONEncoder(flask.json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)




def rule_score(UnitNo,dt,lineNo,trainNo):
    health_score=None
    serious_fault_res=db_model.get_ventilator1_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_ventilator2_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_emerinverter_fault(UnitNo,dt,lineNo,trainNo)+0

    mid_fault_res=db_model.get_converter2_protect(UnitNo,dt,lineNo,trainNo)+db_model.get_converter1_protect(UnitNo,dt,lineNo,trainNo)+db_model.get_Condesfan2_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_Condesfan1_fault(UnitNo,dt,lineNo,trainNo)+ \
                  db_model.get_Compress2_LV_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_Compress1_LV_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_Compress2_HV_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_Compress1_HV_fault(UnitNo,dt,lineNo,trainNo) + \
                  db_model.get_Compress1_communite_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_Compress2_communite_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_IO_communite_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_Compress1_Ov_Protect(UnitNo,dt,lineNo,trainNo)+ \
                  db_model.get_Compress2_Ov_Protect(UnitNo,dt,lineNo,trainNo)+0

    slight_fault_res=db_model.et_FreshAir_Sensor_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_ReturnAir_Sensor_fault(UnitNo,dt,lineNo,trainNo)+db_model.get_FreshAir_Valve_fault(UnitNo,dt,lineNo,trainNo)+ \
                     db_model.get_ReturnAir_Valve_fault(UnitNo,dt,lineNo,trainNo)+0
    # 正常:85-100 分
    if serious_fault_res+mid_fault_res+slight_fault_res==0:
        health_score=100-15*random.random()
        return health_score
    
    elif slight_fault_res>0:
        if slight_fault_res==1:
            health_score=85-10*random.random()
        if slight_fault_res==2:
            health_score=85-12*random.random()
        if slight_fault_res>2:
            health_score=85-14*random.random()
        return health_score

    elif mid_fault_res>0:
        if 3>=slight_fault_res>=1:
            health_score=70-15*random.random()
        if 6>=slight_fault_res>3:
            health_score=66-15*random.random()
        if slight_fault_res>6:
            health_score=63-15*random.random()
        return health_score
    
    elif serious_fault_res>0:
        if  serious_fault_res==1:
            health_score=60-30*random.random()
        if  serious_fault_res==2:
            health_score=50-30*random.random()
        if  slight_fault_res==3:
            health_score=45-30*random.random()
        return health_score
    # 严重故障
    else:
        health_score=100-15*random.random()
        return health_score

    




	
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
    res=rule_score(args.UnitNo,dt_str,args.lineNo,args.trainNo)
    print('{:*^30}'.format('健康评估分数'))  # 使用“*”填充

    print()

    # 运行
    # python models.py --UnitNo "2#" 
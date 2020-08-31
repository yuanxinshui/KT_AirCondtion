import time
import pymysql
import decimal
import flask
import random
from db_model import query


# 处理jsonify报错
class MyJSONEncoder(flask.json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)

def get_time():
    time_str =  time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

###########################严重故障################################
def get_ventilator2_fault(UnitNo,dt,lineNo,trainNo):
    """
    严重故障:1机组通风机2故障
    """
    sql="select Interfan2_Internalthermal_Protect,InterFan2_ContactorFD_Fault,InterFan2_ContactorLock_Alarm from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_ventilator1_fault(UnitNo,dt,lineNo,trainNo):
    """
    严重故障:1机组通风机1故障
    """
    sql="select Interfan1_Internalthermal_Protect,InterFan1_ContactorFD_Fault,InterFan1_ContactorLock_Alarm from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_emerinverter_fault(UnitNo,dt,lineNo,trainNo):
    """
    严重故障:紧急逆变器故障
    """
    sql="select EmergencyInverter_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

###########################中等故障################################
def get_converter2_protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组压缩机2变频器保护，一般系统有通风无制冷
    """
    sql="select Sys2_Inverter_HTemperlock,Sys2_Inverter_HVollock,Sys2_Inverter_LVollock,Sys2_Inverter_MissPhasslock,Sys2_Inverter_OtherFaultlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_converter1_protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组压缩机1变频器保护，一般系统有通风无制冷
    """
    sql="select Sys1_Inverter_HTemperlock,Sys1_Inverter_HVollock,Sys1_Inverter_LVollock,Sys1_Inverter_MissPhasslock,Sys1_Inverter_OtherFaultlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])


def get_Condesfan2_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组冷凝风机2故障
    """
    sql="select Outerfan2_Internalthermal_Protect,OuterFan2_ContactorFD_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_Condesfan1_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组冷凝风机1故障
    """
    sql="select Outerfan1_Internalthermal_Protect,OuterFan1_ContactorFD_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_Compress2_LV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2低压故障
    """
    sql="select Sys2_LV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_Compress1_LV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1低压故障
    """
    sql="select Sys1_LV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])


def get_Compress2_HV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2高压故障
    """
    sql="select Sys2_HV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_Compress1_HV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1高压故障
    """
    sql="select Sys1_HV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_Compress1_communite_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1变频板通讯故障
    """
    sql="select Sys1_Inverter_Connect_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_Compress2_communite_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2变频板通讯故障
    """
    sql="select Sys2_Inverter_Connect_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_IO_communite_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2变频板通讯故障
    """
    sql="select IO1_Communication_Failure,IO2_Communication_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_Compress1_Ov_Protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1过载保护
    """
    sql="select Sys1_Inverter_HCurrlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])


def get_Compress2_Ov_Protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2过载保护
    """
    sql="select Sys2_Inverter_HCurrlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])


###########################轻微故障################################
def get_FreshAir_Sensor_fault(UnitNo,dt,lineNo,trainNo):
    """
    轻微故障:1机组新风传感器故障
    """
    sql="select Sensor1_FreshTemper_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_ReturnAir_Sensor_fault(UnitNo,dt,lineNo,trainNo):
    """
    轻微故障:1机组回风传感器故障
    """
    sql="select Sensor1_ReturnTemper_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_FreshAir_Valve_fault(UnitNo,dt,lineNo,trainNo):
    """
    轻微故障:1机组新风阀故障
    """
    sql="select FreshValve1_Fault,FreshValve2_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])

def get_ReturnAir_Valve_fault(UnitNo,dt,lineNo,trainNo):
    """
    轻微故障:1机组回风阀故障
    """
    sql="select ReturnValve1_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res[0])


def result_rule(UnitNo,dt,lineNo,trainNo):
    health_point=None
    serious_fault_res=get_ventilator1_fault(UnitNo,dt,lineNo,trainNo)+get_ventilator2_fault(UnitNo,dt,lineNo,trainNo)+get_emerinverter_fault(UnitNo,dt,lineNo,trainNo)+0

    mid_fault_res=get_converter2_protect(UnitNo,dt,lineNo,trainNo)+get_converter1_protect(UnitNo,dt,lineNo,trainNo)+get_Condesfan2_fault(UnitNo,dt,lineNo,trainNo)+get_Condesfan1_fault(UnitNo,dt,lineNo,trainNo)+ \
                  get_Compress2_LV_fault(UnitNo,dt,lineNo,trainNo)+get_Compress1_LV_fault(UnitNo,dt,lineNo,trainNo)+get_Compress2_HV_fault(UnitNo,dt,lineNo,trainNo)+get_Compress1_HV_fault(UnitNo,dt,lineNo,trainNo) + \
                  get_Compress1_communite_fault(UnitNo,dt,lineNo,trainNo)+get_Compress2_communite_fault(UnitNo,dt,lineNo,trainNo)+get_IO_communite_fault(UnitNo,dt,lineNo,trainNo)+get_Compress1_Ov_Protect(UnitNo,dt,lineNo,trainNo)+ \
                  get_Compress2_Ov_Protect(UnitNo,dt,lineNo,trainNo)+0

    slight_fault_res=get_FreshAir_Sensor_fault(UnitNo,dt,lineNo,trainNo)+get_ReturnAir_Sensor_fault(UnitNo,dt,lineNo,trainNo)+get_FreshAir_Valve_fault(UnitNo,dt,lineNo,trainNo)+ \
                     get_ReturnAir_Valve_fault(UnitNo,dt,lineNo,trainNo)+0
    # 正常:85-100 分
    if serious_fault_res+mid_fault_res+slight_fault_res==0:
        health_point=100-15*random.random()
        return health_point
    
    elif slight_fault_res>0:
        if slight_fault_res==1:
            health_point=85-10*random.random()
        if slight_fault_res==2:
            health_point=85-12*random.random()
        if slight_fault_res>2:
            health_point=85-14*random.random()
        return health_point

    elif mid_fault_res>0:
        if 3>=slight_fault_res>=1:
            health_point=70-15*random.random()
        if 6>=slight_fault_res>3:
            health_point=66-15*random.random()
        if slight_fault_res>6:
            health_point=63-15*random.random()
        return health_point
    
    elif serious_fault_res>0:
        if  serious_fault_res==1:
            health_point=60-30*random.random()
        if  serious_fault_res==2:
            health_point=50-30*random.random()
        if  slight_fault_res==3:
            health_point=45-30*random.random()
        return health_point
    # 严重故障
    else:
        health_point=100-15*random.random()
        return health_point

    




	
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
    res=result_rule(args.UnitNo,dt_str,args.lineNo,args.trainNo)
    print('{:*^30}'.format('健康评估分数'))  # 使用“*”填充

    print()

    # 运行
    # python models.py --UnitNo "2#" 
import time
import pymysql
import decimal
import flask

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

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="7515",
                           db="air_condition",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()# 执行完毕返回的结果集默认以元组显示
    return conn, cursor

def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

###########################严重故障################################
def get_ventilator2_fault(UnitNo,dt,lineNo,trainNo):
    """
    严重故障:1机组通风机2故障
    """
    sql="select Interfan2_Internalthermal_Protect,InterFan2_ContactorFD_Fault,InterFan2_ContactorLock_Alarm from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_ventilator1_fault(UnitNo,dt,lineNo,trainNo):
    """
    严重故障:1机组通风机1故障
    """
    sql="select Interfan1_Internalthermal_Protect,InterFan1_ContactorFD_Fault,InterFan1_ContactorLock_Alarm from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return res


def get_emerinverter_fault(UnitNo,dt,lineNo,trainNo):
    """
    严重故障:紧急逆变器故障
    """
    sql="select EmergencyInverter_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return res




###########################中等故障################################
def get_converter2_protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组压缩机2变频器保护，一般系统有通风无制冷
    """
    sql="select Sys2_Inverter_HTemperlock,Sys2_Inverter_HVollock,Sys2_Inverter_LVollock,Sys2_Inverter_MissPhasslock,Sys2_Inverter_OtherFaultlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_converter1_protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组压缩机1变频器保护，一般系统有通风无制冷
    """
    sql="select Sys1_Inverter_HTemperlock,Sys1_Inverter_HVollock,Sys1_Inverter_LVollock,Sys1_Inverter_MissPhasslock,Sys1_Inverter_OtherFaultlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)


def get_Condesfan2_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组冷凝风机2故障
    """
    sql="select Outerfan2_Internalthermal_Protect,OuterFan2_ContactorFD_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_Condesfan1_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组冷凝风机1故障
    """
    sql="select Outerfan1_Internalthermal_Protect,OuterFan1_ContactorFD_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_Compress2_LV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2低压故障
    """
    sql="select Sys2_LV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_Compress1_LV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1低压故障
    """
    sql="select Sys1_LV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)


def get_Compress2_HV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2高压故障
    """
    sql="select Sys2_HV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_Compress1_HV_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1高压故障
    """
    sql="select Sys1_HV_AlarmLock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_Compress1_communite_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1变频板通讯故障
    """
    sql="select Sys1_Inverter_Connect_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_Compress2_communite_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2变频板通讯故障
    """
    sql="select Sys2_Inverter_Connect_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_IO_communite_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2变频板通讯故障
    """
    sql="select IO1_Communication_Failure,IO2_Communication_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_Compress1_Ov_Protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机1过载保护
    """
    sql="select Sys1_Inverter_HCurrlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)


def get_Compress1_Ov_Protect(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:压缩机2过载保护
    """
    sql="select Sys2_Inverter_HCurrlock from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)


###########################轻微故障################################
def get_FreshAir_Sensor_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组新风传感器故障
    """
    sql="select Sensor1_FreshTemper_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_ReturnAir_Sensor_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组回风传感器故障
    """
    sql="select Sensor1_ReturnTemper_Failure from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_FreshAir_Valve_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组新风阀故障
    """
    sql="select FreshValve1_Fault,FreshValve2_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)

def get_FreshAir_Valve_fault(UnitNo,dt,lineNo,trainNo):
    """
    中等故障:1机组回风阀故障
    """
    sql="select ReturnValve1_Fault from alarm_log " \
        "where HappenTime<'{}' and UnitNo='{}' and Metro_Line_No='{}' and TrainNo='{}' order by HappenTime desc limit 1".format(dt,UnitNo,lineNo,trainNo)
    res = query(sql)
    return any(res)




	
if __name__ == "__main__":
    # print(get_r2_data())
    # import sys
    # print(sys.argv)
    # get_ventilator2_fault("2#",'2020-8-17 10:30')
    # get_ventilator1_fault("1#",'2020-8-17 10:30','5L','534')
    get_Condesfan1_fault("1#",'2020-8-17 10:30','5L','534')
# -*- coding: utf-8 -*-
from __future__ import division
import time
import math
import socket
import re
from multiprocessing import Process
import datetime
import json

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import redirect
import pandas as pd

#pandas.read_json   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html

# class COOLTEK_diagnostic_logic(object):
#     def __init__(self):
#         pass

#制冷剂泄漏预警
def Refrigerant_leak(df_RL):
    '''
    :param df_Refrigerant_leak:
    包含lowpressure compressorstatus working_flag三列 超过120s的数据
    :return:0为正常 1为故障
    '''
    print('start Refrigerant_leak')
    if df_RL.loc[df_RL.index[-1],'working_flag']==1:
        working_flag = 1 #open
    else:
        working_flag = 0 #close
    #空调压缩机为开启状态时的判断逻辑

    a = df_RL.loc[df_RL.index[-1] + datetime.timedelta(seconds=-30):, 'lowpressure'] < 6.0
    # any”意味着一行或者一列有一个为真（这里一般指不为0）则返回真，一行或者一列全部为假（一般指0）才为假，”all“意味着一行或者一列所有为真才为真（均不等于0），一行或者一列有一个为假则为假。
    if a.all():
        lowpressure_flag1 = 1
    else:
        lowpressure_flag1 = 0
    b=df_RL.loc[df_RL.index[-1] + datetime.timedelta(seconds=-100):,'compressorstatus'] ==0
    if b.all():
        compressorstatus_flag1 = 1
    else:
        compressorstatus_flag1 = 0
    if lowpressure_flag1==1 and compressorstatus_flag1==1:
        acon_flag1 = 1
    else:
        acon_flag1 = 0

    # 空调压缩机为关闭状态时的判断逻辑
    c=df_RL.loc[df_RL.index[-1]+datetime.timedelta(seconds=-10):,'lowpressure']<=0.5
    if c.all():
        lowpressure_flag2 = 1
    else:
        lowpressure_flag2 = 0
    d=df_RL.loc[df_RL.index[-1] + datetime.timedelta(seconds=-120):,'compressorstatus'] ==1
    if d.all():
        compressorstatus_flag2 = 1
    else:
        compressorstatus_flag2 = 0
    if lowpressure_flag2==1 and compressorstatus_flag2==1:
        acoff_flag2 = 1
    else:
        acoff_flag2 = 0

    if (acon_flag1==1 or acoff_flag2==1) and working_flag==1:
        Refrigerant_leak_flag=1
    else:
        Refrigerant_leak_flag = 0


    return Refrigerant_leak_flag






#排气温度过高/高压故障
def high_pressure_failure(df_hpf):
    '''
    :param df_hpf:
        compressorstatus压缩机运行状态
        newwindtemperature新风温度
        airouttemperature排气温度
        working_flag
        4列 超过5s的数据
    :return: 0为正常 1为故障
    '''
    if df_hpf.iloc[-1,-1]==1:
        working_flag = 1 #open
    else:
        working_flag = 0 #close
    # working_flag=df_hpf.iloc[-1,-1]
    a=df_hpf.loc[:,'compressorstatus'] ==1
    if a.all():
        compressorstatus_flag = 1
    else:
        compressorstatus_flag = 0
    if working_flag==1 and compressorstatus_flag==1:
        a1 = df_hpf.loc[df_hpf.index[-1] + datetime.timedelta(seconds=-5):, 'airouttemperature'] > 45
        a2 = df_hpf.loc[df_hpf.index[-1] + datetime.timedelta(seconds=-5):, 'airouttemperature'] > 55
        a3 = df_hpf.loc[df_hpf.index[-1] + datetime.timedelta(seconds=-5):, 'airouttemperature'] > 75
        a4 = df_hpf.loc[df_hpf.index[-1] + datetime.timedelta(seconds=-5):, 'airouttemperature'] > 85
        a5 = df_hpf.loc[df_hpf.index[-1] + datetime.timedelta(seconds=-5):, 'airouttemperature'] > 95
        a6 = df_hpf.loc[df_hpf.index[-1] + datetime.timedelta(seconds=-5):, 'airouttemperature'] > 105


        if df_hpf.loc[df_hpf.index[-1],'newwindtemperature']<=-5 and a1.all():
            high_pressure_failure_flag = 1
        elif df_hpf.loc[df_hpf.index[-1],'newwindtemperature']>-5  and df_hpf.loc[df_hpf.index[-1],'newwindtemperature']<=2 and a2.all():
            high_pressure_failure_flag = 1
        elif df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] > 2 and df_hpf.loc[df_hpf.index[-1],'newwindtemperature']<= 7 and a3.all():
            high_pressure_failure_flag = 1
        elif df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] > 7 and df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] <= 24 and a4.all():
            high_pressure_failure_flag = 1
        elif df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] > 24 and df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] <= 35 and a5.all():
            high_pressure_failure_flag = 1
        elif df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] > 35 and df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] <= 48 and a6.all():
            high_pressure_failure_flag = 1
        elif df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] > 48 and df_hpf.loc[df_hpf.index[-1],'newwindtemperature'] <= 55 and a6.all():
            high_pressure_failure_flag = 1
        else:
            high_pressure_failure_flag = 0

    else:
        high_pressure_failure_flag=0
    # high_pressure_failure_flag1=0
    return high_pressure_failure_flag

#制冷制热不正常
def Refrigeration_abnormal(df_Refrigeration_abnormal):
    '''
    :param df_Refrigeration_abnormal:
        inwindtemperature_avg 所有送风温度20分钟内平均数
        backwindtemperature_avg  所有回风温度20分钟内平均数
        compressorstatus_sum压缩机运行状态各机组相加求和35分钟内
        targettemperature_avg空调目标温度
        working_flag
        4列 35分钟数据
    :return: 0为正常 1为制冷不冷 2为制冷过冷 3为制热不热 4为制热过热
    '''
    if df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],['working_flag']].values[0]==1:
        working_flag = 1 #open
    else:
        working_flag = 0 #close
    print (working_flag)
    # m1s1_inwindtemperature_avg=df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],['m1s1_inwindtemperature_avg']].values[0]
    # m1s2_inwindtemperature_avg=df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],['m1s2_inwindtemperature_avg']].values[0]
    # m2s1_inwindtemperature_avg=df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],['m2s1_inwindtemperature_avg']].values[0]
    # m2s2_inwindtemperature_avg=df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],['m2s2_inwindtemperature_avg']].values[0]
    # inwindtemperature_avg=(m1s1_inwindtemperature_avg+ m1s2_inwindtemperature_avg+m2s1_inwindtemperature_avg+m2s2_inwindtemperature_avg)/4#各机组送风温度平均值
    # m1_backwindtemperature_avg=df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],['m1_backwindtemperature_avg']].values[0]
    # m2_backwindtemperature_avg=df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],['m2_backwindtemperature_avg']].values[0]
    # backwindtemperature_avg=(m1_backwindtemperature_avg+m2_backwindtemperature_avg)/2#各机组回风温度平均值
    inwindtemperature_avg=df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],'inwindtemperature_avg']#.values[0]
    backwindtemperature_avg = df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1],'backwindtemperature_avg']#.values[0]
    print ('各机组送风温度平均值',inwindtemperature_avg)
    print ('各机组回风温度平均值',backwindtemperature_avg)

    if (inwindtemperature_avg-backwindtemperature_avg) < 0:#制冷模式 判断是否异常
        a = df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1] + datetime.timedelta(minutes=-35):,
            'compressorstatus_sum'] > 0.0
        if a.all():
            compressorstatus_flag = 1
        else:
            compressorstatus_flag = 0
        print(compressorstatus_flag)
        targettemperature_avg = \
        df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1], ['targettemperature_avg']].values[0]
        print(targettemperature_avg)
        if working_flag == 1 and compressorstatus_flag == 1:
            if backwindtemperature_avg - targettemperature_avg > 2:
                Refrigeration_abnormal_flag = 1  # 制冷不冷
            elif backwindtemperature_avg - targettemperature_avg < -2:
                Refrigeration_abnormal_flag = 2  # 制冷过冷
            else:
                Refrigeration_abnormal_flag = 0 # 制冷正常
        else:
            Refrigeration_abnormal_flag = 0  # 制冷正常

    elif (inwindtemperature_avg-backwindtemperature_avg) > 0: #制热模式 判断是否异常
        a = df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1] + datetime.timedelta(minutes=-35):,
            'compressorstatus_sum'] > 0.0
        if a.all():
            compressorstatus_flag = 1
        else:
            compressorstatus_flag = 0
        print(compressorstatus_flag)
        targettemperature_avg = \
            df_Refrigeration_abnormal.loc[df_Refrigeration_abnormal.index[-1], ['targettemperature_avg']].values[0]
        print(targettemperature_avg)
        if working_flag == 1 and compressorstatus_flag == 1:
            if backwindtemperature_avg - targettemperature_avg > 2:
                Refrigeration_abnormal_flag = 4  # 制热过热
            elif backwindtemperature_avg - targettemperature_avg < -2:
                Refrigeration_abnormal_flag = 3  # 制热不热
            else:
                Refrigeration_abnormal_flag = 0  # 制热正常
        else:
            Refrigeration_abnormal_flag = 0  # 制冷正常
    else:
        Refrigeration_abnormal_flag=0

    return Refrigeration_abnormal_flag



app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route('/HPF_getjson/<njson>')#高压故障
def HPF_getjson(njson):#高压故障
    print('start HPF_getjson')
    inputdata_df = pd.read_json(njson, orient='index').sort_index()
    high_pressure_failure_flag = high_pressure_failure(inputdata_df)
    print('high_pressure_failure_flag ' + str(high_pressure_failure_flag))
    return json.dumps(int(high_pressure_failure_flag))

@app.route('/RL_getjson/<njson>')#制冷剂泄漏预警
def RL_getjson(njson):#制冷剂泄漏预警

    # dict1 = json.loads(njson)
    # input_data = dict1["inputs"]
    # input_value = []
    # for key in data_key:
    #     input_value.append(float(input_data[key[1:-1]]))
    # inputdata_df = input_value
    print('start RL_getjson')
    inputdata_df =pd.read_json(njson, orient='index').sort_index()
    Refrigerant_leak_flag=Refrigerant_leak(inputdata_df)
    print('Refrigerant_leak_flag '+str(Refrigerant_leak_flag))
    return json.dumps(int(Refrigerant_leak_flag))

def HPF_getjson(njson):#高压故障
    print('start HPF_getjson')
    inputdata_df = pd.read_json(njson, orient='index').sort_index()
    high_pressure_failure_flag = high_pressure_failure(inputdata_df)
    print('high_pressure_failure_flag ' + str(high_pressure_failure_flag))
    return json.dumps(int(high_pressure_failure_flag))

@app.route('/RA_getjson/<njson>')#制冷不正常
def RA_getjson(njson):#制冷不正常
    print('start Refrigeration_abnormal')
    inputdata_df =pd.read_json(njson, orient='index').sort_index()
    # print (inputdata_df)
    Refrigeration_abnormal_flag=Refrigeration_abnormal(inputdata_df)
    print('Refrigeration_abnormal '+str(Refrigeration_abnormal_flag))
    return json.dumps(int(Refrigeration_abnormal_flag))

# @app.route('/HA_getjson/<njson>')#制热不正常
# def HA_getjson(njson):#制热异常
#     print('start Heating_abnormal')
#     inputdata_df = pd.read_json(njson, orient='index').sort_index()
#     # print (inputdata_df)
#     Heating_abnormal_flag = Heating_abnormal(inputdata_df)
#     print('Refrigeration_abnormal ' + str(Heating_abnormal_flag))
#     return json.dumps(int(Heating_abnormal_flag))




if __name__ == '__main__':

    print('start')
    # app.run(debug=True,host='10.84.1.203',port=8000,threaded=True) #多线程
    app.run(debug=True, host='10.84.1.203', port=8000)  # 单线程


    # njson ='{"2019-09-27 11:26:33":{"lowpressure":270,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:34":{"lowpressure":261,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:35":{"lowpressure":268,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:36":{"lowpressure":264,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:37":{"lowpressure":251,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:38":{"lowpressure":289,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:39":{"lowpressure":274,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:40":{"lowpressure":268,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:41":{"lowpressure":260,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:42":{"lowpressure":283,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:43":{"lowpressure":289,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:44":{"lowpressure":285,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:45":{"lowpressure":299,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:46":{"lowpressure":279,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:47":{"lowpressure":265,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:48":{"lowpressure":276,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:49":{"lowpressure":297,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:50":{"lowpressure":290,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:51":{"lowpressure":292,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:52":{"lowpressure":287,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:53":{"lowpressure":289,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:54":{"lowpressure":266,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:55":{"lowpressure":274,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:56":{"lowpressure":273,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:57":{"lowpressure":270,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:58":{"lowpressure":291,"compressorstatus":1,"working_flag":1},"2019-09-27 11:26:59":{"lowpressure":256,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:00":{"lowpressure":258,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:01":{"lowpressure":275,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:02":{"lowpressure":283,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:03":{"lowpressure":286,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:04":{"lowpressure":288,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:05":{"lowpressure":291,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:06":{"lowpressure":286,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:07":{"lowpressure":256,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:08":{"lowpressure":291,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:09":{"lowpressure":274,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:10":{"lowpressure":283,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:11":{"lowpressure":269,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:12":{"lowpressure":278,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:13":{"lowpressure":296,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:14":{"lowpressure":269,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:15":{"lowpressure":259,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:16":{"lowpressure":289,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:17":{"lowpressure":260,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:18":{"lowpressure":300,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:19":{"lowpressure":258,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:20":{"lowpressure":274,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:21":{"lowpressure":295,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:22":{"lowpressure":293,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:23":{"lowpressure":270,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:24":{"lowpressure":272,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:25":{"lowpressure":267,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:26":{"lowpressure":253,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:27":{"lowpressure":268,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:28":{"lowpressure":284,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:29":{"lowpressure":281,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:30":{"lowpressure":298,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:31":{"lowpressure":269,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:32":{"lowpressure":280,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:33":{"lowpressure":299,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:34":{"lowpressure":284,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:35":{"lowpressure":270,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:36":{"lowpressure":251,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:37":{"lowpressure":296,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:38":{"lowpressure":276,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:39":{"lowpressure":293,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:40":{"lowpressure":270,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:41":{"lowpressure":296,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:42":{"lowpressure":300,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:43":{"lowpressure":257,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:44":{"lowpressure":260,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:45":{"lowpressure":289,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:46":{"lowpressure":257,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:47":{"lowpressure":292,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:48":{"lowpressure":266,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:49":{"lowpressure":277,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:50":{"lowpressure":272,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:51":{"lowpressure":290,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:52":{"lowpressure":254,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:53":{"lowpressure":281,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:54":{"lowpressure":255,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:55":{"lowpressure":292,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:56":{"lowpressure":287,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:57":{"lowpressure":262,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:58":{"lowpressure":278,"compressorstatus":1,"working_flag":1},"2019-09-27 11:27:59":{"lowpressure":261,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:00":{"lowpressure":258,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:01":{"lowpressure":287,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:02":{"lowpressure":259,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:03":{"lowpressure":257,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:04":{"lowpressure":284,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:05":{"lowpressure":286,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:06":{"lowpressure":298,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:07":{"lowpressure":295,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:08":{"lowpressure":261,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:09":{"lowpressure":262,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:10":{"lowpressure":268,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:11":{"lowpressure":251,"compressorstatus":1,"working_flag":1},"2019-09-27 11:28:12":{"lowpressure":263,"compressorstatus":1,"working_flag":1}}'
    # RL_getjson(njson)
    # njson ='{"2019-09-27 11:57:14":{"compressorstatus":1,"newwindtemperature":26,"airouttemperature":26,"working_flag":1},"2019-09-27 11:57:15":{"compressorstatus":1,"newwindtemperature":26,"airouttemperature":26,"working_flag":1},"2019-09-27 11:57:16":{"compressorstatus":1,"newwindtemperature":25,"airouttemperature":25,"working_flag":1},"2019-09-27 11:57:17":{"compressorstatus":1,"newwindtemperature":25,"airouttemperature":26,"working_flag":1},"2019-09-27 11:57:18":{"compressorstatus":1,"newwindtemperature":25,"airouttemperature":26,"working_flag":1},"2019-09-27 11:57:19":{"compressorstatus":1,"newwindtemperature":26,"airouttemperature":25,"working_flag":1},"2019-09-27 11:57:20":{"compressorstatus":1,"newwindtemperature":26,"airouttemperature":25,"working_flag":1},"2019-09-27 11:57:21":{"compressorstatus":1,"newwindtemperature":25,"airouttemperature":26,"working_flag":1},"2019-09-27 11:57:22":{"compressorstatus":1,"newwindtemperature":26,"airouttemperature":25,"working_flag":1},"2019-09-27 11:57:23":{"compressorstatus":1,"newwindtemperature":25,"airouttemperature":26,"working_flag":1}}'
    # njson ='{"2019-10-09 10:51:19":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":26,"working_flag":1},"2019-10-09 10:51:20":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":25,"working_flag":1},"2019-10-09 10:51:21":{"airouttemperature":25,"compressorstatus":1,"newwindtemperature":25,"working_flag":1},"2019-10-09 10:51:22":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":26,"working_flag":1},"2019-10-09 10:51:23":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":25,"working_flag":1},"2019-10-09 10:51:24":{"airouttemperature":25,"compressorstatus":1,"newwindtemperature":26,"working_flag":1},"2019-10-09 10:51:25":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":26,"working_flag":1},"2019-10-09 10:51:26":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":26,"working_flag":1},"2019-10-09 10:51:27":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":25,"working_flag":1},"2019-10-09 10:51:28":{"airouttemperature":26,"compressorstatus":1,"newwindtemperature":26,"working_flag":1}}'
    # HPF_getjson(njson)
    # njson='{"2019-06-24 01:48:47":{"backwindtemperature_avg":253,"compressorstatus_sum":3740,"inwindtemperature_avg":240,"targettemperature_avg":252,"working_flag":1}}'
    # RA_getjson(njson)
    print('finish')
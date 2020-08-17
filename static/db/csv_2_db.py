import time
import pymysql
import os,sys
import csv
import traceback

# path=r"E:\AirCondition\data\1\2#-EnviLog-2020-2(1)(1).csv"
# with open(path,'r') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#     rows = [row for row in reader]
# print(rows)

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

def get_field():
    field_list=[]
    sql="select COLUMN_NAME from information_schema.COLUMNS where table_name = '{}' and table_schema = '{}'".format('condition_data','air_condition')
    res=query(sql)
    for tmp in res:
        for field in tmp:
            field_list.append(field)
    print("field_list:\n",field_list )
    print(len(field_list))
  
   


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


def readAllFiles(filePath):
    """
    读取文件夹下的csv文件
    """
    fileList = os.listdir(filePath)
    for file in fileList:
        path = os.path.join(filePath, file)
        if os.path.isfile(path):
            print(path)
            #流程记录信息
            if path.find("EnviLog") != -1:
                insertdata(path)
            else:
                continue
        else:
            readAllFiles(path)



# def analysisWorkflowCsv(file):
#     """
#     解析文件:解析文件内容，首行为标题栏需要跳过。入库操作每满1000条commit一次主要是python频繁提交执行次数达到1000+就会报错。1000条commit一次可以避免错误并缓解内存压力。
#     """
#     with open(file,'rb') as f:
#         csvFile = csv.reader(f)

#         # 读取一行，下面的reader中已经没有该行了
#         head_row = next(csvFile)
#         # print(head_row)
#         counter = 0
#         for row in csvFile:
            
#             if insertWorkflows(__conn, workflow):
#                 counter += 1
#             if counter % 1000 == 0:
#                 __conn.commitData()
#         print("已经插入工作流数据： %d 条。"%counter)
#         __conn.commitData()
#         __conn.closeConn()



def insertdata(file):
    """
    插入空调数据
    """
    CarriageNo=file.split('\\')[-2]
    TrainNo=(file.split('\\')[-3]).split('-')[-1]
    Metro_lineNo=file.split('\\')[-4]
    UnitNo=(file.split('\\')[-1]).split('-')[0]
    Train_Type="05C01"


    with open(file,'r') as f:
        csvData= csv.reader(f)
        # 读取一行，下面的reader中已经没有该行了
        head_row = next(csvData)
        # app=[row for row in csvData ]


        

        sql = "INSERT INTO condition_data ( Metro_Line_No,Train_Type,TrainNo, CarriageNo,UnitNo, HappenTime, ReturnTemper_1, ReturnTemper_2, VentilationTemper_1, VentilationTemper_2,DeliveryTemper_1," \
            "DeliveryTemper_2, Sys1_Evaporator1_MedTemper, Sys1_Evaporator2_MedTemper, Sys2_Evaporator1_MedTemper, Sys2_Evaporator2_MedTemper, Evaporator1_OutletTemper_1," \
            "Evaporator1_OutletTemper_2, Evaporator2_OutletTemper_1, Evaporator2_OutletTemper_2, Condenser1_Temper, Condenser2_Temper, Sys1_InspiratoryTemper," \
            "Sys2_InspiratoryTemper, Sys1_ExhaustTemper, Sys2_ExhaustTemper, Sys1_LowPressure, Sys2_LowPressure, Sys1_HighPressure, Sys2_HighPressure," \
            "Sys1_CondensPressure,  Sys2_CondensPressure, Passenger_CompartTempter_1, Passenger_CompartTempter_2, Passenger_HumidityTempter_1, Passenger_HumidityTempter_2," \
            "UnitTempter_1, UnitTempter_2, UnitHumidity_1, UnitHumidity_2, FreshValve_FB_1, FreshValve_FB_2, L1_L2_V, L3_L2_V, L1_L3_V, L1_Current, L2_Current, L3_Current," \
            "N_Current, Energy_H, Energy_L, PowerRate_H, PowerRate_L, Unit_Mean_V, Unit_Mean_Current, Sys1_Discharge_Superheat, Sys2_Discharge_Superheat, Sys1_Inspiratory_Superheat," \
            "Sys2_Inspiratory_Superheat, Sys1_Condens_Undercool, Sys2_Condens_Undercool, Sys1_EvaporSat_Tempter, Sys2_EvaporSat_Tempter, Sys1_CondensSat_Tempter, Sys2_CondensSat_Tempter," \
            "Vehicle_load, Return_Air_Mean_Temper, Outlet_Air_MeanTemper, Fresh_Air_MeanTemper, Return_Air_HotSpot_Temper, Outlet_HotSpot_Temper, Return_Air_MeanHumidity, Control_Temper," \
            "Control_Humidity, Dew_Point_Humidity, Return_Air_MeanTemper_T, Outlet_Air_MeanTemper_T, Fresh_Air_MeanTemper_T, Return_Air_MeanHumidity_T, Mean_CariageTemper_T," \
            "Sys1_Coil1_Outlet_Superheat, Sys2_Coil1_Outlet_Superheat, Sys1_Coil2_Outlet_Superheat, Sys1_Coil2_Outlet_Superheat_0, Rail_Mean_humidity30, Dynamic_Outlet_PointTemper_Calu," \
            "Unit_PointTemper_Calu, Coil_Compressor_Demand, Dehumidification_Status, FreshValve_Pos_FB1_Calu, FreshValve_Pos_FB2_Calu, Refrigeration_Feedforward, Heat_Feed_Forward," \
            "Cool_Displacement, Heat_Displacement, Overall_Power, UIC_Temper_Limit, Fresh_Valve_Opening, Mean_Codens_Mediate_Temper, Mean_Evaporation_Mediate_Temper, Mean_Evaporation_Median_Temper_T," \
            "Converter1_Frequency, Converter2_Frequency, EEPROM_Error_Num, InterFan_1, interFan_2, OuterFan_1, OuterFan_2, Compressor_1, Compressor_2, Return_Air_Valve, Fresh_Air_Valve, Eleic_Expan_Valve_1," \
            "Eleic_Expan_Valve_2, Eleic_Expan_Valve_3, Eleic_Expan_Valve_4, Fresh_Alve_Demend ) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s," \
                    "%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s," \
                    "%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s," \
                    "%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s," \
                    "%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s,%s,%s)"
           
            
            


        cursor = None
        conn = None

        row1=[Metro_lineNo,Train_Type,TrainNo,CarriageNo,UnitNo]
        try:
            conn, cursor = get_conn()
            print(f"{time.asctime()}开始插入历史数据")
            for row in csvData:
                row=row1+row
                try:
                    row=[rw.strip() for rw in row[0:6]]+[float(rw.strip()) for rw in row[6:]]
                    cursor.execute(sql, row)
                    conn.commit()
                except:
                    pass
                continue
                
            # if counter % 1000 == 0:
            #     conn.commit()  # 提交事务 update delete insert操作
            print(f"{time.asctime()}插入历史数据完毕")
        except:
            traceback.print_exc()
        finally:
            close_conn(conn, cursor)


if __name__ == '__main__':
    cPath = os.getcwd()+'\data'
    readAllFiles(cPath)
    
    # for fileName in os.listdir(cPath) :
    #     print (fileName)

    # get_field()
    # readAllFiles(filePath)
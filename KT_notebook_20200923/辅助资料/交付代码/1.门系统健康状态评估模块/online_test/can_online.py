#!/usr/bin/env python
# coding: utf-8

import pandas as pd
#import pymysql
#pymysql.install_as_MySQLdb()
import MySQLdb as sql
import sklearn.mixture as mix
import numpy as np
import math
import time
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#from pyecharts import Line

#不输出警告
import warnings
warnings.filterwarnings("ignore")
import time
import datetime
import pickle
from sklearn.externals import joblib
#0号门模型
a_open_sd_model_flie='onlycan_opendata_sd_model0.pkl'
a_close_sd_model_flie='onlycan_closedata_sd_model0.pkl'
a_open_normal_model_flie='onlycan_opendata_normal_obj_model0.pkl'
a_close_normal_model_flie='onlycan_closedata_normal_obj_model0.pkl'
#1号门模型
b_open_sd_model_flie='onlycan_opendata_sd_model1.pkl'
b_close_sd_model_flie='onlycan_closedata_sd_model1.pkl'
b_open_normal_model_flie='onlycan_opendata_normal_obj_model1.pkl'
b_close_normal_model_flie='onlycan_closedata_normal_obj_model1.pkl'




#计算CV值
def calculate_cv(MG1,MG2):

    
    NumMixture1 = MG1.n_components
    NumMixture2 = MG2.n_components
    d = 0.0
    for k in range(0,NumMixture1):
        for j in range(0,NumMixture2):
            Sigma1 = MG1.covariances_[k]
            Mu1 = MG1.means_[k]
            Sigma2 = MG2.covariances_[j]
            Mu2 = MG2.means_[j]
            weight = MG1.weights_[k] * MG2.weights_[j]
            dist = L2Dist(Sigma1,Mu1,Sigma2,Mu2)
            d = d + weight*dist
    ''' the L2 norm of each GMM model'''
    n1 = 0.0
    n2 = 0.0
    for k in range(0,NumMixture1):
        for j in range(0,NumMixture1):
            Sigma1 = MG1.covariances_[k]
            Mu1 = MG1.means_[k]
            Sigma2 = MG1.covariances_[j]
            Mu2 = MG1.means_[j]
            weight = MG1.weights_[k]*MG1.weights_[j]
            n1 = n1 + weight * L2Dist(Sigma1,Mu1,Sigma2,Mu2)
    for k in range(0,NumMixture2):
        for j in range(0,NumMixture2):
            Sigma1 = MG2.covariances_[k]
            Mu1 = MG2.means_[k]
            Sigma2 = MG2.covariances_[j]
            Mu2 = MG2.means_[j]
            weight = MG2.weights_[k]*MG2.weights_[j]
            n2 = n2 + weight * L2Dist(Sigma1,Mu1,Sigma2,Mu2)
    cv = d/np.sqrt(n1)/np.sqrt(n2)
    return cv





#计算两个高斯分布之间的距离
def L2Dist(sigma1,mean1,sigma2,mean2):
    '''
    calculate the L2 distance between two multivariate Gaussian distributisons
    
    '''    
    n = mean1.size
    
    '''L2 norm of sigma1, mean1'''
    
    invsigma1 = np.linalg.inv(sigma1)
    invsigma2 = np.linalg.inv(sigma2)
    u = invsigma1*mean1 + invsigma2*mean2
    invsigma = np.linalg.inv(sigma1+sigma2)
    f1norm = 1/math.sqrt( math.sqrt( (2*math.pi)**n*np.linalg.det(sigma1)*2**n ) )
    '''L2 norm of sigma2, mean2'''
    f2norm = 1/math.sqrt( math.sqrt( (2*math.pi)**n*np.linalg.det(sigma2)*2**n ) )
    '''inner product of pdf f1 and f2'''
    
    InnerProd = 1/(math.sqrt(2*math.pi)**n) * math.sqrt(np.linalg.det(invsigma)) *                 np.exp(-1/2*(-u.T*sigma1*invsigma*sigma2*u + mean1.T*invsigma1*mean1 + mean2.T*invsigma2*mean2))
    '''L2 distance between f1 and f2'''
    d = InnerProd/f1norm/f2norm
    
    return d





#训练高斯模型
def gmm_clustering(k,X,cov_type=None):
    '''
    基于高斯混合模型GMM进行无监督学习，聚类
    其中GMM采用传统的EM算法进行参数估计
    
    输入参数含义:
    k    ————   聚类的数目，必填项
    X    ————   样本的输入，比填项
    cov_type  ————  协方差类型，可选项
            四种选择：'spherical', 'tied', 'diag', 'full'
            如果不填写，则默认为'full'
        
    '''
    if cov_type is None:
        cov_type = 'full'   
    
    gmm = mix.GaussianMixture(n_components=k,covariance_type=cov_type)
    gmm.fit(X)
    
    return gmm





def opendata_cv(rawdata_can_open,open_sd_model_flie,open_normal_model_flie):
    #对数据进标准标准化
    data_st1_nors = rawdata_can_open.copy()    
    standardscaler_st1 = joblib.load(open_sd_model_flie) #load标准化模型    
    data_st1_sd = standardscaler_st1.transform(data_st1_nors)#使用该模型将未去除离群点的数据归一化
    
    data_st1_sd = pd.DataFrame(data_st1_sd)
    data_st1_sd.index=data_st1_nors.index
    data_st1_sd.columns=data_st1_nors.columns
    #使用gmm计算与标准状态之间的cv值
    k = 1
    data_s = data_st1_sd.copy()    
    normal_obj = joblib.load(open_normal_model_flie) 

    #使用高斯混合模型进行计算
    def gmm_apply(x,k,normal_obj):
        data_l = pd.DataFrame(x)
        test_obj = gmm_clustering(k,data_l)#test_obj为训练好的gmm模型，需保存
        y = calculate_cv(normal_obj,test_obj)#y为[[cv值]]，只返回cv值
        return y[0][0]
    
    #计算每一行的cv值，存在data_s的cv列中         
    data_s['cv']=data_s.apply(lambda row:gmm_apply(row,k,normal_obj), axis=1)
    #cv=gmm_apply(data_s,k,normal_obj)
    return pd.DataFrame(data_s.loc[:,'cv'])





def closedata_cv(rawdata_can_open,close_sd_model_flie,close_normal_model_flie):
    #对数据进标准标准化
    data_st1_nors = rawdata_can_open.copy()    
    standardscaler_st1 = joblib.load(close_sd_model_flie) #load标准化模型    
    data_st1_sd = standardscaler_st1.transform(data_st1_nors)#使用该模型将未去除离群点的数据归一化
    
    data_st1_sd = pd.DataFrame(data_st1_sd)
    data_st1_sd.index=data_st1_nors.index
    data_st1_sd.columns=data_st1_nors.columns
    #使用gmm计算与标准状态之间的cv值
    k = 1
    data_s = data_st1_sd.copy()    
    normal_obj = joblib.load(close_normal_model_flie) 
    
    #使用高斯混合模型进行计算
    def gmm_apply(x,k,normal_obj):
        data_l = pd.DataFrame(x)
        test_obj = gmm_clustering(k,data_l)#test_obj为训练好的gmm模型，需保存
        y = calculate_cv(normal_obj,test_obj)#y为[[cv值]]，只返回cv值
        return y[0][0]
    
    #计算每一行的cv值，存在data_s的cv列中         
    data_s['cv']=data_s.apply(lambda row:gmm_apply(row,k,normal_obj), axis=1)
    #cv=gmm_apply(data_s,k,normal_obj)
    return pd.DataFrame(data_s.loc[:,'cv'])


# ### 主函数



if __name__=='__main__':   
    
#    #连接本地数据库
#    config = {'user': 'root',
#    		  'passwd': '123456',
#    		  'host': '127.0.0.1',
#    		  'db': 'elevator_door'}
#    database='door_data_can'
#    sql_statement="select * from "+database+" where read_flag is null"
    

    #连接外部数据库
    config = {'user': 'root',
                 'passwd': 'ABCabc123',
                 'host': '10.84.1.20',
                 'db': 'maoqing'}    
    database='door_data_can0429_copy'
    sql_statement="select * from "+database+" where read_flag is null"
    
    
    
    while(1):
        print('start')
        #链接数据库读取新数据
        conn = sql.connect(**config)
        cur = conn.cursor(cursorclass=sql.cursors.DictCursor)#返回字段名
        #根据read_flag为null筛选出新录入的数据
        #cur.execute("select * from "+database+" where read_flag is null")#door_data_can 为原始数据表名
        #data=cur.fetchall()#执行读取操作
        #rawdata_can = pd.DataFrame(list(data))#将读取结果转为dataframe格式
        time_start=time.time()
        rawdata_can=pd.read_sql(sql_statement,conn)
        rawdata_can.head()
        #将HAPPENTIME列属性改为时间，并设置为index        
        #rawdata_can['HAPPENTIME']=pd.to_datetime(rawdata_can['HAPPENTIME'])
        #rawdata_can=rawdata_can.set_index('HAPPENTIME')
        rawdata_can=rawdata_can.set_index('id')
        rawdata_can=rawdata_can.loc[:,['E_Q', 'E_D', 'SPEED_SUM',  'SPEED_MAX_P',
               'SPEED_MAX_N', 'SPEED_MAX_N_POSITION', 'START_POSITION', 'END_POSITION',
               'IQ_SUM_P', 'IQ_SUM_N', 'ID_SUM_P', 'ID_SUM_N', 'EM','SPEED_SUM_SQR','SPEED_SUM_CNT','DOOR_STATE','GATE']].copy()
        rawdata_can=rawdata_can.dropna()#删除有缺失值的行
        
        rawdata_can.shape
        rawdata_can.head()  
    
        time_end=time.time()
        print('read sql cost',datetime.timedelta(seconds=time_end-time_start))
        #统计读取出来的数据中有多少个门的数据
        rawdata_can_group=rawdata_can.groupby('GATE').count()
        for door_gate in rawdata_can_group.index:
            print ('door_gate',door_gate)
    
    
    
    #####################################################################################################
        time_start=time.time()
        #对读进来的所有行的read_flag置1
        if len(rawdata_can)==0:
            print('rawdata_can is empty')
        else:
            print('rawdata_can is '+str(len(rawdata_can)))
            cur.execute('update '+database+' set read_flag = 1 where id <= '+str(rawdata_can.index[-1]))
            conn.commit()
            print('read_flag finish')
        time_end=time.time()
        print('read_flag置1 cost',datetime.timedelta(seconds=time_end-time_start))
#    
    ######0号门数据###############################################################################################
        
        #筛选开门数据
        a_rawdata_can_open=rawdata_can[(rawdata_can['DOOR_STATE'].astype(str)=='0010011100100101')&(rawdata_can['GATE'].astype(str)==str(0))]
#        rawdata_can_open=rawdata_can_open.dropna()#删除缺失数据
        if len(a_rawdata_can_open)==0:
            pass
        else:
#            rawdata_can_open=rawdata_can_open.loc[:,['E_Q', 'E_D', 'SPEED_SUM',  'SPEED_MAX_P',
#               'SPEED_MAX_N', 'SPEED_MAX_N_POSITION', 'START_POSITION', 'END_POSITION',
#               'IQ_SUM_P', 'IQ_SUM_N', 'ID_SUM_P', 'ID_SUM_N', 'EM','SPEED_SUM_SQR','SPEED_SUM_CNT','DOOR_STATE_TIME']].copy()
            
            a_rawdata_can_open['SPEED_SUM_SQR_REAL'] = a_rawdata_can_open['SPEED_SUM_SQR']/a_rawdata_can_open['SPEED_SUM_CNT']
            a_rawdata_can_open=a_rawdata_can_open.drop(labels=['SPEED_SUM_SQR','SPEED_SUM_CNT','GATE','DOOR_STATE'],axis=1)#删除计算后的两列
        #筛选关门数据
        a_rawdata_can_close=rawdata_can[((rawdata_can['DOOR_STATE'].astype(str)=='0010101100101010')^(rawdata_can['DOOR_STATE'].astype(str)=='0010101100100011'))&(rawdata_can['GATE'].astype(str)==str(0))] #

        if len(a_rawdata_can_close)==0:#若读取进来的数据中没有关门数据
            pass
        else:
#            rawdata_can_close=rawdata_can_close.loc[:,['E_Q', 'E_D', 'SPEED_SUM',  'SPEED_MAX_P',
#               'SPEED_MAX_N', 'SPEED_MAX_N_POSITION', 'START_POSITION', 'END_POSITION',
#               'IQ_SUM_P', 'IQ_SUM_N', 'ID_SUM_P', 'ID_SUM_N', 'EM','SPEED_SUM_SQR','SPEED_SUM_CNT','DOOR_STATE_TIME']].copy()
            
            a_rawdata_can_close['SPEED_SUM_SQR_REAL'] = a_rawdata_can_close['SPEED_SUM_SQR']/a_rawdata_can_close['SPEED_SUM_CNT']
            a_rawdata_can_close=a_rawdata_can_close.drop(labels=['SPEED_SUM_SQR','SPEED_SUM_CNT','GATE','DOOR_STATE'],axis=1)#删除计算后的两列
    
    #####################################################################################################
        #计算开门数据的cv值并写入数据库
        
        if len(a_rawdata_can_open)==0:
            pass
        else:
            time_start=time.time()
            a_open_cv=opendata_cv(a_rawdata_can_open,a_open_sd_model_flie,a_open_normal_model_flie)#计算所有开门数据的cv值
            time_end=time.time()
            print('door 0 opendata cv cost',datetime.timedelta(seconds=time_end-time_start))
            time_start=time.time()
            for indexs in a_open_cv.index:
                for i in a_open_cv.ix[indexs].values:
                    row_cv=i
                row_id=indexs
                #print('update '+database+' set CV ='+str(row_cv)+' where id = '+str(row_id))
                cur.execute('update '+database+' set CV ='+str(row_cv)+' where id = '+str(row_id))
                conn.commit()   
            time_end=time.time()
            print('updata door 0 open cv cost',datetime.timedelta(seconds=time_end-time_start))
        
        #计算关门数据的cv值并写入数据库
        if len(a_rawdata_can_close)==0:#若读取进来的数据中没有关门数据
            pass
        else:
            time_start=time.time()
            a_close_cv=closedata_cv(a_rawdata_can_close,a_close_sd_model_flie,a_close_normal_model_flie)#计算所有关门数据的cv值
            time_end=time.time()
            print('door 0 closedata cv cost',datetime.timedelta(seconds=time_end-time_start))
            time_start=time.time()
            for indexs in a_close_cv.index:
                #将计算出的cv值写入数据库cv列
                for i in a_close_cv.ix[indexs].values:
                    row_cv=i
                row_id=indexs
                #print('update '+database+' set CV ='+str(row_cv)+' where id = '+str(row_id))
                cur.execute('update '+database+' set CV ='+str(row_cv)+' where id = '+str(row_id))
                conn.commit()
            time_end=time.time()
            print('updata door 0 close cv cost',datetime.timedelta(seconds=time_end-time_start))
        print('door 0 finish')
    
    #####1号门数据################################################################################################
        #筛选开门数据
        b_rawdata_can_open=rawdata_can[(rawdata_can['DOOR_STATE'].astype(str)=='0010011100100101')&(rawdata_can['GATE'].astype(str)==str(1))]
#        rawdata_can_open=rawdata_can_open.dropna()#删除缺失数据
        if len(b_rawdata_can_open)==0:
            pass
        else:
#            rawdata_can_open=rawdata_can_open.loc[:,['E_Q', 'E_D', 'SPEED_SUM',  'SPEED_MAX_P',
#               'SPEED_MAX_N', 'SPEED_MAX_N_POSITION', 'START_POSITION', 'END_POSITION',
#               'IQ_SUM_P', 'IQ_SUM_N', 'ID_SUM_P', 'ID_SUM_N', 'EM','SPEED_SUM_SQR','SPEED_SUM_CNT','DOOR_STATE_TIME']].copy()
            
            b_rawdata_can_open['SPEED_SUM_SQR_REAL'] = b_rawdata_can_open['SPEED_SUM_SQR']/b_rawdata_can_open['SPEED_SUM_CNT']
            b_rawdata_can_open=b_rawdata_can_open.drop(labels=['SPEED_SUM_SQR','SPEED_SUM_CNT','GATE','DOOR_STATE'],axis=1)#删除计算后的两列
        
        #筛选关门数据
        b_rawdata_can_close=rawdata_can[((rawdata_can['DOOR_STATE'].astype(str)=='0010101100101010')^(rawdata_can['DOOR_STATE'].astype(str)=='0010101100100011'))&(rawdata_can['GATE'].astype(str)==str(1))] #

#        rawdata_can_close=rawdata_can_close.dropna()#删除缺失数据
        if len(b_rawdata_can_close)==0:#若读取进来的数据中没有关门数据
            pass
        else:
#            rawdata_can_close=rawdata_can_close.loc[:,['E_Q', 'E_D', 'SPEED_SUM',  'SPEED_MAX_P',
#               'SPEED_MAX_N', 'SPEED_MAX_N_POSITION', 'START_POSITION', 'END_POSITION',
#               'IQ_SUM_P', 'IQ_SUM_N', 'ID_SUM_P', 'ID_SUM_N', 'EM','SPEED_SUM_SQR','SPEED_SUM_CNT','DOOR_STATE_TIME']].copy()
            
            b_rawdata_can_close['SPEED_SUM_SQR_REAL'] = b_rawdata_can_close['SPEED_SUM_SQR']/b_rawdata_can_close['SPEED_SUM_CNT']
            b_rawdata_can_close=b_rawdata_can_close.drop(labels=['SPEED_SUM_SQR','SPEED_SUM_CNT','GATE','DOOR_STATE'],axis=1)#删除计算后的两列
    
    #####################################################################################################
        #计算开门数据的cv值并写入数据库
        if len(b_rawdata_can_open)==0:
            pass
        else:
            b_open_cv=opendata_cv(b_rawdata_can_open,b_open_sd_model_flie,b_open_normal_model_flie)#计算所有开门数据的cv值
            for indexs in b_open_cv.index:
                for i in b_open_cv.ix[indexs].values:
                    row_cv=i
                row_id=indexs
                #print('update door_data_can0220 set CV ='+str(row_cv)+' where id = '+str(row_id))
                cur.execute('update '+database+' set CV ='+str(row_cv)+' where id = '+str(row_id))
                conn.commit()   
        #计算关门数据的cv值并写入数据库
        if len(b_rawdata_can_close)==0:#若读取进来的数据中没有关门数据
            pass
        else:
            b_close_cv=closedata_cv(b_rawdata_can_close,b_close_sd_model_flie,b_close_normal_model_flie)#计算所有关门数据的cv值
            for indexs in b_close_cv.index:
                #将计算出的cv值写入数据库cv列
                for i in b_close_cv.ix[indexs].values:
                    row_cv=i
                row_id=indexs
                #print('update door_data_can0220 set CV ='+str(row_cv)+' where id = '+str(row_id))
                cur.execute('update '+database+' set CV ='+str(row_cv)+' where id = '+str(row_id))
                conn.commit()
        print('door 1 finish')
    
    
    
        print('finish')
        time.sleep(60)#间隔一分钟          
    
        cur.close()
        conn.close()


import pandas as pd
import pymysql
#pymysql.install_as_MySQLdb()
import sklearn.mixture as mix
import numpy as np
import math
import time
import matplotlib.pyplot as plt
import seaborn as sns#添加Seaborn模块
import os
import datetime
import pickle
import joblib
from db_model import querydf
import argparse

class GMM_HS:
    def __init__(self, sql=None):
        self.df=querydf(sql)

    #计算CV值
    def calculate_cv(self,MG1,MG2):
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
                dist = self.L2Dist(Sigma1,Mu1,Sigma2,Mu2)
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
                n1 = n1 + weight * self.L2Dist(Sigma1,Mu1,Sigma2,Mu2)
        for k in range(0,NumMixture2):
            for j in range(0,NumMixture2):
                Sigma1 = MG2.covariances_[k]
                Mu1 = MG2.means_[k]
                Sigma2 = MG2.covariances_[j]
                Mu2 = MG2.means_[j]
                weight = MG2.weights_[k]*MG2.weights_[j]
                n2 = n2 + weight * self.L2Dist(Sigma1,Mu1,Sigma2,Mu2)
        cv = d/np.sqrt(n1)/np.sqrt(n2)
        return cv

    #计算两个高斯分布之间的距离
    def L2Dist(self,sigma1,mean1,sigma2,mean2):
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
        
        InnerProd = 1/(math.sqrt(2*math.pi)**n) * math.sqrt(np.linalg.det(invsigma)) * \
                    np.exp(-1/2*(-u.T*sigma1*invsigma*sigma2*u + mean1.T*invsigma1*mean1 + mean2.T*invsigma2*mean2))
        '''L2 distance between f1 and f2'''
        d = InnerProd/f1norm/f2norm
        
        return d

    #训练高斯模型
    def gmm_clustering(self,k,X,cov_type=None):
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

    def opendata_findbest(self,data_st1_sd_sps,df_name=None):
        time_start=time.time()
        #找出表现最好的行编号---开门状态
        #选取前50个点，计算cv均值
        list_findopenbest=[]
        sample_len=100
        print('open_sample_len',sample_len)
        i=0
        while len(list_findopenbest)!=sample_len:
            row_num=i
            i+=1
            k = 1
            cv1 = np.zeros(1)
            data_so = data_st1_sd_sps.copy()    
            data_s1 = data_so.iloc[row_num].copy()
            data_s1 = pd.DataFrame(data_s1)
            #print(data_so.index[row_num])

            data_s = data_st1_sd_sps.copy()

            normal_obj = self.gmm_clustering(k,data_s1)
            a = len(data_s)
            cv = np.zeros(a)

            #建立高斯混合模型
            def gmm_apply(x,k,normal_obj):
                data_l = pd.DataFrame(x)
                test_obj =self.gmm_clustering(k,data_l)
                y = calculate_cv(normal_obj,test_obj)#y为[[cv值]]，只返回cv值
                return y[0][0]

            #计算每一行的cv值，存在data_s的cv列中         
            data_s['cv']=data_s.apply(lambda row:gmm_apply(row,k,normal_obj), axis=1)

            #计算cv的均值
            cv1= data_s['cv']#cv1为Series
            #print(type(cv1))
            count =0    
            data_s['health_label']=cv1.map(count_gmm) 
            count=data_s['health_label'].sum()   
            c = cv1.mean() 
            ##########################################
            list_row=[data_so.index[row_num],a,count,c]
            list_findopenbest.append(list_row)

        df_findopenbest=pd.DataFrame(list_findopenbest,columns=['time','a', 'count', 'cv.mean'] )   
        #用cv.mean列对df进行排序
        df_openbest=df_findopenbest.sort_values(by="cv.mean" , ascending=False)#按照降序排序

        time_end=time.time()
        print('findopenbest totally cost',datetime.timedelta(seconds=time_end-time_start))
        print('df_openbest',df_openbest.head())
    ##########################################
    #     保存效果最好的模型
        data_so = data_st1_sd_sps.copy()
        best_time_df=df_openbest.iloc[[0],[0]].values
        print(best_time_df)
        for i in best_time_df:
            for j in i:
                best_time=j        
        print(best_time)
        data_s1 = data_so.loc[best_time].copy()
        data_s1 = pd.DataFrame(data_s1)
        normal_obj = self.gmm_clustering(1,data_s1)
        #保存normal_obj模型
        #保存训练好的模型文件
        dt=datetime.datetime.now()
        dt_str=self.time_to_str(dt)
        joblib.dump(normal_obj, './Models/model_{}.pkl'.format(df_name),compress=3)
    #     导入训练好的模型文件
    #     clf = joblib.load('onlycan_opendata_normal_obj_model0.pkl') 

    def load_model(self,df_std,model_path):
        k=1
        data_s=df_std
        normal_obj = joblib.load(model_path) 
        a = len(data_s)
        cv = np.zeros(a)

        #使用高斯混合模型进行计算
        def gmm_apply(x,k,normal_obj):
            data_l = pd.DataFrame(x)
            test_obj = self.gmm_clustering(k,data_l)#test_obj为训练好的gmm模型，需保存
            y = self.calculate_cv(normal_obj,test_obj)#y为[[cv值]]，只返回cv值
            return y[0][0]

        #计算每一行的cv值，存在data_s的cv列中         
        data_s['cv']=data_s.apply(lambda row:gmm_apply(row,k,normal_obj), axis=1)
        c = data_s['cv'].mean()
        data_s['health_label']=data_s['cv'].map(self.count_gmm)
        
        return data_s
    
    def visiual_cv(self,df,df_all_titlle):
        long_rolling_data_close=df['cv'].rolling(30,min_periods=1).mean()
        plt.figure(figsize=(50,15))
        long_rolling_data_close.plot()
        plt.ylim((-0.1,1.1))#确认一下
        plt.axhline(y=0.75, color='#00FF00')#画横线y=0.3
        plt.axhline(y=0.65, color='#0000FF')#画横线y=0.3
        plt.axhline(y=0.5, color='#FFFF00')#画横线y=0.3
        plt.axhline(y=0.3, color='#FF0000')#画横线y=0.3
        plt.grid()
        

    def count_gmm(self,x):
        if x > 0.75:
            return 0   #健康
        elif x>0.65:
            return 1   #亚健康
        elif x>0.5:
            return 2   #轻微故障
        elif x>0.3:
            return 3
        else: 
            return 4   #严重故障

    def time_to_str(self,dt):
        dt_str=dt.strftime('%Y-%m-%d %H:%M:%S')
        return dt_str

    
    def process_df(self,df):
        cols,drop_cols=[],[]
        if isinstance(df,pd.DataFrame):
            cols=df.columns
        if "id" in cols:
            drop_cols.append("id")
        for col in cols:
            if len(df[col].value_counts())<=1  :
                drop_cols.append(col)
        df.drop(drop_cols,axis=1,inplace=True)

        return df,drop_cols  

    def std_data(self,df):
        from sklearn import preprocessing
        df_std = preprocessing.StandardScaler().fit_transform(df)
        df_std  = pd.DataFrame(df_std)
        df_std.index=df.index
        df_std.columns=df.columns
        return df_std

    
    def result_cv(self,df,sql,UnitNo,lineNo,trainNo,path_list):
        df['HappenTime']=pd.to_datetime(df['HappenTime'])
        df=df.set_index('HappenTime')
        df,drop_cols=df.process_df(df)

        df_train=df[df['TrainNo']==trainNo & df['UnitNo']==UnitNo]

        CarriageNo_list=['MP1','MP2','TC1','M1','M2']
        df_train_MP1=df_train[df_train['CarriageNo']=='MP1']
        df_train_MP2=df_train[df_train['CarriageNo']=='MP2']
        df_train_TC1=df_train[df_train['CarriageNo']=='TC1']
        df_train_M1=df_train[df_train['CarriageNo']=='M1']
        df_train_M2=df_train[df_train['CarriageNo']=='M2']
        df_all=[df_train_MP1,df_train_MP2,df_train_TC1,df_train_M1,df_train_M2]
        df_titlle_list=['MP1','MP2','TC1','M1','M2']
        cols=df.columns
        feature_list=[]
        #3.标准化数据
        for i in range(len(CarriageNo_list)):
            df=df_all[i]
            feature=df[cols[2:]]
            df_std=gmm.std_data()
            feature_list.append(df_std)

        #4.训练并选择最优的模型
        for i in range(0,5):
            gmm.opendata_findbest(feature_list[i],df_titlle_list[i])

        #5. 加载训练好的模型
        df_list=[]

        for i in range(0,5): 
            df_list.append(gmm.load_model(feature_list[i],path_list[i]))
        

    
if __name__=="__main__":
    # 1.设置动态参数
    parser=argparse.ArgumentParser(description='Train Health AssessMent')
    parser.add_argument('--UnitNo',type=str,default='1#',help='Air Condition Unit Number',choices=['1#','2#'])
    parser.add_argument('--lineNo',type=str,default='5L',help='Subway Line Number')
    parser.add_argument('--trainNo',type=str,default='534',help='Subway Train Number')

    args = parser.parse_args()

    path_list=['./Models/model_df_train_M1.pkl','./Models/model_df_train_M2.pkl','./Models/model_df_train_MP1.pkl','./Models/model_df_train_MP2.pkl','./Models/model_df_train_TC1.pkl']
    # 2.获取数据
    database='condition_data'
    sql="select * from "+database #  read_flag is nulland 
    gmm=GMM_HS(sql)
    df=gmm.df
    gmm.result_cv(df,sql,args.UnitNo,args.lineNo,args.trainNo,path_list)

    


    


    
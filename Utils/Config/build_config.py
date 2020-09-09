import configparser #引入模块
import os
# 参考:https://www.cnblogs.com/plf-Jack/p/11170284.html

config = configparser.ConfigParser()    #类中一个方法 #实例化一个对象

config["mysql_db"] = {'username': 'root',
                      'passwd': '7515',
                      'host':'localhost',
                     'db': 'air_condition',
                     'raw_data_tb':'condition_data',
                     'alarm_tb':'alarm_log'
                     }	#类似于操作字典的形式

config['model_name'] = {'model_M1':'model_df_train_M1.pkl',
                        'model_M2':'model_df_train_M2.pkl',
                        'model_MP1':'model_df_train_MP1.pkl',
                        'model_MP2':'model_df_train_MP2.pkl',
                        'model_TC1':'model_df_train_TC1.pkl',
                        } #类似于操作字典的形式

config['Default_info'] = {'TrainNo':'534',
                        'CarrageNo':'M1',
                        'dt':'2020-09-09 13:48:00',
                        'lineNo':'5L',
                        'UnitNo':'#1',
                        'model_path':'model_df_train_M1.pkl',
                        } #类似于操作字典的形式



# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}

root_path=os.path.join(os.getcwd(),"Utils","Config")
path=os.path.join(root_path,"config.ini")

with open(path, 'w') as configfile:
   config.write(configfile)	#将对象写入文件
import configparser
import os


#************************************Read Config**************************************
config = configparser.ConfigParser()

#---------------------------查找文件内容,基于字典的形式
root_path=os.path.join(os.getcwd(),"Utils","Config")
path=os.path.join(root_path,"config.ini")

config.read(path)

print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']

print('mysql_db' in config) # False

print(config['mysql_db']["username"])  # Atlan


for key in config['mysql_db']:     
    print(key)

print(config.options('mysql_db'))  # 同for循环,找到'mysql_db'下所有键

print(config.items('mysql_db'))    #找到'mysql_db'下所有键值对

print(config.get('mysql_db','alarm_tb')) # get方法mysql_db下的key对应的value

#************************************End*************************************************



#************************************Modify Config**************************************


# import configparser

# config = configparser.ConfigParser()
# root_path=os.path.join(os.getcwd(),"Utils","Config")
# config_path=os.path.join(root_path,"config.ini")

# config.read(config_path)  #读文件

# config.add_section('yuan')  #添加section

# config.remove_section('yuan') #删除section
# config.remove_option('mysql_db',"root") #删除一个配置想

# config.set('mysql_db','host','127.0.0.1')
# with open('new2.ini','w') as f:
#      config.write(f)
#************************************End*************************************************
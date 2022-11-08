# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个工具辅助模块
"""
模块介绍
-------

这是一个工具辅助模块

设计模式：

    （1）  无 

关键点：    

    （1）MongoDB信息管理

主要功能：            

    （1）MongoDB管理JSON                                

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import pymongo



####### MongoDB信息管理模型 ##################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）MongoDB信息管理                                                 ###
### 主要功能：                                                           ###
### （1）MongoDB管理JSON                                                 ###
############################################################################


####### MongoDB信息管理模型 #############################################################################
########################################################################################################



class MongoManager(object):
    '''
    类介绍：

        这是一个MongoDB数据库连接管理类
    '''


    def __init__(self,host,port,username,password,database,collection):
        '''
        属性功能：

            定义一个汇总数据库基本信息的属性方法

        参数:
            host (str): mongodb的ip地址
            port (int): mongodb的端口
            username (str): mongodb的用户名
            password (str): mongodb的密码
            database (str): 数据库名称
            collection (str): 集合名称
            client (object): mongodb客户端对象

        返回：
            无
        '''

        self.host = host
        self.port = port 
        self.username = username
        self.password = password
        self.database = database
        self.collection = collection
        self.client = self.create_mongodb_client()


    def create_mongodb_client(self):
        '''
        方法功能：

            定义一个连接mongodb的方法，从MongoManager实例参数中获取方法

        参数：
            无

        返回：
            mongodb_collection (object): mongodb客户端对象-mongodb集合
        '''

        mongodb_client = pymongo.MongoClient(host=self.host,port=self.port,username=self.username,password=self.password)
        mongodb_database = mongodb_client[self.database]
        database_list = mongodb_client.list_database_names()
        if self.database not in database_list: ### 执行数据库操作前，需要判断数据库是否存在
            mongodb_database.create_collection(self.collection)
        mongodb_collection = mongodb_database[self.collection]
        print('=============================>>>>>> fiche info {} create well done!'.format(self.collection))

        return mongodb_collection


    def insert_info(self,info_dict_list):
        '''
        方法功能：

            定义一个插入信息json串的方法

        参数：
            info_dict_list (list): 信息字典列表 

        返回：
            result (str): 插入成功信息
        '''

        self.client.insert_many(info_dict_list)
        result = "=============>>>>>> fiche info insert well done!"
        print(result)

        return result


    def update_info(self,query,update):
        '''
        方法功能：

            定义一个更新信息json串的方法

        参数：
            query (dict): mongodb查询字典
            update (dict): mongodb更新字典 

        返回：
            result (str): 更新成功信息
        '''

        self.client.update_many(query,update) 
        result = "=============>>>>>> fiche info update well done!"
        print(result)

        return result


    def query_info(self,query,view_index = 0):
        '''
        方法功能：

            定义一个查询信息json串的方法

        参数：
            query (dict): mongodb查询字典 

        返回：
            result_iter (object): 查询结果
        '''

        result_iter = self.client.find(query,projection={'_id': False})### 使用保护机制引入{'_id':false})来去除id额外索引
        result = "=============>>>>>> fiche info query well done!"
        print(result)

        return result_iter[view_index]       


    def delete_info(self,query):
        '''
        方法功能：

            定义一个删除信息json串的方法

        参数：
            query (dict): mongodb查询字典 

        返回：
            result (str): 删除成功信息
        '''

        self.client.delete_many(query)
        result = "=============>>>>>> fiche info delete well done!"
        print(result)

        return result         



##############################################################################################
##############################################################################################



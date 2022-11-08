# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个fiche对外接口类，主要功能整理各种信息处理操作
"""
模块介绍
-------

这是一个fiche对外接口类，主要功能整理各种信息处理操作

设计模式：

    （1）  无 

关键点：    

    （1）信息处理

主要功能：            

    （1）整理各种信息处理操作                        

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fiche.observer_mode import *
from fiche.cons import *



####### 观察者模式类 ########################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）信息处理                                                        ###
### 主要功能：                                                           ###
### （1）整理各种信息处理操作                                              ###
############################################################################


####### 信息处理操作 ###############################################################
###################################################################################



class FicheData(object):
    '''
    类介绍：

        这是一个fiche整理各种信息处理操作的接口类
    '''


    def __init__(self,host,username,password,port=27017,database='fiche'):### 默认参数放到最后
        '''
        属性功能：

            定义一个初始化属性功能的方法

        参数：
            host (str): mongodb的host
            port (int): mongodb的port，默认27017
            username (str): mongodb的用户名
            password (str): mongodb的密码
            database (str): mongodb中fiche对应的数据库
        返回：
            fichedata (object): fichedata实例
        '''

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database


    def add_observer(self,                     
                     observer_name,
                     observer_version,
                     observer_summary='default summary',
                     observer_config='default config',
                     observer_remark='default remark'):
        '''
        方法功能：

            定义一个添加观察者的方法

        参数：
            observer_name (str): 观察者名称
            observer_version (str): 观察者版本
            observer_summary (str): 观察者简述
            obserser_config (str): 观察者配置
            observer_remark (str): 观察者备注

        返回：
            result (str): 结果信息
        '''

        ### fiche存储--observer_info
        fiche_observer_info_storage = MongoManager(host=self.host,
                                                   port=self.port,
                                                   username=self.username,
                                                   password=self.password,
                                                   database=self.database,
                                                   collection='observer_info')                                   
        ### 添加观察者
        Observable.add_observer(storage=fiche_observer_info_storage,
                                observer_name=observer_name,
                                observer_version=observer_version,
                                observer_summary=observer_summary,
                                observer_config=observer_config,
                                observer_remark=observer_remark)     


    def remove_observer(self,observer_name,observer_version):
        '''
        方法功能：

            定义一个删除观察者的方法

        参数：
            observer_name (str): 观察者名称
            observer_version (str): 观察者版本

        返回：
            result (str): 结果信息
        '''                  

        ### fiche存储--observer_info
        fiche_observer_info_storage = MongoManager(host=self.host,
                                                   port=self.port,
                                                   username=self.username,
                                                   password=self.password,
                                                   database=self.database,
                                                   collection='observer_info')
        ### 删除观察者
        Observable.remove_observer(storage=fiche_observer_info_storage,
                                   observer_name=observer_name,
                                   observer_version=observer_version)    


    def show_obervers(self):
        '''
        方法功能：

            定义一个获取观察者的方法

        参数：
            无

        返回：
            observers_list (list): 观察者列表
        '''

        ### fiche存储--observer_info
        fiche_observer_info_storage = MongoManager(host=self.host,
                                                   port=self.port,
                                                   username=self.username,
                                                   password=self.password,
                                                   database=self.database,
                                                   collection='observer_info')
        ### 展示观察者
        observers_list = Observable.get_observers(storage=fiche_observer_info_storage)

        return observers_list      


    def query_observer_info(self,observer_name,observer_version):
        '''
        方法功能：

            定义一个查询观察者信息的方法

        参数：
            observer_name (str): 观察者名称
            observer_version (str): 观察者版本

        返回：
            observer_info_query (dict): 查询信息字典
        '''                                         

        ### fiche存储--observer_info
        fiche_observer_info_storage = MongoManager(host=self.host,
                                                   port=self.port,
                                                   username=self.username,
                                                   password=self.password,
                                                   database=self.database,
                                                   collection='observer_info')
        ### 查询observer_info
        observer_info_query = fiche_observer_info_storage.query_info({'name':observer_name,'version':observer_version})                                                                
        
        return observer_info_query


    def save_algorithm_info(self,
                            name,
                            version,
                            summary,
                            config,
                            remark,
                            homepage,
                            author,
                            authoremail,
                            license,
                            requires,
                            requiredby):
        '''
        方法功能：

            定义一个保存算法包信息方法

        参数：
            name (str): 算法包名称
            version (str): 版本
            summary (str): 简述
            config (str): 配置指导
            ramark (str): 备注
            homepage (str): 官方文档
            author (str): 作者
            authoremail (str): 作者邮箱
            license (str): 开源协议
            requires (str): 依赖
            requiredby (str): 被依赖
        
        返回：
            无
        '''                    

        ### fiche存储--algorithm_info
        fiche_algorithm_info_storage = MongoManager(host=self.host,
                                                    port=self.port,
                                                    username=self.username,
                                                    password=self.password,
                                                    database=self.database,
                                                    collection='algorithm_info')                
        ### 算法包信息
        tmp_algorithm_info = Algorithm_Info(name = name,
                                            version = version,
                                            summary = summary,
                                            config = config,
                                            remark = remark,
                                            homepage = homepage,
                                            author = author,
                                            authoremail = authoremail,
                                            license = license,
                                            requires = requires,
                                            requiredby = requiredby)
        tmp_algorithm_info.save(storage=fiche_algorithm_info_storage)   


    def query_algorithm_info(self,algorithm_name,algorithm_version):
        '''
        方法功能：

            定义一个查询算法信息的方法

        参数：
            algorithm_name (str): 算法名称
            algorithm_version (str): 算法版本

        返回：
            algorithm_info_query (dict): 查询信息字典
        '''                                         

        ### fiche存储--algorithm_info
        fiche_algorithm_info_storage = MongoManager(host=self.host,
                                                    port=self.port,
                                                    username=self.username,
                                                    password=self.password,
                                                    database=self.database,
                                                    collection='algorithm_info')
        ### 查询algorithm_info
        algorithm_info_query = fiche_algorithm_info_storage.query_info({'name':algorithm_name,'version':algorithm_version})                                                                
        
        return algorithm_info_query


    def save_model_info(self,
                        name,
                        version,
                        summary,
                        config,
                        remark,
                        requires,
                        data,
                        algorithm):
        '''
        方法功能：

            定义一个保存模型信息的方法

        参数:
            name (str): 算法包名称
            version (str): 版本
            summary (str): 简述
            data (str): 依赖数据
            algorithm (str): 依赖算法
            requires (str): 依赖
            config (str): 配置
            remark (str): 备注    

        返回：
            无        
        '''

        ### fiche存储--model_info
        fiche_model_info_storage = MongoManager(host=self.host,
                                                port=self.port,
                                                username=self.username,
                                                password=self.password,
                                                database=self.database,
                                                collection='model_info')
        ### 模型信息
        tmp_model_info = Model_Info(name = name,
                                    version = version,
                                    summary = summary,
                                    config = config,
                                    remark = remark,
                                    requires = requires,
                                    data = data,
                                    algorithm = algorithm)
        tmp_model_info.save(storage=fiche_model_info_storage)                                            


    def query_model_info(self,model_name,model_version):
        '''
        方法功能：

            定义一个查询模型信息的方法

        参数：
            model_name (str): 模型名称
            model_version (str): 模型版本

        返回：
            model_info_query (dict): 查询信息字典
        '''                                         

        ### fiche存储--model_info
        fiche_model_info_storage = MongoManager(host=self.host,
                                                port=self.port,
                                                username=self.username,
                                                password=self.password,
                                                database=self.database,
                                                collection='model_info')
        ### 查询model_info
        model_info_query = fiche_model_info_storage.query_info({'name':model_name,'version':model_version})                                                                
        
        return model_info_query


    def save_parameter_info(self,
                            name,
                            version,
                            summary,
                            config,
                            remark,
                            datatype,
                            requiredby):
        '''
        方法功能：

            定义一个保存参数信息的方法
        
        参数：
            name (str): 算法包名称
            version (str): 版本
            summary (str): 简述
            config (str): 配置指导
            remark (str): 备注
            datatype (str): 类型
            requiredby (str): 被依赖 

        返回：
            无
        '''                            

        ### fiche存储--parameter_info
        fiche_parameter_info_storage = MongoManager(host=self.host,
                                                    port=self.port,
                                                    username=self.username,
                                                    password=self.password,
                                                    database=self.database,
                                                    collection='parameter_info')
        ### 参数信息
        tmp_parameter_info = Parameter_Info(name = name,
                                            version = version,
                                            summary = summary,
                                            config = config,
                                            remark = remark,
                                            datatype = datatype,
                                            requiredby = requiredby)
        tmp_parameter_info.save(storage=fiche_parameter_info_storage)                                                    


    def query_parameter_info(self,parameter_name,parameter_version):
        '''
        方法功能：

            定义一个查询参数信息的方法

        参数：
            parameter_name (str): 参数名称
            parameter_version (str): 参数版本

        返回：
            parameter_info_query (dict): 查询信息字典
        '''                                         

        ### fiche存储--parameter_info
        fiche_parameter_info_storage = MongoManager(host=self.host,
                                                    port=self.port,
                                                    username=self.username,
                                                    password=self.password,
                                                    database=self.database,
                                                    collection='parameter_info')
        ### 查询parameter_info
        parameter_info_query = fiche_parameter_info_storage.query_info({'name':parameter_name,'version':parameter_version})                                                                
        
        return parameter_info_query


    def save_application_info(self,
                              name,
                              version,
                              summary,
                              config,
                              remark,
                              requires,
                              project):
        '''
        方法功能：

            定义一个保存应用信息的方法

        参数：
            name (str): 算法包名称
            version (str): 版本
            summary (str): 简述
            config (str): 配置指导
            ramark (str): 备注
            requires (str): 依赖
            project (str): 项目              
        
        返回：
            无
        '''        

        ### fiche存储--application_info
        fiche_application_info_storage = MongoManager(host=self.host,
                                                      port=self.port,
                                                      username=self.username,
                                                      password=self.password,
                                                      database=self.database,
                                                      collection='application_info')
        ### 应用信息
        tmp_application_info = Application_Info(name = name,
                                                version = version,
                                                summary = summary,
                                                config = config,
                                                remark = remark,
                                                requires = requires,
                                                project = project)
        tmp_application_info.save(storage=fiche_application_info_storage)                                                     


    def query_application_info(self,application_name,application_version):
        '''
        方法功能：

            定义一个查询应用信息的方法

        参数：
            application_name (str): 应用名称
            application_version (str): 应用版本

        返回：
            application_info_query (dict): 查询信息字典
        '''                                         

        ### fiche存储--application_info
        fiche_application_info_storage = MongoManager(host=self.host,
                                                    port=self.port,
                                                    username=self.username,
                                                    password=self.password,
                                                    database=self.database,
                                                    collection='application_info')
        ### 查询application_info
        application_info_query = fiche_application_info_storage.query_info({'name':application_name,'version':application_version})                                                                
        
        return application_info_query


    def save_dataset_info(self,
                          name,
                          version,
                          summary,
                          config,
                          remark,
                          requiredby,
                          datatype,
                          project):
        '''
        方法功能：

            定义一个保存数据集信息的方法

        参数：
            name (str): 算法包名称
            version (str): 版本
            summary (str): 简述
            config (str): 配置指导
            remark (str): 备注
            requiredby (str): 被依赖
            datatype (str): 数据类型
            project (str): 项目 

        返回：
            无
        '''   

        ### fiche存储--dataset_info
        fiche_dataset_info_storage = MongoManager(host=self.host,
                                                  port=self.port,
                                                  username=self.username,
                                                  password=self.password,
                                                  database=self.database,
                                                  collection='dataset_info')     
        ### 数据集信息
        tmp_dataset_info = Dataset_Info(name = name,
                                        version = version,
                                        summary = summary,
                                        config = config,
                                        remark = remark,
                                        requiredby = requiredby,
                                        datatype = datatype,
                                        project = project)
        tmp_dataset_info.save(storage=fiche_dataset_info_storage)                                                


    def query_dataset_info(self,dataset_name,dataset_version):
        '''
        方法功能：

            定义一个查询应用信息的方法

        参数：
            dataset_name (str): 应用名称
            dataset_version (str): 应用版本

        返回：
            dataset_info_query (dict): 查询信息字典
        '''                                         

        ### fiche存储--application_info
        fiche_dataset_info_storage = MongoManager(host=self.host,
                                                    port=self.port,
                                                    username=self.username,
                                                    password=self.password,
                                                    database=self.database,
                                                    collection='dataset_info')
        ### 查询dataset_info
        dataset_info_query = fiche_dataset_info_storage.query_info({'name':dataset_name,'version':dataset_version})                                                                
        
        return dataset_info_query       



############################################################################################################################################
############################################################################################################################################



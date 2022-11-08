# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个fiche服务应用路由类，主要使用fastspi搭建ASGI服务器
"""
模块介绍
-------

这是一个fiche服务应用路由类，主要使用fastspi搭建ASGI服务器

设计模式：

    无

关键点：    

    （1）fastapi

主要功能：            

    （1）fiche服务应用路由
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fiche.data import *
from fiche.cons import fiche_config_yaml
from fastapi import FastAPI
import uvicorn
from fastapi import APIRouter



####### fiche服务应用路由 ###################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）fastapi                                                          ###
### 主要功能：                                                            ###
### （1）fiche服务应用路由                                                 ###
############################################################################



####### fiche服务观察者路由 ###########################################################################
######################################################################################################



observer_router = APIRouter()


### 增加观察者路由
@observer_router.get("/add_observer")
async def add_observer(observer_name,observer_version):
    '''
    函数功能：

        定义一个添加观察者信息的函数

    参数：
        observer_name (str): 观察者名称
        observer_version (str): 观察者版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])
    ### 执行增加观察者操作                      
    fiche.add_observer(observer_name=observer_name,observer_version=observer_version)
    result = {'info':'Add observer well done!'}

    return result


### 查询观察者
@observer_router.get("/query_observer")
async def query_observer(observer_name,observer_version):
    '''
    函数功能：

        定义一个查询观察者信息的函数

    参数：
        observer_name (str): 观察者名称
        observer_version (str): 观察者版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])
    ### 执行查询观察者操作                      
    tmp_observer_info_query = fiche.query_observer_info(observer_name=observer_name,observer_version=observer_version)
    result = {'data':tmp_observer_info_query}

    return result


### 删除观察者    
@observer_router.get("/remove_observer")
async def remove_observer(observer_name,observer_version):
    '''
    函数功能：

        定义一个删除观察者信息的函数

    参数：
        observer_name (str): 观察者名称
        observer_version (str): 观察者版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])
    ### 执行删除观察者操作
    fiche.remove_observer(observer_name=observer_name,observer_version=observer_version)
    result = {'info':'{}--{} Remove observer well done!'.format(observer_name,observer_version)}

    return result                          



####### fiche服务各个信息管理路由 ###########################################################################
######################################################################################################


info_manager_router = APIRouter()


### 保存算法信息
@info_manager_router.get("/save_algorithm_info")
async def save_algorithm_info(name,version,summary,config,remark,homepage,author,authoremail,license,requires,requiredby):
    '''
    函数功能：

        定义一个保存算法信息的函数

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
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])
    ### 保存算法信息
    fiche.save_algorithm_info(name=name,
                              version=version,
                              summary=summary,
                              config=config,
                              remark=remark,
                              homepage=homepage,
                              author=author,
                              authoremail=authoremail,
                              license=license,
                              requires=requires,
                              requiredby=requiredby)
    result = {'info':'Save algorithm info well done!'}

    return result                      


### 查询算法信息
@info_manager_router.get("/query_algorithm_info")
async def query_algorithm_info(algorithm_name,algorithm_version):
    '''
    函数功能：

        定义一个查询算法信息的函数

    参数：
        algorithm_name(str): 算法名称
        algorithm_version(str): 算法版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])
    ### 查询算法信息
    tmp_algorithm_info_query = fiche.query_algorithm_info(algorithm_name=algorithm_name,algorithm_version=algorithm_version)           
    result = {'data':tmp_algorithm_info_query}

    return result


### 保存模型信息
@info_manager_router.get("/save_model_info")
async def save_model_info(name,version,summary,config,remark,requires,data,algorithm):
    '''
    函数功能：

        定义一个保存模型信息的函数

    参数：
        name (str): 算法包名称
        version (str): 版本
        summary (str): 简述
        data (str): 依赖数据
        algorithm (str): 依赖算法
        requires (str): 依赖
        config (str): 配置
        remark (str): 备注

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])
    ### 保存模型信息
    fiche.save_model_info(name=name,
                          version=version,
                          summary=summary,
                          config=config,
                          remark=remark,
                          requires=requires,
                          data=data,
                          algorithm=algorithm)
    result = {'info':'Save model info well done!'}

    return result


### 查询模型信息
@info_manager_router.get("/query_model_info")
async def query_model_info(model_name,model_version):
    '''
    函数功能：

        定义一个查询模型信息的函数

    参数：
        model_name (str): 模型名称
        model_version (str): 模型版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])   
    ### 查询模型信息
    tmp_model_info_query = fiche.query_model_info(model_name=model_name,model_version=model_version)
    result = {'data':tmp_model_info_query}

    return result                                                 


### 保存参数信息
@info_manager_router.get("/save_parameter_info")
async def save_parameter_info(name,version,summary,config,remark,datatype,requiredby):
    '''
    函数功能：

        定义一个保存参数信息的函数

    参数：
        name (str): 算法包名称
        version (str): 版本
        summary (str): 简述
        config (str): 配置指导
        remark (str): 备注
        datatype (str): 类型
        requiredby (str): 被依赖

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database']) 
    ### 保存参数信息
    fiche.save_parameter_info(name=name,
                              version=version,
                              summary=summary,
                              config=config,
                              remark=remark,
                              datatype=datatype,
                              requiredby=requiredby)
    result = {'info':'Save parameter info well done!'}

    return result             


### 查询参数信息
@info_manager_router.get("/query_parameter_info")
async def query_parameter_info(parameter_name,parameter_version):
    '''
    函数功能：

        定义一个查询参数信息的函数

    参数：
        parameter_name (str): 参数名称
        parameter_version (str): 参数版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database'])
    ### 查询参数信息
    tmp_parameter_info_query = fiche.query_parameter_info(parameter_name=parameter_name,parameter_version=parameter_version)                                           
    result = {'data':tmp_parameter_info_query}

    return result


### 保存应用信息
@info_manager_router.get("/save_application_info")
async def save_application_info(name,version,summary,config,remark,requires,project):
    '''
    函数功能：

        定义一个保存应用信息的函数

    参数：
        name (str): 算法包名称
        version (str): 版本
        summary (str): 简述
        config (str): 配置指导
        remark (str): 备注
        requires (str): 依赖
        project (str): 项目 

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database']) 
    ### 保存应用信息
    fiche.save_application_info(name=name,
                                version=version,
                                summary=summary,
                                config=config,
                                remark=remark,
                                requires=requires,
                                project=project)
    result = {'info':'Save application info well done!'}

    return result


### 查询应用信息
@info_manager_router.get("/query_application_info")
async def query_application_info(application_name,application_version):
    '''
    函数功能：

        定义一个查询应用信息的函数

    参数：
        application_name (str): 应用名称
        application_version (str): 应用版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database']) 
    ### 查询应用信息
    tmp_application_info_query = fiche.query_application_info(application_name=application_name,application_version=application_version)
    result = {'data':tmp_application_info_query}

    return result


### 保存数据信息
@info_manager_router.get("/save_dataset_info")
async def save_dataset_info(name,version,summary,config,remark,requiredby,datatype,project):
    '''
    函数功能：

        定义一个保存数据信息的函数

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
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database']) 
    ### 保存数据信息
    fiche.save_dataset_info(name=name,
                            version=version,
                            summary=summary,
                            config=config,
                            remark=remark,
                            requiredby=requiredby,
                            datatype=datatype,
                            project=project)    
    result = {'info':'Save dataset info well done!'}

    return result


### 查询数据信息
@info_manager_router.get("/query_dataset_info")
async def query_dataset_info(dataset_name,dataset_version):
    '''
    函数功能：

        定义一个查询数据信息的函数

    参数：
        dataset_name (str): 数据名称
        dataset_version (str): 数据版本

    返回：
        result (json): json结果字符串
    '''

    ### 从fiche的yaml配置文件中加载参数，并获得fiche的数据接口实例
    fiche = FicheData(host=fiche_config_yaml['host'],
                      port=fiche_config_yaml['port'],
                      username=fiche_config_yaml['username'],
                      password=fiche_config_yaml['password'],
                      database=fiche_config_yaml['database']) 
    ### 查询数据信息
    tmp_dataset_info_query = fiche.query_dataset_info(dataset_name=dataset_name,dataset_version=dataset_version)
    result = {'data':tmp_dataset_info_query}

    return result



###### fiche服务应用主路由 #################################################################################################################################
###########################################################################################################################################################



### 创建fastapi应用实例
app = FastAPI()
app.include_router(observer_router,prefix="/observer",tags=['observer'])
app.include_router(info_manager_router,prefix="/info_manager",tags=['info_manager'])



if __name__ == '__main__':
    uvicorn.run(app='service:app',host='0.0.0.0',port=11811,reload=True,debug=True) ### app参数需要使用字符串格式的时候，才可以添加reload和debug参数



##########################################################################################################################################################
##########################################################################################################################################################
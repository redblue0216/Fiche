# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个具体数据模型类整理模块
"""
模块介绍
-------

这是一个具体数据模型类整理模块

设计模式：

    （1）  无 

关键点：    

    （1）fiche具体数据模型类整理

主要功能：            

    （1）fiche具体数据模型类整理                                

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fiche.orm import *
from fiche.util import *
import yaml
import fiche as fc



####### fiche具体数据模型类整理 ##############################################
### 设计模式：                                                            ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）fiche具体数据模型类整理                                          ###
### 主要功能：                                                           ###
### （1）fiche具体数据模型类整理                                          ###
############################################################################



####### fiche 元数据配置信息管理 #########################################################################
########################################################################################################



### 锁定包路径---->>进入路径开启yaml配置文件---->>解析yaml文件
fiche_package_path = fc.__file__.replace('__init__.py','')
fiche_config_file = open('{}fiche_config.yaml'.format(fiche_package_path),encoding='UTF-8')
fiche_config_yaml = yaml.load(fiche_config_file,Loader=yaml.FullLoader)



####### fiche具体数据模型类 #############################################################################
########################################################################################################



### 观察者信息
class Observer_Info(Models):
    '''
    类介绍：

        这是一个观察者信息的数据模型

    属性功能：
        name (str): 观察者名称
        state (str): 观察者状态
        summary (str): 简述
        config (str): 配置信息
        remark (str): 备注
    ''' 


    name = TagsField(name='name',tag_key=True)
    version = TagsField(name='version',tag_key=False)
    summary = TagsField(name='summary',tag_key=False)
    config = TagsField(name='config',tag_key=False)
    remark = TagsField(name='remark',tag_key=False)



###  算法包信息
class Algorithm_Info(Models):
    '''
    类介绍：

        这是一个算法包信息的数据模型

    属性功能：
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
    '''


    name = TagsField(name='name',tag_key=True)
    version = TagsField(name='version',tag_key=True)
    summary = TagsField(name='summary',tag_key=False)
    config = TagsField(name='config',tag_key=False)
    remark = TagsField(name='remark',tag_key=False)
    homepage = TagsField(name='homepage',tag_key=False)
    author = TagsField(name='author',tag_key=False)
    authoremail = TagsField(name='authoremail',tag_key=False)
    license = TagsField(name='license',tag_key=False)
    requires = TagsField(name='requires',tag_key=False)
    requiredby = TagsField(name='requiredby',tag_key=False)



### 模型信息
class Model_Info(Models):
    '''
    类介绍：

        这是一个模型信息的数据模型

    属性功能：
        name (str): 算法包名称
        version (str): 版本
        summary (str): 简述
        data (str): 依赖数据
        algorithm (str): 依赖算法
        requires (str): 依赖
        config (str): 配置
        remark (str): 备注
    '''


    name = TagsField(name='name',tag_key=True)
    version = TagsField(name='version',tag_key=True)
    summary = TagsField(name='summary',tag_key=False)
    config = TagsField(name='config',tag_key=False)
    remark = TagsField(name='remark',tag_key=False)
    requires = TagsField(name='requires',tag_key=False)
    data = TagsField(name='data',tag_key=False)
    algorithm = TagsField(name='algorithm',tag_key=False)



### 参数信息
class Parameter_Info(Models):
    '''
    类介绍：

        这是一个参数信息的数据模型

    属性功能：
        name (str): 算法包名称
        version (str): 版本
        summary (str): 简述
        config (str): 配置指导
        remark (str): 备注
        datatype (str): 类型
        requiredby (str): 被依赖
    '''


    name = TagsField(name='name',tag_key=True)
    version = TagsField(name='version',tag_key=True)
    summary = TagsField(name='summary',tag_key=False)
    config = TagsField(name='config',tag_key=False)
    remark = TagsField(name='remark',tag_key=False)
    datatype = TagsField(name='datatype',tag_key=False)
    requiredby = TagsField(name='requiredby',tag_key=False)



### 应用信息
class Application_Info(Models):
    '''
    类介绍：

        这是一个应用信息的数据模型

    属性功能：
        name (str): 算法包名称
        version (str): 版本
        summary (str): 简述
        config (str): 配置指导
        remark (str): 备注
        requires (str): 依赖
        project (str): 项目        
    '''


    name = TagsField(name='name',tag_key=True)
    version = TagsField(name='version',tag_key=True)
    summary = TagsField(name='summary',tag_key=False)
    config = TagsField(name='config',tag_key=False)
    remark = TagsField(name='remark',tag_key=False)
    requires = TagsField(name='requires',tag_key=False)
    project = TagsField(name='project',tag_key=False)



### 数据集信息
class Dataset_Info(Models):
    '''
    类介绍；

        这是一个数据集信息的数据模型

    属性功能：
        name (str): 算法包名称
        version (str): 版本
        summary (str): 简述
        config (str): 配置指导
        remark (str): 备注
        requiredby (str): 被依赖
        datatype (str): 数据类型
        project (str): 项目        
    '''


    name = TagsField(name='name',tag_key=True)
    version = TagsField(name='version',tag_key=True)
    summary = TagsField(name='summary',tag_key=False)
    config = TagsField(name='config',tag_key=False)
    remark = TagsField(name='remark',tag_key=False)
    requiredby = TagsField(name='requiredby',tag_key=False)
    datatype = TagsField(name='datatype',tag_key=False)
    project = TagsField(name='project',tag_key=False)    

    

###################################################################################################################
###################################################################################################################



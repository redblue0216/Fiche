# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个观察者模式类，主要采用推模型的功能设计。
"""
模块介绍
-------

这是一个观察者模式类，主要采用推模型的功能设计。

设计模式：

    （1）  无 

关键点：    

    （1）观察者模式

主要功能：            

    （1）主从节点信息管理                                 

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractclassmethod
from fiche.cons import *



####### 观察者模式类 ########################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）观察者模式                                                      ###
### 主要功能：                                                           ###
### （1）主从节点信息管理                                                 ###
############################################################################


####### 观察者类 ###############################################################
###############################################################################



class Observer(metaclass = ABCMeta):
    '''
    类介绍：

        这是一个观察者类，主要功能用于接受master节点发送的通知并处理，主要技术抽象方法
    '''

    @abstractclassmethod
    def update(self):
        '''
        方法功能：

            定义一个更新观察者的抽象方法
        '''

        pass



####### 被观察者类 #################################################################
###################################################################################



class Observable(object):
    '''
    类介绍：

        这是一个被观察者类，主要功能管理观察者、向观察者下发通知、与元数据信息管理通信。主要技术类继承。
    '''


    @staticmethod
    def add_observer(storage,
                     observer_name,
                     observer_version,
                     observer_summary='default summary',
                     observer_config='default config',
                     observer_remark='default remark'):
        '''
        方法功能：

            定义一个添加观察者的方法

        参数：
            storage (object): 存储对象MongoDB
            observer_name (str): 观察者名称
            observer_version (str): 观察者版本
            observer_summary (str): 观察者简述
            obserser_config (str): 观察者配置
            observer_remark (str): 观察者备注

        返回：
            result (str): 结果信息
        '''

        ### 整理观察者信息
        tmp_observer_info = Observer_Info(name = observer_name,
                                          version = observer_version,
                                          summary = observer_summary,
                                          config = observer_config,
                                          remark = observer_remark)
        ### 向主节点保存观察者信息                                          
        tmp_observer_info.save(storage=storage)
        ### 执行结果信息
        result = '{} add well done!'.format(observer_name)
        print(result)

        return result


    @staticmethod
    def remove_observer(storage,observer_name,observer_version):
        '''
        方法功能：

            定义一个删除观察者的方法

        参数：
            storage (object): 存储对象MongoDB 
            observer_name (str): 观察者名称
            observer_version (str): 观察者版本

        返回：
            result (str): 结果信息
        '''

        ### 配置要删除的观察者参数
        tmp_delete_query = {'name':observer_name,'version':observer_version}
        ### 删除指定观察者
        storage.delete_info(tmp_delete_query)
        result = '{}--{}remove well done!'.format(observer_name,observer_version)
        print(result)

        return result


    @staticmethod
    def get_observers(storage):
        '''
        方法功能：

            定义一个获取观察者的方法

        参数：
            storage (object): 存储对象MongoDB

        返回：
            observers_list (list): 观察者列表
        '''

        ### 获取mongodb观察者迭代对象
        observers_iter = storage.client.find()
        ### 整理观察者列表，包括去重操作
        observers_list = []         
        for i in observers_iter:
            observers_list.append((i['name'],i['version']))
        observers_list = list(set(observers_list))

        return observers_list


    @staticmethod
    def update_observer(*args,**kwargs):
        '''
        方法功能：

            定义一个更新观察者的方法，暂时不提供。

        参数：
            observer_name (str): 观察者名称
            oberver_version (str): 观察者版本

        返回：
            result (str): 结果信息
        '''

        pass


    @staticmethod
    def notify_observer(*args,**kwargs):
        '''
        方法功能：

            定义一个通知观察者的方法，暂时不提供。

        参数：
            observer_name (str): 观察者名称

        返回：
            result (str): 结果信息
        '''

        pass



#################################################################################################
#################################################################################################



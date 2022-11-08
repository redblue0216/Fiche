# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个MongoDB专属的ORM模型基础模块
"""
模块介绍
-------

这是一个MongoDB专属的ORM模型基础模块

设计模式：

    （1）  无 

关键点：    

    （1）type与__new__技术

主要功能：            

    （1）MongoDB专属ORM模型                                   

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fiche.util import *
import datetime



####### InfluxDBORM模型类 ##################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）type与__new__技术                                               ###
### 主要功能：                                                           ###
### （1）MongoDB专属ORM模型                                              ###
############################################################################


####### 数据类型类 #############################################################
###############################################################################



class Field(object):
    """
    类介绍：

        这是一个数据模型中的表达数据变量类型的基础类
    """


    def __init__(self,name,field_type,tag_key,default):
        """
        属性功能：

            定义一个初始化属性的方法

        参数：
            name (str): 数据类型名称
            field_type (str): 数据类型
            tag_key （bool): 是否是标签数据类型
            default (obj): 默认值
        """

        self.name = name
        self.field_type = field_type
        self.tag_key = tag_key
        self.default = default



class FieldsField(Field):
    """
    类介绍：

        这是一个数据模型中的表达fields数据变量类型的基础类
    """    


    def __init__(self,name,field_type = 'all',tag_key = False,default = None):
        """
        属性功能：

            定义一个初始化属性的方法

        参数：
            name (str): 数据类型名称
            field_type (str): 数据类型all
            tag_key （bool): 是否是标签数据类型False
            default (obj): 默认值
        """

        super().__init__(name,field_type,tag_key,default)




class TagsField(Field):
    """
    类介绍：

        这是一个数据模型中的表达fields数据变量类型的基础类
    """    


    def __init__(self,name,field_type = 'str',tag_key = True,default = None):
        """
        属性功能：

            定义一个初始化属性的方法

        参数：
            name (str): 数据类型名称
            field_type (str): 数据类型str
            tag_key （bool): 是否是标签数据类型True
            default (obj): 默认值
        """        

        super().__init__(name,field_type,tag_key,default)



####### 数据模型元类 #########################################################
#############################################################################



class ModelMetaClass(type):
    """
    类介绍：

        这是一个MongoDB数据模型构建类，主要用于抽象数据类型的构建过程。
    """


    def __new__(cls,name,obj,attr):
        """
        属性功能：

            定义一个MongoDB数据模型构建的魔法方法

        参数：
            cls (object): 构建类自身
            name (str): 构建类名称
            obj (object): 构建类父类
            attr (object): 构建类属性，包括方法

        返回：
            obj (object): 构建类
        """

        if name == 'Models':
            return type.__new__(cls,name,obj,attr)
        mappings = {}
        for k,v in attr.items():
            if isinstance(v,Field):
                mappings[k] = v
        for k in mappings.keys():
            attr.pop(k)
        attr['__table_name__'] = name
        attr['__mappings__'] = mappings
        return type.__new__(cls,name,obj,attr)



####### 数据模型基础类 #####################################################
###########################################################################



class Models(dict,metaclass = ModelMetaClass):
    """
    类介绍：

        这是一个InfluxDB数据模型类，主要用于抽象InfluxDB数据表结果。
    """


    def __init__(self,**kwargs):
        """
        属性功能：

            定义一个初始化的方法
        """

        super().__init__(**kwargs)


    def __getattr__(self,key):
        """
        方法功能：

            定义一个获取属性并检查的魔法方法

        参数：
            key (str): 属性关键字

        返回：
            属性对象
        """

        try:
            return self[key]
        except KeyError:
            raise AttributeError("No attribute '{}'".format(key))


    def __setattr__(self,key,value):
        """
        方法功能：

            定义一个设置属性的魔法方法

        参数：
            key (str): 属性关键字
            value (Object): 数据值对象

        返回：
            无
        """

        self[key] = value


    def save(self,storage):
        '''
        方法功能：

            定义一个保存数据模型中的数据到mongodb中的方法

        参数：
            storage (object): 存储器对象(MongoDB)

        返回：
            result (str): 执行结果信息
        '''

        ### 解析数据模型中的数据为字典
        tmp_data_dict = {}
        for tmp_key in list(self.__mappings__.keys()):
            tmp_data_dict[tmp_key] = self[tmp_key]
            tmp_data_dict['time'] = datetime.datetime.now()
        tmp_insert_list = [tmp_data_dict]
        ### 将解析后的字典加载进MongoDB
        storage.insert_info(tmp_insert_list)
        result = "MongoDB save well done!"
        print(result)

        return result


##########################################################################################
##########################################################################################



from fiche.orm import *
from fiche.util import *
import datetime


### 构建数据模型基础类
class people_info(Models):
    name = FieldsField(name = 'name',tag_key = False)
    age = TagsField(name = 'age',tag_key = True)
    address = TagsField(name = 'address',tag_key = True)
    version= TagsField(name = 'version',tag_key= True)



# ### 构建数据模型
# people_info = people_info(name = 'd',age = 45,address = 'chengdu')
# people_info.save()
# print(list(people_info.__mappings__.keys()))
# tmp_data_dict = {}
# for tmp_key in list(people_info.__mappings__.keys()):
#     tmp_data_dict[tmp_key] = people_info[tmp_key]
#     tmp_data_dict['time'] = datetime.datetime.now()
# print(tmp_data_dict)
# tmp_insert_list = [tmp_data_dict]

### 二级API
### fiche_test信息表
fiche_storage = MongoManager(host='192.168.0.111',
                          port=27017,
                          username='admin',
                          password='123456',
                          database='fiche',
                          collection='test')
# print(fiche_test.client)
# fiche_test.insert_info(tmp_insert_list)
### 构建数据模型
people_info = people_info(name = 'e',age = 59,address = 'chengdu',version = '002')
### 保存数据到MongoDB
people_info.save(fiche_storage)
### 查询数据
test_query = {'name':'e','version':'002'}
query_result = fiche_storage.query_info(query = test_query)
print(query_result)



### 一级API
# # ### 增加一条信息
# # test_insert_list = [{'name':'a','age':16,'address':'beijing'},
# #                     {'name':'b','age':30,'address':'shanghai'},
# #                     {'name':'c','age':20,'address':'nanjing'}]                    
# # fiche_test.insert_info(test_insert_list)
# ### 更新一条信息
# # test_update_query = {'name':'a'}
# # test_update_update = {'$set':{'address':'dalian'}}
# # fiche_test.update_info(test_update_query,test_update_update)
# # ### 删除一条信息
# # test_delete_query = {'name':'c'}
# # fiche_test.delete_info(test_delete_query)
# ### 查询一条信息
# test_query = {'name':'b'}
# query_result = fiche_test.query_info(test_query)
# print(query_result)
# for i in query_result:
#     print(i,type(i))

### 二级API

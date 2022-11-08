from fiche.data import *


fiche = FicheData(host='192.168.1.18',
                  port=27017,
                  username='admin',
                  password='123456',
                  database='fiche')


### 增加观察者
# fiche.add_observer(observer_name='test001',observer_version='v001')
# fiche.add_observer(observer_name='test002',observer_version='v002')
# fiche.add_observer(observer_name='test_remove',observer_version='test_remove001')

### 查询观察者
tmp_observer_info_query = fiche.query_observer_info(observer_name='test003',observer_version='v003')
print(tmp_observer_info_query)

### 获取观察者列表
tmp_observers_list = fiche.show_obervers()
print(tmp_observers_list) 

### 删除观察者
# fiche.remove_observer(observer_name='test_remove',observer_version='test_remove001')

### 保存算法信息
# fiche.save_algorithm_info(name = 'test001',
#                           version = 'v001',
#                           summary = 'this is a test algorithm package',
#                           config = 'bash xxxxx.sh',
#                           remark = 'test algorithm remark',
#                           homepage = 'xxx.xxx.xxx.xxx/xxxx',
#                           author = 'shihua',
#                           authoremail = '15021408795@163.com',
#                           license = 'MIT',
#                           requires = 'numpy,sklearn,tensorflow',
#                           requiredby = 'WPFsystem')

### 查询算法信息
tmp_algorithm_info_query = fiche.query_algorithm_info(algorithm_name='test001',algorithm_version='v001')
print(tmp_algorithm_info_query)

### 保存模型信息
# fiche.save_model_info(name = 'test001',
#                       version = 'v001',
#                       summary = 'this is a test model',
#                       config = 'bash xxxxxxx.sh',
#                       remark = 'test model remark',
#                       requires = 'test',
#                       data = 'test data set',
#                       algorithm = 'test algorithm')

### 查询模型信息
tmp_model_info_query = fiche.query_model_info(model_name='test001',model_version='v001')
print(tmp_model_info_query)

### 保存参数信息
# fiche.save_parameter_info(name = 'test001',
#                           version = 'v001',
#                           summary = 'this is a test parameter',
#                           config = 'bash xxxxxxxxxxx.sh',
#                           remark = 'test parameter remark',
#                           datatype = 'test datatype',
#                           requiredby = 'test model')

### 查询参数信息
tmp_parameter_info_query = fiche.query_parameter_info(parameter_name='test001',parameter_version='v001')
print(tmp_parameter_info_query)

### 保存应用信息
# fiche.save_application_info(name = 'test001',
#                             version = 'v001',
#                             summary = 'this is a test application',
#                             config = 'bash xxxxxxxxxxxxx.sh',
#                             remark = 'test application remark',
#                             requires = 'xxx algorithm,xxxxx data',
#                             project = 'wpf system')

### 查询应用信息
tmp_application_info_query = fiche.query_application_info(application_name='test001',application_version='v001')
print(tmp_application_info_query)

### 保存数据信息
# fiche.save_dataset_info(name = 'test001',
#                         version = 'v001',
#                         summary = 'this is a test dataset',
#                         config = 'bash xxxxxxxxxxxxx.sh',
#                         remark = 'test dataset',
#                         requiredby = 'test model,test application',
#                         datatype = 'test datatype',
#                         project = 'pv system')

### 查询数据信息
tmp_dataset_info_query = fiche.query_dataset_info(dataset_name='test001',dataset_version='v001')
print(tmp_dataset_info_query)
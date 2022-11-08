from fiche.cons import * 


### fiche存储
### fiche存储--observer_info
fiche_observer_info_storage = MongoManager(host='192.168.1.18',
                                           port=27017,
                                           username='admin',
                                           password='123456',
                                           database='fiche',
                                           collection='observer_info')
### fiche存储--algorithm_info
fiche_algorithm_info_storage = MongoManager(host='192.168.1.18',
                                            port=27017,
                                            username='admin',
                                            password='123456',
                                            database='fiche',
                                            collection='algorithm_info')
### fiche存储--model_info
fiche_model_info_storage = MongoManager(host='192.168.1.18',
                                        port=27017,
                                        username='admin',
                                        password='123456',
                                        database='fiche',
                                        collection='model_info')                                            
### fiche存储--parameter_info
fiche_parameter_info_storage = MongoManager(host='192.168.1.18',
                                            port=27017,
                                            username='admin',
                                            password='123456',
                                            database='fiche',
                                            collection='parameter_info')
### fiche存储--application_info
fiche_application_info_storage = MongoManager(host='192.168.1.18',
                                              port=27017,
                                              username='admin',
                                              password='123456',
                                              database='fiche',
                                              collection='application_info')
### fiche存储--dataset_info
fiche_dataset_info_storage = MongoManager(host='192.168.1.18',
                                          port=27017,
                                          username='admin',
                                          password='123456',
                                          database='fiche',
                                          collection='dataset_info')                                          


### 观察者信息
test_observer_info = Observer_Info(name = 'test',
                                   version = '001',
                                   summary = 'test oberver',
                                   config = 'test observer config',
                                   remark = 'test remark')
test_observer_info.save(storage=fiche_observer_info_storage)
### 算法包信息
test_algorithm_info = Algorithm_Info(name = 'test',
                                     version = '002',
                                     summary = 'this is a test algorithm package',
                                     config = 'bash xxxxx.sh',
                                     remark = 'test algorithm remark',
                                     homepage = 'xxx.xxx.xxx.xxx/xxxx',
                                     author = 'shihua',
                                     authoremail = '15021408795@163.com',
                                     license = 'MIT',
                                     requires = 'numpy,sklearn,tensorflow',
                                     requiredby = 'WPFsystem')
test_algorithm_info.save(storage=fiche_algorithm_info_storage)


### 模型信息
test_model_info = Model_Info(name = 'test',
                             version = '001',
                             summary = 'this is a test model',
                             config = 'bash xxxxxxx.sh',
                             remark = 'test model remark',
                             requires = 'test',
                             data = 'test data set',
                             algorithm = 'test algorithm')
test_model_info.save(storage=fiche_model_info_storage)   


### 参数信息
test_parameter_info = Parameter_Info(name = 'test',
                                     version = '001',
                                     summary = 'this is a test parameter',
                                     config = 'bash xxxxxxxxxxx.sh',
                                     remark = 'test parameter remark',
                                     datatype = 'test datatype',
                                     requiredby = 'test model')
test_parameter_info.save(storage=fiche_parameter_info_storage)


### 应用信息
test_application_info = Application_Info(name = 'test',
                                         version = '001',
                                         summary = 'this is a test application',
                                         config = 'bash xxxxxxxxxxxxx.sh',
                                         remark = 'test application remark',
                                         requires = 'xxx algorithm,xxxxx data',
                                         project = 'wpf system')
test_application_info.save(storage=fiche_application_info_storage)                                         


### 数据集信息
test_dataset_info = Dataset_Info(name = 'test',
                                 version = '001',
                                 summary = 'this is a test dataset',
                                 config = 'bash xxxxxxxxxxxxx.sh',
                                 remark = 'test dataset',
                                 requiredby = 'test model,test application',
                                 datatype = 'test datatype',
                                 project = 'pv system')
test_dataset_info.save(storage=fiche_dataset_info_storage)



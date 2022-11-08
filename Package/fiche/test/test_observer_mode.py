from fiche.observer_mode import *
from fiche.cons import *



### fiche存储
### fiche存储--observer_info
fiche_observer_info_storage = MongoManager(host='192.168.1.18',
                                           port=27017,
                                           username='admin',
                                           password='123456',
                                           database='fiche',
                                           collection='observer_info')


### 添加观察者
Observable.add_observer(storage=fiche_observer_info_storage,
                        observer_name='test003',
                        observer_version='v003')                                           


### 删除观察者
Observable.remove_observer(storage=fiche_observer_info_storage,
                           observer_name='test',
                           observer_version='003')


### 展示观察者
observers_list = Observable.get_observers(storage=fiche_observer_info_storage) 
print(observers_list)


### 查询配置信息
### 查询observer_info
observer_info_query = fiche_observer_info_storage.query_info({'name':'test'})
print(observer_info_query)

#coding=utf-8
'''定义learning_logs的urls模式'''
from django.conf.urls import url
from . import views

urlpatterns = [
    #主页
    url(r'^$',views.index,name='index'),#views.index的意思是在views模块中查找index()函数
    #显示所有主题
    url(r'^topics/$',views.topics,name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
]

#coding=utf-8
from django.shortcuts import render
from .models import Topic
#render()函数根据视图提供的数据渲染响应

# Create your views here.

def index(request):
    return render(request,'learning_logs/index.html')#在views中查找到这个函数时，将请求对象传入这个视图函数

def topics(request):
    '''显示所有的主题'''
    topics = Topic.objects.order_by('date_add')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request):
    '''显示单个主题及其所有的条目'''
    topic = Topic.object.all()
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
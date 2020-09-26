import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {
        'pick': pick
    }
    return render(request, 'dinner.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)

    
def dtl_practice(request):
    menus = ['짜장면', '탕수육', '짬뽕', '볶음밥']
    empty_list = []
    context = {
        'menus': menus,
        'empty_list': empty_list,
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    msg = request.GET.get('send')
    context = {
        'msg': msg,
    }
    return render(request, 'catch.html', context)
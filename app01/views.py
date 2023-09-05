from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    return render(request, "index.html")


def news(request):
    # 定义一个包含一些新闻的列表
    data_list = ["新闻1", "新闻2", "新闻3", "新闻4", "新闻5"]
    print(data_list)
    return render(request, "news.html", {"data_list": data_list})


def login(request):
    return render(request, "login.html")
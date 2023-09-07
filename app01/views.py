from django.shortcuts import render, redirect

from app01 import models


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


def users(request):
    """定义用户管理网页"""
    # 1.获取所有用户信息
    user_list = models.Users.objects.all()
    return render(request, "users.html", {"user_list": user_list})


def user_delete(request):
    """删除用户"""
    # 1.获取要删除的用户id
    user_id = request.GET.get("id")
    # 2.根据id删除用户
    models.Users.objects.filter(id=user_id).delete()
    # 3.返回用户列表页面
    return redirect("/users/")


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        return render(request, "user_add.html")
    # 1.获取用户提交的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    # 2.将数据添加到数据库
    models.Users.objects.create(username=username, password=password, email=email)
    # 3.返回用户列表页面
    return redirect("/users/")


def user_edit(request, id):
    """编辑用户"""
    if request.method == "GET":
        user = models.Users.objects.get(id=id)
        return render(request, "user_edit.html", {"user": user})
    # 1.获取用户提交的数据,并修改数据库
    user_obj = models.Users.objects.get(id=id)
    user_obj.username = request.POST.get("username")
    user_obj.password = request.POST.get("password")
    user_obj.email = request.POST.get("email")
    user_obj.save()
    # 2.重定向到用户列表页面
    return redirect("/users/")


def test(request):
    return render(request, "test.html")
# View files for product information management
import os
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
import time
from appadmin.models import Product, Category, Size


# Create your views here.

def index(request, pIndex=1):
    smod = Product.objects
    slist = smod.filter(status__lt=9)
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = slist.filter(product_name__contains=kw)
        mywhere.append('keyword=' + kw)
    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        slist = slist.filter(status=status)
        mywhere.append("status=" + status)

    cid = request.GET.get("category_id", None)
    if cid:
        slist = slist.filter(category_id=cid)
        mywhere.append('category_id=' + cid)

    slist = slist.order_by("id")  # 对id排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 5)  # 以每页5条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息

    for vo in list2:
        cob = Category.objects.get(id=vo.category_id)
        vo.categoryname = cob.category_name

    context = {"productlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "appadmin/shop/index.html", context)


def add(request):
    slist = Size.objects.values("id", 'sizenum')
    clist = Category.objects.values("id", "category_name")
    context = {"sizelist": slist, "categorylist": clist}
    return render(request, "appadmin/shop/add.html", context)


def insert(request):
    try:
        # Image upload processing
        myfile = request.FILES.get("picture", None)
        if not myfile:
            return HttpResponse("No cover to upload file information")
        picture = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/web/" + picture, "wb+")
        for chunk in myfile.chunks():  # Write to file in chunks
            destination.write(chunk)
        destination.close()

        ob = Product()
        ob.delivery = request.POST['delivery']
        ob.category_id = request.POST['category_id']
        ob.product_name = request.POST['name']
        ob.price = request.POST['price']
        ob.product_info = request.POST['info']
        ob.picture = picture
        ob.status = 1
        ob.save()
        context = {'info': "Add successful！"}
    except Exception as err:
        print(err)
        context = {'info': "Add failed！"}
    return render(request, "appadmin/info.html", context)


def delete(request, pid=0):
    try:
        ob = Product.objects.get(id=pid)
        ob.status = 9
        ob.save()
        context = {'info': "Add successful！"}
    except Exception as err:
        print(err)
        context = {'info': "Add failed！"}
    return render(request, "appadmin/info.html", context)


def edit(request, pid=0):
    try:
        ob = Product.objects.get(id=pid)
        clist = Category.objects.values("id", "category_name")
        context = {'product': ob, "categorylist": clist}
        return render(request, "appadmin/shop/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "can't find edit information"}
        return render(request, "appadmin/info.html", context)


def update(request, pid):
    try:
        # Get the original image
        oldpic = request.POST['oldpic']
        # Image uploading process
        myfile = request.FILES.get("picture", None)
        if not myfile:
            picture = oldpic
        else:
            picture = str(time.time()) + "." + myfile.name.split('.').pop()
            destination = open("./static/web/" + picture, "wb+")
            for chunk in myfile.chunks():  # Write to file in chunks
                destination.write(chunk)
            destination.close()

        ob = Product.objects.get(id=pid)
        ob.delivery = request.POST['delivery']
        ob.category_id = request.POST['category_id']
        ob.product_name = request.POST['name']
        ob.price = request.POST['price']
        ob.product_info = request.POST['info']
        ob.picture = picture
        ob.status = request.POST['status']
        ob.save()
        context = {'info': "Successful modification！"}

        # Determine and delete old images
        if myfile:
            os.remove("./static/web/" + oldpic)

    except Exception as err:
        print(err)
        context = {'info': "Modification failure！"}
        # Determine and delete new images
        if myfile:
            os.remove("./static/web/" + picture)
    return render(request, "appadmin/info.html", context)

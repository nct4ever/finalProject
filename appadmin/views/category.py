# View files for category information management
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from appadmin.models import Category
import hashlib, random


# Create your views here.

def index(request, pIndex=1):
    umod = Category.objects
    ulist = umod.all()
    mywhere = []
    # Get and determine search criteria
    ky = request.GET.get("keyword", None)
    if ky:
        ulist = ulist.filter(category_name__contains=ky)
        mywhere.append('keyword' + ky)

    cid = request.GET.get("category_id", None)
    if cid:
        ulist = ulist.filter(category_id=cid)
        mywhere.append('category_id=' + cid)

    ulist = ulist.order_by("id")  # sort id
    # Paging
    pIndex = int(pIndex)
    page = Paginator(ulist, 5)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range

    context = {"categorylist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "appadmin/category/index.html", context)


def add(request):
    return render(request, "appadmin/category/add.html")


def insert(request):
    try:
        ob = Category()
        ob.category_name = request.POST['cname']
        ob.save()
        context = {'info': "Add successfully!"}
    except Exception as err:
        print(err)
        context = {'info': "add failed!"}
    return render(request, "appadmin/info.html", context)


def delete(request, cid=0):
    try:
        ob = Category.objects.get(id=cid)
        ob.delete()
        context = {'info': "Delete successfully!"}
    except Exception as err:
        print(err)
        context = {'info': "Delete failed!"}
    return render(request, "appadmin/info.html", context)


def edit(request, cid=0):
    try:
        ob = Category.objects.get(id=cid)
        context = {'category': ob}
        return render(request, "appadmin/category/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "can't find edit information"}
    return render(request, "appadmin/info.html", context)


def update(request, cid):
    try:
        ob = Category.objects.get(id=cid)
        ob.category_name = request.POST['cname']
        ob.save()
        context = {'info': 'edit success'}
    except Exception as err:
        print(err)
        context = {'info': "edit failed"}
    return render(request, "appadmin/info.html", context)

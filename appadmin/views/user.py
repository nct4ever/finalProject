# View files for user information management
from datetime import datetime

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from appadmin.models import User
import hashlib, random


# Create your views here.

def index(request, pIndex=1):
    # Browse information
    umod = User.objects
    ulist = umod.filter(status__lt=9)
    mywhere=[]
    #Get and determine search criteria
    kw = request.GET.get("keyword",None)
    if kw:
        ulist = ulist.filter(username__contains=kw)
        mywhere.append('keyword='+kw) #Encapsulated search criteria

    pIndex = int(pIndex)
    page = Paginator(ulist, 10)  # Paging with every 10 data items
    maxpages = page.num_pages  # Get maximum number of pages
    #Determine if the current page is out of bounds
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1 :
        pIndex = 1
    list2 = page.page(pIndex) #Get current page data
    plist = page.page_range #Get the list of page numbers


    context = {"userlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request, "appadmin/user/index.html", context)


def add(request):
    return render(request,"appadmin/user/add.html")


def insert(request):
    try:
        ob = User()
        ob.username = request.POST['username']
        #The password of the current employee information is processed by MD5
        import hashlib,random
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password'] + str(n) #Get password from form and add noise value
        md5.update(s.encode('utf-8')) #Put the substring to generate md5 into
        ob.password_hash = md5.hexdigest() #get md5 value
        ob.password_salt = n
        ob.email = request.POST['email']
        ob.address = request.POST['address']
        ob.status = 1
        ob.reg_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "add successful"}
    except Exception as err:
        print(err)
        context = {'info': "add failed"}
    return render(request, "appadmin/info.html",context)

def delete(request, uid=0):
    # Execute info deletion
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.save()
        context = {'info': "Delete successfully!"}
    except Exception as err:
        print(err)
        context = {'info': "Delete failed!"}
    return render(request, "appadmin/info.html", context)


def edit(request, uid=0):
    # Load edit form
    try:
        ob = User.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "appadmin/user/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "can't find edit information"}
    return render(request, "appadmin/info.html", context)


def update(request, uid):
    # Execute message edit
    try:
        ob = User.objects.get(id=uid)
        ob.username= request.POST['username']
        ob.status = request.POST['status']
        ob.save()
        context = {'info': 'edit success'}
    except Exception as err:
        print(err)
        context = {'info': "edit failed"}
    return render(request, "appadmin/info.html", context)


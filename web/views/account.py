from django.db.models import Q, QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
from django.core.paginator import Paginator
from appadmin.models import User, Category, Product


def edit(request):
    try:
        slist = User.objects.values("id", 'username')
        context = {"userlist": slist}
        return render(request, "web/account.html", context)
    except Exception as err:
        print(err)
        context = {'info': "can't find edit information"}
    return render(request, context)
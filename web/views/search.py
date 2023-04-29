from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from appadmin.models import Category, User, Product
import time, os
from django.db.models import Q

# Create your views here.

def index(request, pIndex=1):
    umod = Product.objects
    ulist = umod.all()
    mywhere = []
    # Get and determine search criteria
    ky = request.GET.get("keyword", None)
    if ky:
        ulist = ulist.filter(product_name__contains=ky)
        mywhere.append('keyword' + ky)

    pIndex = int(pIndex)
    page = Paginator(ulist, 5)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range


    cartlist = request.session.get('cartlist', {})
    sum = 0  # Initialize a total amount
    # Iterate through the items in the cart and total the total amount
    for vo in cartlist.values():
        sum += vo['num'] * vo['price']
    request.session['sum'] = sum  # Put in session

    context = {"productlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere,'categorylist': request.session.get("categorylist", {}).items()}
    return render(request, "web/search.html", context)


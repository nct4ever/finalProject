from django.db.models import Q, QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
from django.core.paginator import Paginator
from django.views import View

from appadmin.models import User, Category, Product, Size, Rate



def index(request,pIndex=1):
    umod = Product.objects
    ulist = umod.all()

    mywhere = []
    # Get and determine search criteria
    bid = request.GET.get("product_id", None)
    if bid:
        ulist = ulist.filter(id=bid)
        mywhere.append('product_id=' + bid)

    pIndex = int(pIndex)
    page = Paginator(ulist, 5)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range

    for vo in list2:
        uob = Product.objects.get(id=vo.id)
        vo.product_name = uob.product_name

    rmod = Rate.objects
    rlist = rmod.filter(product_id=bid)
    sob=Size.objects
    zlist = sob.all()


    cartlist = request.session.get('cartlist', {})
    sum = 0  # Initialize a total amount
    # Iterate through the items in the cart and total the total amount
    for vo in cartlist.values():
        sum += vo['num'] * vo['price']
    request.session['sum'] = sum  # Put in session

    context = {"productlist": list2,'rlist': rlist,'zlist': zlist,'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere,'categorylist': request.session.get("categorylist", {}).items()}
    return render(request, "web/details.html",context)


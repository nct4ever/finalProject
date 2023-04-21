from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
from appadmin.models import User, Category, Product


def index(request):
    cartlist = request.session.get('cartlist', {})
    sum = 0  # Initialise a total amount
    # Iterate through the items in the shopping cart and add up the total amount
    for vo in cartlist.values():
        sum += vo['num'] * vo['price']
    request.session['sum'] = sum  # put in session

    context = {'categorylist': request.session.get("categorylist", {}).items()}
    return render(request, 'web/cart.html', context)


def add(request, pid):
    # Get all the items in the current shop from the session and get the items to add to the shopping cart.
    product = request.session['productlist'][pid]
    product['num'] = 1  # Initialise the amount of current purchased
    # Try to get the shopping cart information from session with the name cartlist, if not return {}
    cartlist = request.session.get('cartlist', {})
    # Determine if there are items in the current shopping cart to be added to the cart
    if pid in cartlist:
        cartlist[pid]['num'] += product['num']  # increase purchase volume
    else:
        cartlist[pid] = product  # Put in cart
    # Put cartlist cart information into session
    request.session['cartlist'] = cartlist
    # jump to home page
    return redirect(reverse('web_index'))


def delete(request, pid):
    # Try to get the shopping cart information from session with the name cartlist, if not return {}
    cartlist = request.session.get('cartlist', {})
    del cartlist[pid]  # Deleting products
    # Put cartlist cart information into session
    request.session['cartlist'] = cartlist
    # jump to home page
    return redirect(reverse('web_cart'))


def clear(request):
    request.session['cartlist'] = {}
    # jump to home page
    return redirect(reverse('web_cart'))


def change(request):
    cartlist = request.session.get('cartlist', {})
    pid = request.GET.get("pid", 0)
    m = int(request.GET.get('num', 1))
    if m < 1:
        m = 1
    cartlist[pid]['num'] = m
    request.session['cartlist'] = cartlist
    return redirect(reverse('web_cart'))

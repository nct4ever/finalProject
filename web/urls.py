
from django.urls import path,include
from sqlalchemy import func

from appadmin.views import category
from web.views import index, cart, orders, detail, account, search, categories, recommend

urlpatterns = [
    path('', index.index, name="web_index"),

    path('login', index.login, name="web_login"),  # Loading the login form
    path('dologin', index.dologin, name="web_dologin"),  # Execute login
    path('logout', index.logout, name="web_logout"),  # exit login
    path('verify', index.verify, name="web_verify"),
    path('home/', index.webindex, name="web_index"),

    # Add the request prefix web/ to the url route, all url addresses with this prefix must be logged in before they can be accessed
    path("web/", include([
        path('cart/index', cart.index, name="web_cart"),  # Shopping cart page
        path('cart/add/<str:pid>', cart.add, name="web_cart_add"),  # Shopping cart additions
        path('cart/delete/<str:pid>', cart.delete, name="web_cart_delete"),  # Shopping cart delete
        path('cart/clear', cart.clear, name="web_cart_clear"),  # clear shopping cart
        path('cart/change', cart.change, name="web_cart_change"),

        path('orders/<int:pIndex>', orders.index, name="web_orders_index"),  # Order view
        path('orders/detail', orders.detail, name="web_orders_detail"),  # Order detail
        path('orders/status', orders.status, name="web_orders_status"),  # Order status
        path('orders/insert', orders.insert, name="web_orders_insert"),

        path('details/<int:pIndex>', detail.index, name="web_detail"),

        path('user/index', account.edit, name="web_account"),  # Buyer's personal page

        path('search/<int:pIndex>', search.index, name="web_search_index"),  # search page

        path('recommend/', recommend.index, name='web_recommend'),

        path('categoryinfo/<int:pIndex>', categories.index, name="web_category_index"),


    ]))
]

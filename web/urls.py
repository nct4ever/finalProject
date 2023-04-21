from django.urls import path,include

from web.views import index, cart

urlpatterns = [
    path('', index.index, name="web_index"),

    path('login', index.login, name="web_login"),  # Loading the login form
    path('dologin', index.dologin, name="web_dologin"),  # Execute login
    path('logout', index.logout, name="web_logout"),  # exit login
    path('verify', index.verify, name="web_verify"),
    path('home', index.webindex, name="web_index"),

    # Add the request prefix web/ to the url route, all url addresses with this prefix must be logged in before they can be accessed
    path("web/", include([
        path('cart/index', cart.index, name="web_cart"),  # Shopping cart page
        path('cart/add/<str:pid>', cart.add, name="web_cart_add"),  # Shopping cart additions
        path('cart/delete/<str:pid>', cart.delete, name="web_cart_delete"),  # Shopping cart delete
        path('cart/clear', cart.clear, name="web_cart_clear"),  # clear shopping cart
        path('cart/change', cart.change, name="web_cart_change"),
    ]))
]

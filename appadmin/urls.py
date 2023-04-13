from django.urls import path

from appadmin.views import index, product, category
from appadmin.views import user

urlpatterns = [
    path('', index.index, name="appadmin_index"),

    # The administrator login and logout of the route
    path('login', index.login, name="appadmin_login"),
    path('dologin', index.dologin, name="appadmin_dologin"),
    path('logout', index.logout, name="appadmin_logout"),
    path('verify', index.verify, name="appadmin_verify"),


    path('user/<int:pIndex>', user.index, name="appadmin_user_index"),  # Browse
    path('user/add', user.add, name="appadmin_user_add"),  # Add form
    path('user/insert', user.insert, name="appadmin_user_insert"),  # Execute Add
    path('user/del/<int:uid>', user.delete, name="appadmin_user_delete"),  # Execute deletion
    path('user/edit/<int:uid>', user.edit, name="appadmin_user_edit"),  # Load edit form
    path('user/update/<int:uid>', user.update, name="appadmin_user_update"),  # Executive Editor

    path('product/<int:pIndex>', product.index, name="appadmin_product_index"),  # Browse
    path('product/add', product.add, name="appadmin_product_add"),  # Add form
    path('product/insert', product.insert, name="appadmin_product_insert"),  # Execute Add
    path('product/del/<int:pid>', product.delete, name="appadmin_product_del"),  # Execute deletion
    path('product/edit/<int:pid>', product.edit, name="appadmin_product_edit"),  # Load edit form
    path('product/update/<int:pid>', product.update, name="appadmin_product_update"),  # Executive Editor

    path('category/<int:pIndex>', category.index, name="appadmin_category_index"),  # Browse
    path('category/add', category.add, name="appadmin_category_add"), #Add form
    path('category/insert', category.insert, name="appadmin_category_insert"), #Execute Add
    path('category/del/<int:cid>', category.delete, name="appadmin_category_del"), #Execute deletion
    path('category/edit/<int:cid>', category.edit, name="appadmin_category_edit"), #Load edit form
    path('category/update/<int:cid>', category.update, name="appadmin_category_update"), #Executive Editor



]

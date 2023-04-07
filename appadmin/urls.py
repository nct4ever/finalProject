from django.urls import path

from appadmin.views import index
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


]

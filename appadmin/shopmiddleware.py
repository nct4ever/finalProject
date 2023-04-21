#Customize the intermediate class (perform login or non-login judgment)
from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):
        path = request.path
        print("url:",path)

        #Determine if the admin backend is logged in or not
        #Define the list of URLs that the backend can access directly without logging in
        urllist = ['/appadmin/login','/appadmin/logout','/appadmin/dologin','/appadmin/verify']
        #Determine if the current request url address starts with /myadmin and is not in the urllist before making a decision on whether to log in
        if re.match(r'^/appadmin',path) and (path not in urllist):
            #Determine if you are logged in (because there is no adminuser in the session)
            if 'adminuser' not in request.session:
                # Redirect to login page
                return redirect(reverse("appadmin_login"))
                #pass
                # Judgement on frontend user login requests to determine if they are logged in (whether there is a webuser in the session)
        if re.match(r'^/web', path):
                # Determine if you are logged in or not (because there is no adminuser in the session)
            if 'webuser' not in request.session:
                 # Redirect to login page
                return redirect(reverse("web_login"))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
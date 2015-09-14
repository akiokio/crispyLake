"""crispyLake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from todo import urls as todo_urls
from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^api/v1/todos/', include(todo_urls)),
    url(r'^api/v1/accounts/', include(accounts_urls)),
]



# curl -X POST -d "grant_type=password&username=client1&password=123123" -u"ZzfXP8KuTGs1W8yleSFXLT4SPSzTtaWcUELhXv8l:LntuSPsUl6hE8PCiqWONG3joGr164E39KdRj01bCgly9abrkRMVWh6L1SzbjkUEYUdRSoJ0iGGYDNy4RIudhQs4SkwgBgvOX2lOlBxYmIlBdqXksXn5Tg4oRFuJ4LiQj" http://localhost:8000/o/token/
# {"access_token": "X057nRNonJHP1WMBJulx9d7o6E6NNW", "token_type": "Bearer", "expires_in": 36000, "refresh_token": "pRMtX6H4cSGXK47wWqJig65kxjtSpz", "scope": "read write groups"}
# curl -H "Authorization: Bearer X057nRNonJHP1WMBJulx9d7o6E6NNW" http://localhost:8000/todos/

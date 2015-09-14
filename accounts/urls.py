# -*- coding: utf-8 -*-
__author__ = 'akiokio'

from django.conf.urls import url

from accounts.views import SignUp, SignUpSocial

urlpatterns = [
    url(r'signup/social/$', SignUpSocial.as_view(), name="sign_up_social"),
    url(r'signup/$', SignUp.as_view(), name="sign_up"),
]
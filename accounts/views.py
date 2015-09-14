# -*- coding: utf-8 -*-
__author__ = 'akiokio'

from django.contrib.auth import get_user_model, login

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from social.apps.django_app.utils import load_backend, load_strategy
from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.exceptions import AuthAlreadyAssociated

from accounts.serializers import SignUpSerializer, SignUpSocialSerializer
from accounts.permissions import IsAuthenticatedOrCreate
from accounts.oauthtools import get_access_token

User = get_user_model()

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class SignUpSocial(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSocialSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

    def create(self, request, *args, **kwargs):
        provider = request.data['provider']

        # If this request was made with an authenticated user, try to associate this social
        # account with it
        authed_user = request.user if not request.user.is_anonymous() else None

        # `strategy` is a python-social-auth concept referencing the Python framework to
        # be used (Django, Flask, etc.). By passing `request` to `load_strategy`, PSA
        # knows to use the Django strategy
        strategy = load_strategy(request)
        # Now we get the backend that corresponds to our user's social auth provider
        # e.g., Facebook, Twitter, etc.
        backend = load_backend(strategy=strategy, name=provider, redirect_uri=None)

        if isinstance(backend, BaseOAuth1):
            # Twitter, for example, uses OAuth1 and requires that you also pass
            # an `oauth_token_secret` with your authentication request
            token = {
                'oauth_token': request.data['access_token'],
                'oauth_token_secret': request.data['access_token_secret'],
            }
        elif isinstance(backend, BaseOAuth2):
            # We're using oauth's implicit grant type (usually used for web and mobile
            # applications), so all we have to pass here is an access_token
            token = request.data['access_token']

        try:
            # if `authed_user` is None, python-social-auth will make a new user,
            # else this social account will be associated with the user you pass in
            user = backend.do_auth(token, user=authed_user)
            login(request, user)
        except AuthAlreadyAssociated:
            # You can't associate a social account with more than user
            return Response({"errors": "That social media account is already in use"},
                            status=status.HTTP_400_BAD_REQUEST)

        if user and user.is_active:
            # if the access token was set to an empty string, then save the access token
            # from the request
            auth_created = user.social_auth.get(provider=provider)
            if not auth_created.extra_data['access_token']:
                # Facebook for example will return the access_token in its response to you.
                # This access_token is then saved for your future use. However, others
                # e.g., Instagram do not respond with the access_token that you just
                # provided. We save it here so it can be used to make subsequent calls.
                auth_created.extra_data['access_token'] = token
                auth_created.save()

            return get_access_token(user)
        else:
            return Response({"errors": "Error with social authentication"},
                            status=status.HTTP_400_BAD_REQUEST)
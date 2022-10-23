import email
from . models import Account
from django.contrib.auth.backends import ModelBackend
import logging

class MyAuthBackEnd(ModelBackend):
    def authenticate(self, **kwargs):
        
        username = kwargs['username']
        password = kwargs['password']
        
        try:
            account = Account.objects.get(email=username)
            if account.check_password(password) is True:
                return account
        except Account.DoesNotExist:
            pass

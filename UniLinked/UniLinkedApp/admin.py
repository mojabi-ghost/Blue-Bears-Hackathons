from django.contrib import admin

# Register your models here.
from . models import Register, Account, Message, Room

admin.site.register(Account)
admin.site.register(Message)
admin.site.register(Room)
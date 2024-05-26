from django.contrib import admin
from authentication.models import CustomUser, LoginCheck

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(LoginCheck)
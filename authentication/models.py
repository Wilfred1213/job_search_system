from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True)
    second_name = models.CharField(max_length=255, null=True)
    photograph = models.ImageField(upload_to='passports')
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

class LoginCheck(models.Model):
    jobseeker = models.BooleanField('Are you an Applicant', default= False)
    employer = models.BooleanField('Are you an Employer', default=False)
    


from django.contrib import admin
from searchApp.models import *

# Register your models here.
admin.site.register(JobApplication)
admin.site.register(JobCategory)
admin.site.register(JobPosting)
# admin.site.register(EmploymentType)
admin.site.register(JobDescription)


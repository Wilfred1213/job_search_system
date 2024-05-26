from django.urls import path, include
from searchApp import views as v


urlpatterns = [
   
    path('', v.index, name='index'),
    path('add_job', v.add_job, name='add_job'),
    path('job_listing', v.job_listing, name='job_listing'),
    path('job_details/<int:job_id>/', v.job_details, name='job_details'),
    path('application/<int:job_id>/', v.application, name='application'),
    path('job_category/<int:cat_id>/', v.job_category, name='job_category'),
    # path('category/<int:cat_id>/<int:desc_id>/', v.job_category, name='job_details'),
    path('job_category_detail/<int:cat_id>/', v.job_category_detail, name='job_category_detail'),
]

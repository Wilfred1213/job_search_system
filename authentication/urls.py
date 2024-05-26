from django.urls import path, include
from authentication import views as v

app_name = 'authentication'
urlpatterns = [
   
    path('signup/', v.signup, name='signup'),
    path('user_login/', v.user_login, name='user_login'),
    path('logout_user/', v.logout_user, name='logout_user')
]
from django.urls import path,include
from accounts.views import *

urlpatterns = [
    
    path('register',UserRegistration.as_view(),name='createuser'),
    path('updateuser/<int:id>',UpdateCustomeUser.as_view(),name='updateuser'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    
     
    #user login and Logout
    path('login', UserLogin.as_view(), name='user_login'),
    path('logout', UserLogout.as_view(), name='userlogout'),
    path('api/changepassword', ChangePassword.as_view(), name='api/changepassword'),
    

]

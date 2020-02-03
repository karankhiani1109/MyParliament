from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emailotpverify', views.emailotpverify, name='emailotpverify'),
    path('register',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('application', views.application, name='application'),

    path('application1', views.application1, name='application1'),
    path('application2', views.application2, name='application2'),
    path('application3', views.application3, name='application3'),
    path('application4', views.application4, name='application4'),
    path('application5', views.application5, name='application5'),
    
    
    # path('/application', views.index, name='index'),
    
]
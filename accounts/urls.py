from django.urls import path
from .import views

urlpatterns=[
    path("signup",views.sign_up,name="sign_up"),
    path("login",views.login,name='login'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout,name='logout'),
]
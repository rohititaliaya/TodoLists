from django.urls import path
from django.conf.urls import url
from mLogin import views

urlpatterns = [
    path('',views.Index,name="login"),
    path('Register',views.Register,name="Register"),
    path('userHome/<str:pk>/',views.Home,name="Home"),
    path('logout',views.logout,name="logout")
]
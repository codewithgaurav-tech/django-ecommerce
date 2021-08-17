from django.urls import path
from . import  views

urlpatterns = [
   path("register",views.register, name="register"),
   path('reg_page', views.reg_view,name="To open reg page"),
   path('login_page', views.login_view,name="To open login page"),
   path('logeed_in',views.logeed_in, name="logeed_in")

    ]
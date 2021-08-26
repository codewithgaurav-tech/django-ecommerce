from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
   path("",views.index, name="ShopHome"),
   path("about/",views.about, name="about"),
   path("contact/",views.contact, name="contact"),
   path("tracker/",views.tracker, name="tracker"),
   path("search/",views.search, name="search"),
   path("products/<int:my_id>", views.products, name="products"),
   path("checkout/",views.checkout, name="checkout")
]

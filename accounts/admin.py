from itertools import product

from django.contrib import admin

# Register your models here.
from .models import  user

admin.site.register(user)

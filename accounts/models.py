from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=300)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

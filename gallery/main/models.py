from django.db import models


# Create your models here.

class Add_img(models.Model):
    img = models.ImageField(upload_to="img/")
    category = models.CharField(max_length=30,default="nature")
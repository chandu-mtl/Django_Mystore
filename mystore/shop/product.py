from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='imp')
    desc=models.TextField()
    price=models.IntegerField()



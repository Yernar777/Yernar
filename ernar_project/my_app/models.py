from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=20)
    processor = models.TextField()
    price = models.IntegerField(max_length=15)



class Cards(models.Model):
    name = models.CharField(max_length=7)
    descroptions = models.TextField()
    prise = models.IntegerField()
    old_price = models.IntegerField()
    img = models.ImageField(upload_to = 'upload',blank=True,null=True)

class Category(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Laptop(models.Model):
    name = models.CharField(max_length=10)
    descriptions = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
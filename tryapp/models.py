from django.db import models

# Create your models here.
class BookStore(models.Model):
    book_name = models.CharField(max_length=25, blank=True,null=True)
    book_price = models.IntegerField(blank=True,null=True)
    book_auther_name = models.CharField(max_length=20,blank=True,null=True)

class Banking(models.Model):
    bank_name = models.CharField(max_length=25,blank=True,null=True)
    ifsc_code = models.CharField(max_length=25,blank=True,null=True)
    bank_location = models.CharField(max_length=100,null=True,blank=True)
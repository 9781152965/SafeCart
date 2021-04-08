from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=500)
    head0 = models.CharField(max_length=5000, default='')
    chead0 = models.CharField(max_length=5000, default='')
    head1 = models.CharField(max_length=5000, default='')
    chead1= models.CharField(max_length=5000,default='')
    head2= models.CharField(max_length=5000,default='')
    chead2= models.CharField(max_length=5000,default='')
    pub_date = models.DateField(default=datetime.now(), blank=True)
    thumbnail = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.tittle

# Create your models here.
class Customer2(models.Model):
    user_1 = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name_1 = models.CharField(max_length=200)
    address_1 = models.CharField(max_length=200, null=True, blank=True)
    joined_on= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
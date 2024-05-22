from django.db import models
from onlyAuth.models import User


class RentPost(models.Model):
    
    renter = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    location = models.CharField(max_length=100)
    area = models.IntegerField()
    rent = models.IntegerField()
    number_of_rooms = models.IntegerField()
    posted = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='image',blank=True)

class Booking(models.Model):
    property = models.ForeignKey(RentPost,on_delete=models.CASCADE)
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    bookingForDate = models.DateField()

class fav(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    property= models.ForeignKey(RentPost,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


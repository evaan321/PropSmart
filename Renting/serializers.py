from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name'] 
class RentPostSerializer(serializers.ModelSerializer):
    renter = UserSerializer()
    class Meta:
        model = RentPost
        fields = '__all__'


class RentPostUser(serializers.ModelSerializer):
    
    class Meta:
        model = RentPost
        fields = '__all__'



class BookingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Booking
        fields = '__all__'

class showBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 1

class Bookmark(serializers.ModelSerializer):
    class Meta:
        model = fav
        fields = '__all__'
        depth = 1
        

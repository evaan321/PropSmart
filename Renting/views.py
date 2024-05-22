from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class RentPostView(viewsets.ModelViewSet):
    queryset = RentPost.objects.all()

    serializer_class = RentPostSerializer


class RentPostUserView(viewsets.ModelViewSet):
    queryset = RentPost.objects.all()

    serializer_class = RentPostUser

class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ShowBookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = showBookingSerializer


"""
URL configuration for SmartProp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from onlyAuth.views import *
from rest_framework import routers
router  = routers.DefaultRouter()
from django.conf.urls.static import static
from django.conf import settings
from Renting.views import *

router.register('Home',RentPostView)
router.register('Post',RentPostUserView)
router.register('booking',BookingView)
router.register('showBooking',ShowBookingView)
router.register('bookmark',bookmarkView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/', activate),
    path('login/',UserLoginApiView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('', include(router.urls)),
    path('password_reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
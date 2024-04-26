from django.urls import path
from contactus.views import contactUS
urlpatterns = [
    path('contact/',contactUS,name='contactus'),

]
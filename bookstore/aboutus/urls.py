from django.urls import path
from aboutus.views import aboutus
urlpatterns = [
    path('about/',aboutus,name='aboutus'),
]
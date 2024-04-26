from django.urls import path
from bookindex.views import allbooks,showbook
urlpatterns = [
    path('bookslist/',allbooks,name='list'),
    path('showbook/<int:id>', showbook, name='viewbook')
]
from django.shortcuts import render

# Create your views here.
import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
Books = [
    {"id": 1, "title": "book1", "author": "Ahmed", "no_of_pages": "23","image":"https://marketplace.canva.com/EAFaQMYuZbo/1/0/1003w/canva-brown-rusty-mystery-novel-book-cover-hG1QhA7BiBU.jpg","price":30},
    {"id": 2, "title": "book2", "author": "mohamed", "no_of_pages": "100", "image": "https://marketplace.canva.com/EAFfSnGl7II/2/0/1003w/canva-elegant-dark-woods-fantasy-photo-book-cover-vAt8PH1CmqQ.jpg", "price": 200},
    {"id": 3, "title": "book3", "author": "heba", "no_of_pages": "100", "image": "https://marketplace.canva.com/EAFf0E5urqk/1/0/1003w/canva-blue-and-green-surreal-fiction-book-cover-53S3IzrNxvY.jpg", "price": 100},
    {"id": 4, "title": "book4", "author": "hana", "no_of_pages": "180", "image": "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/teal-and-orange-fantasy-book-cover-design-template-056106feb952bdfb7bfd16b4f9325c11.jpg?ts=1698543827", "price": 340},
    {"id": 5, "title": "book5", "author": "karim", "no_of_pages": "170", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaM9ed8SHyYHsGnyNct6Jjezc1KCIncWT8Mj-5qxmZrg&s", "price": 290},
]


def showbook(request, id):
    books = filter(lambda BOOK: BOOK["id"] == id, Books)  # filter object
    books = list(books)
    if books:
        return render(request, 'bookcard.html',context={"book":books[0]})
    return HttpResponse("book not found")


def allbooks(request):
    return render(request, 'bookslist.html',context={"Books":Books})


def mytempp(request):
    return render(request, 'my.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book  # The book is available now
from rest_framework import viewsets
from .serializers import BookSerializer


def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html',
                  {'books': books})  # Rendering a template to the server, {} is used to pass an opject


class Another(View):  # This class will have a multiple functions to use it for my application
    book = Book.objects.filter(isPublished=True)  # We referenced all the object from that model to the var  book
    bookWithId = Book.objects.get(id=1)

    # We can filter the search using .filter function
    output = f"We have {bookWithId.title} book in DB WITH id {bookWithId.id} \n <br>"

    # for book in books:
    #     output += f"We have {book.title} book in DB WITH id {book.id} \n <br>"
    # print("Number Of books --> ", len(books))
    # output += f"We have {len(books)} books in DB"

    def get(self, request):
        return HttpResponse(self.output)


class BookViewSet(viewsets.ModelViewSet):  # Create built in view for our book and will it create the http methods
    serializer_class = BookSerializer
    queryset = Book.objects.all()


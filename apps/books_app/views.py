from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

def index(request):
    print("*"*100)
    print("This is the index rendering")
    context = {
        'books' : Books.objects.all()
    }
    return render(request, "books_app/index.html", context)

def add_book(request):
    print("*"*100)
    print("processing new book")
    new_book = Books.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def book_info(request, book_id):
    print('*'*100)
    print("this is the book info page")
    context = {
        'books' : Books.objects.get(id = book_id),
        'authors' : Books.objects.get(id = book_id).authors.all()
    }
    return render(request, "books_app/book_info.html", context)
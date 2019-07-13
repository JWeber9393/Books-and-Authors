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

def authors(request):
    print("*"*100)
    print("This is the authors rendering")
    context = {
        'authors' : Authors.objects.all()
    }
    return render(request, "books_app/authors.html", context)

def add_author(request):
    print("*"*100)
    print("processing new author")
    new_author = Authors.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'])
    return redirect('/authors')


def author_info(request, author_id):
    print('*'*100)
    print("this is the author info page")
    context = {
        'authors' : Authors.objects.get(id = author_id),
        'books' : Authors.objects.get(id = author_id).books.all()
    }
    return render(request, "books_app/author_info.html", context)
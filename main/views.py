from django.shortcuts import render, HttpResponse, redirect
from .models import BookShop

def homepage(request):
    return HttpResponse('Books')

def books(request):
    book_list = BookShop.objects.all()
    return render(request, 'books.html', {"book_list": book_list})

def add_book(request):
    form = request.POST
    text = form["book_text"]
    book = BookShop(text=text)
    book.save()
    return redirect(books)
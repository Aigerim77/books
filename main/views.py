from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse('Books')

def books(request):
    return render(request, 'books.html')

def add_book(request):
    form = request.POST
    title = form['book_title']
    book_title = Book(title=title)
    book_title.save()

    subtitle = form['book_subtitle']
    book_subtitle = Book(subtitle=subtitle)
    book_subtitle.save()

    description = form['book_description']
    book_description = Book(description=description)
    book_description.save()
    return redirect(books)
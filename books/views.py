from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from books.models import *
#from django.contrib.auth.models import User
#from django.contrib import auth
from django.contrib import *
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method == 'POST':
        post = request.POST
    return render_to_response("home.html")
def searchbook(request): 
    if 'tname' in request.GET:       
        name = request.GET['tname']   
        authors = Author.objects.filter(Name=name)
        book = Book.objects.filter(AuthorID=authors[0].AuthorID)
        c = Context({"book":book})
        return render_to_response("searchbook.html",c)
    else:
        return HttpResponse("Hello world")
def bookinformation(request):
    title = request.GET['name']
    book = Book.objects.filter(Title = title)
    author = Author.objects.filter(AuthorID=book[0].AuthorID)
    c = Context({"book":book ,"author":author})    
    return render_to_response("bookinformation.html",c)

def deletebook(request):
    title = request.GET["title"]
    book=Book.objects.get(Title=title)
    book.delete() 

    return render_to_response("deletebook.html")

def addbook(request):
    if request.method == 'POST':
        post = request.POST
        new_book = Book(
            ISBN = post["ISBN"],
            Title = post["Title"],
            AuthorID = post["AuthorID"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"],)
        new_book.save()
        author = Author.objects.filter(AuthorID=new_book.AuthorID)

        if author.exists():
            return render_to_response("addedbook.html")
        else:
            #afteraddbook(request)
            return HttpResponseRedirect("/afteraddbook/")
    return render_to_response("addbook.html")  

def afteraddbook(request):
    if request.method == 'POST':
        post = request.POST
        new_author = Author(
            AuthorID = post['AuthorID'],
            Name = post['Name'],
            Age = post['Age'],
            Country = post['Country'],)
        new_author.save() 
    return render_to_response("afteraddbook.html")

def updatebook(request):
    title = request.GET["title"]
    book=Book.objects.get(Title=title)
    if request.method == 'POST':
        post = request.POST
        book.ISBN = post["ISBN"]
        book.AuthorID = post["AuthorID"]
        book.Publisher = post["Publisher"]
        book.PublishDate = post["PublishDate"]
        book.Price = post["Price"]
        book.save()
    return render_to_response("updatebook.html")
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, TemplateView, View
from django.urls import reverse_lazy
from one.models import Book, Author
from django.http import JsonResponse



class BooksView(ListView):
    model = Book
    template_name = "one/book_list.html"
    context_object_name = "books"
    
class BookView(DetailView):
    model = Book
    template_name = "one/book.html"
    context_object_name = "book"

class CreateBookView(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("booklist")
    template_name = "one/create_book.html"
    
class DeleteBookView(DeleteView):
    model = Book
    template_name = "one/delete_book.html"
    success_url = reverse_lazy("booklist")
    context_object_name = "book"
    
    

def author_list_view(request):
    authors = Author.objects.all()
    return render(request, "one/author_list.html", context={"authors": authors})

def author_page(request, id):
    author = Author.objects.get(id=id)
    booklist = Book.objects.filter(author=author)
    return render(request, "one/author_page.html", context={"author": author, "books": booklist})
    

    
 

# Create your views here.

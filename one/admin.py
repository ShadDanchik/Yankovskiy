from django.contrib import admin
from .models import Author, Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = "title", "author", "year", "price"
    ordering = "author", "title"
    list_filter = "year", "author", "price"
    search_fields = ["title"]
    list_editable = "price",
    
    
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
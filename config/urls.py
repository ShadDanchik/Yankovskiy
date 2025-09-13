"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from config import settings
from django.conf.urls.static import static
from one.views import (
    BooksView,
    BookView,
    CreateBookView,
    DeleteBookView,
    author_list_view,
    author_page
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", BooksView.as_view(), name="booklist"),
    path("book/<int:pk>", BookView.as_view(), name="book"),
    path("bookcreate/", CreateBookView.as_view(), name="create_book"),
    path("delete/<int:pk>", DeleteBookView.as_view(), name="delete"),
    path("authorlist/", author_list_view, name="authorlist"),
    path("authorpage/<int:id>", author_page, name="authorpage")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

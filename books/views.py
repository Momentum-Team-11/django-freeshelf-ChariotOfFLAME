from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book
from .models import User
from .view_helpers import is_staff, is_user, book_is_favorited
from .forms import BookForm
# from .forms import BooksForm


def home(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    else:
        return render(request, "books/home.html")


@login_required
def list_books(request):
    books = Book.objects.all()
    books = books.order_by("-id")
    return render(request, 'books/list_books.html', {'books': books})


@login_required
def add_favorite(request, book_pk):
    user = request.user
    book = get_object_or_404(Book, pk=book_pk)
    user.favorite_books.add(book)
    return redirect(to="list_books")

@login_required
def remove_favorite(request, book_pk):
    user = request.user
    book = get_object_or_404(Book, pk=book_pk)
    user.favorite_books.remove(book)
    return redirect(to="list_books")


@login_required
def sort_by_category(request, slug):
    books = Book.objects.filter(categories__slug=slug)

    return render(request, "books/list_books.html", {"books": books})


# --------------- ADMIN PAGES -----------------
@login_required
@user_passes_test(is_staff)
def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')
    return render(request, "books/new.html", {"form": form})


@login_required
@user_passes_test(is_staff)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to="list_books")
    return render(request, "books/edit.html", {
        "form": form, 
        "book": book
    })


@login_required
@user_passes_test(is_staff)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_books')

    return render(request, "books/delete.html",
                  {"book": book})


# Create your views here.

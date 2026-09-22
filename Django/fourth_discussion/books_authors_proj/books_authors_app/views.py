from django.shortcuts import render, redirect
from . import models

def books_index(request):
    context = {
        "all_books": models.get_all_books()
    }
    return render(request, "books.html", context)

def add_book(request):
    if request.method == "POST":
        models.create_book(request.POST)
    return redirect('/')

def book_detail(request, book_id):
    context = {
        "book": models.get_book_by_id(book_id),
        "unassigned_authors": models.get_unassigned_authors_for_book(book_id)
    }
    return render(request, "book_detail.html", context)

def add_author_to_book(request, book_id):
    if request.method == "POST":
        models.add_author_to_book(book_id, request.POST['author_id'])
    return redirect(f'/books/{book_id}')


def authors_index(request):
    context = {
        "all_authors": models.get_all_authors()
    }
    return render(request, "authors.html", context)

def add_author(request):
    if request.method == "POST":
        models.create_author(request.POST)
    return redirect('/authors')

def author_detail(request, author_id):
    context = {
        "author": models.get_author_by_id(author_id),
        "unassigned_books": models.get_unassigned_books_for_author(author_id)
    }
    return render(request, "author_detail.html", context)

def add_book_to_author(request, author_id):
    if request.method == "POST":
        models.add_book_to_author(author_id, request.POST['book_id'])
    return redirect(f'/authors/{author_id}')
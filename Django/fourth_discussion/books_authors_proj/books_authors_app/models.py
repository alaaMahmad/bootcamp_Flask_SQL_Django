from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(null=True)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def get_all_books():
    return Book.objects.all()

def create_book(data):
    return Book.objects.create(
        title=data['title'],
        desc=data['desc']
    )

def get_book_by_id(book_id):
    return Book.objects.get(id=book_id)

def get_unassigned_authors_for_book(book_id):
    book = get_book_by_id(book_id)
    assigned_author_ids = book.authors.values_list('id', flat=True)
    return Author.objects.exclude(id__in=assigned_author_ids)

def add_author_to_book(book_id, author_id):
    book = get_book_by_id(book_id)
    author = get_author_by_id(author_id)
    book.authors.add(author)


def get_all_authors():
    return Author.objects.all()

def create_author(data):
    return Author.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        notes=data.get('notes', '')
    )

def get_author_by_id(author_id):
    return Author.objects.get(id=author_id)

def get_unassigned_books_for_author(author_id):
    author = get_author_by_id(author_id)
    assigned_book_ids = author.books.values_list('id', flat=True)
    return Book.objects.exclude(id__in=assigned_book_ids)

def add_book_to_author(author_id, book_id):
    author = get_author_by_id(author_id)
    book = get_book_by_id(book_id)
    author.books.add(book)
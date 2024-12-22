import pytest
from main import BooksCollector

@pytest.fixture
def books_list():
    books_list = ['Гордость и предубеждение и зомби', 'Властелин колец', 'Смерть на Ниле']
    return books_list

@pytest.fixture
def books_dict(books_list):
    books_dict = {}
    for book in books_list:
        books_dict[book] = ''
    return books_dict

@pytest.fixture
def books_with_genre():
    books_with_genre = {'Гордость и предубеждение и зомби': 'Фантастика',
                        'Властелин колец': 'Фантастика',
                        'Смерть на Ниле': 'Детективы'}
    return books_with_genre

@pytest.fixture
def favorite_books_list():
    favorite_books_list = ['Властелин колец', 'Смерть на Ниле']
    return favorite_books_list

@pytest.fixture
def add_books_with_genre(collector, books_with_genre):
    for key, value in books_with_genre.items():
        collector.add_new_book(key)
        collector.set_book_genre(key, value)
    return collector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_books(collector, books_list):
    for book in books_list:
        collector.add_new_book(book)
    return collector

@pytest.fixture
def add_books_to_favorite(collector, favorite_books_list):
    for book in favorite_books_list:
        collector.add_book_in_favorites(book)
    return collector




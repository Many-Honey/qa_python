import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тестируем add_two_books - добавление книги с названием > 40 символов
    def test_add_new_book_name_length_more_than_40_not_added(self, collector):
        # добавляем книгу с названием длинной в 70 символов
        collector.add_new_book('Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции')
        # проверяем, что книга не добавилась
        # словарь books_genre имеет длину 0
        assert len(collector.books_genre) == 0

    # тестируем add_two_books - добавление одной и той же книги дважды
    def test_add_new_book_add_two_equal_books_second_book_not_added(self, collector):
        # добавляем две одинаковые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что добавилась только одна книга
        # словарь books_genre имеет длину 1
        assert len(collector.books_genre) == 1

    # тестируем set_book_genre - установка жанра добавленной книге
    def test_set_book_genre_set_genre_from_gener_list_to_added_book(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # устанавливаем жанр из списка жанров для добавленной книги
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # проверяем что значение ключа добавленной книги соответствует назначенному жанру
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    # тестируем set_book_genre - установка жанра для книги которая не добавлена в books_genre
    def test_set_book_genre_set_genre_from_gener_list_to_not_added_book(self, collector):
        # устанавливаем жанр из списка жанров для книги которой нет в books_genre
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # проверяем что значения 'Фантастика' нет в словаре books_genre
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    # тестируем set_book_genre - установка жанра которого нет в списке жанров
    def test_set_book_genre_set_genre_not_from_gener_list_to_added_book(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # устанавливаем жанр которого нет в списке жанров
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Мелодрама')
        # проверяем что жанр не присвоен фильму
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # тестируем get_book_genre - получение жанра добавленной книги
    def test_get_book_genre(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # устанавливаем жанр из списка жанров для добавленной книги
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # проверяем что метод get_book_genre для добавленной ранее книги вернет назначенный ей жанр
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    # тестируем get_books_with_specific_genre - получение всех добавленных книг указанного жанра
    @pytest.mark.parametrize('books_list, genre',
                             [
                                 [['Гордость и предубеждение и зомби', 'Властелин колец'], 'Фантастика'],
                                 [['Смерть на Ниле'], 'Детективы']
                             ])
    def test_get_books_with_specific_genre(self, books_list, genre, collector, add_books_with_genre):
        assert collector.get_books_with_specific_genre(genre) == books_list

    # тестируем get_books_genre - проверяем что метод возвращает словарь с добавленными книгами
    def test_get_books_genre(self, collector, add_books, books_dict):
        assert collector.get_books_genre() == books_dict

    # тестируем get_books_for_children - проверяем что в список книг для детей не входят книги с возрастным рейтингом
    def test_get_books_for_children_age_rating_books_not_in_children_book_list(self, collector, add_books_with_genre):
        # проверяем что книги 'Смерть на Ниле' жанра 'детективы' нет в списке книг для детей
        assert 'Смерть на Ниле' not in collector.get_books_for_children()

    # тестируем add_book_in_favorites - добавление 2х книг в список избранных
    def test_add_book_in_favorites_add_two_books(self, collector, add_books, favorite_books_list):
        for book in favorite_books_list:
            collector.add_book_in_favorites(book)
        assert len(collector.favorites) == 2

    # тестируем delete_book_from_favorites - удаление одной книги из списка избранных
    def test_delete_book_from_favorites_delete_one_book(self, collector, add_books, add_books_to_favorite,
                                                        favorite_books_list):
        # удаляем одну книгу из списка избранных
        collector.delete_book_from_favorites(favorite_books_list[0])
        # проверяем что удаленной книги нет в списке избранных книг
        assert favorite_books_list[0] not in collector.favorites

    # тестируем get_list_of_favorites_books - проверяем что метод возвращает список избранных книг
    def test_get_list_of_favorites_books(self, collector, add_books, add_books_to_favorite, favorite_books_list):
        assert collector.get_list_of_favorites_books() == favorite_books_list

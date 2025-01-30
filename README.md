# qa_python
### Описание
Проект тестирования приложения BooksCollector
### Использование
- Для запуска тестов должен быть установлен пакет `pytest`
- Запуск всех тестов с подробным выводом результатов выполняется командой `pytest -v tests.py`
### Содержание проекта
- main.py - код приложения BooksCollector
- conftest.py - фикстуры для тестов
- README.md - описание проекта
- tests.py - класс TestBooksCollector объединяющий набор тестов, покрывающих приложение BooksCollector
### Список тест-методов:
1. `test_add_new_book_add_two_books` - добавление двух книг
2. `test_add_new_book_name_length_more_than_40_not_added` - добавление книги с названием > 40 символов
3. `test_add_new_book_add_two_equal_books_second_book_not_added` - добавление одной и той же книги дважды
4. `test_set_book_genre_set_genre_from_gener_list_to_added_book` - установка жанра добавленной книге
5. `test_set_book_genre_set_genre_from_gener_list_to_not_added_book` - установка жанра для книги которая не добавлена в books_genre
6. `test_set_book_genre_set_genre_not_from_gener_list_to_added_book` - установка жанра которого нет в списке жанров
7. `test_get_book_genre` - получение жанра добавленной книги
8. `test_get_books_with_specific_genre` - получение всех добавленных книг указанного жанра
9. `test_get_books_genre` - получение словаря с добавленными книгами
10. `test_get_books_for_children_age_rating_books_not_in_children_book_list` - проверка что в список книг для детей не входят книги с возрастным рейтингом
11. `test_add_book_in_favorites_add_two_books` - добавление 2х книг в список избранных
12. `test_delete_book_from_favorites_delete_one_book` - удаление одной книги из списка избранных
13. `test_get_list_of_favorites_books` - проверка что метод возвращает список избранных книг
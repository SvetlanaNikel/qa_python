import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'name',
        ['',
         'Гостья из будущего и еще приключения собачек']
    )
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_repeat_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.set_book_genre('Град обреченный', 'Фантастика')
        assert collector.get_book_genre('Град обреченный') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Драмы')
        assert collector.get_book_genre('Гордость и предубеждение') == ''

    def test_set_book_genre_missing_genre_not_added(self):
        collector = BooksCollector()
        collector.set_book_genre('Град обреченный', 'Фантастика')
        assert not collector.get_book_genre('Град обреченный')

    def test_get_books_with_specific_genre_is_returned_correctly(self):
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.set_book_genre('Град обреченный', 'Фантастика')
        assert 'Град обреченный' in collector.get_books_with_specific_genre("Фантастика")

    def test_get_books_with_specific_genre_does_not_match(self):
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.set_book_genre('Град обреченный', 'Фантастика')
        assert 'Град обреченный' not in collector.get_books_with_specific_genre("Ужасы")

    def test_get_books_for_children_is_returned_correctly(self):
        collector = BooksCollector()
        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        assert 'Золушка' in collector.get_books_for_children()

    def test_get_books_for_children_has_not_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Пила-2')
        collector.set_book_genre('Пила-2', 'Ужасы')
        assert 'Пила-2' not in collector.get_books_for_children()

    def test_add_book_in_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book('Пила-2')
        collector.add_book_in_favorites('Пила-2')
        assert 'Пила-2' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_missing_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Пила-2')
        assert 'Пила-2' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Пила-2')
        collector.add_book_in_favorites('Пила-2')
        collector.delete_book_from_favorites('Пила-2')
        assert 'Пила-2' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_missing_book_not_deleted(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Пила-2')
        assert 'Пила-2' not in collector.get_list_of_favorites_books()



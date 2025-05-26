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
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize(
        'book',
        ['Что делать, если ваш кот хочет вас убить']
    )
    def test_add_new_book_add_one_book(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.books_genre) == 1

    def test_set_book_genre_add_correct(self, add_one_sciencefiction_book):        
        assert add_one_sciencefiction_book.books_genre.get('Что делать, если ваш кот хочет вас убить') == 'Фантастика'

    @pytest.mark.parametrize(
        'book, genre',
        [
            ['Что делать, если ваш кот хочет вас убить', 'Фантастика'],
            ['Собака баскервилей', 'Ужасы'],
            ['Мой личный враг', 'Детективы'],
            ['Ну Погоди!', 'Мультфильмы'],
            ['Бриллиантовая рука', 'Комедии']
        ]
    )
    def test_set_book_genre_add_correct1(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.books_genre.get(book) == genre

    def test_get_book_genre_from_another_book(self, add_one_sciencefiction_book):
        add_one_sciencefiction_book.add_new_book('Звёздные войны')
        add_one_sciencefiction_book.set_book_genre('Звёздные войны', add_one_sciencefiction_book.get_book_genre('Что делать, если ваш кот хочет вас убить'))
        assert add_one_sciencefiction_book.books_genre.get('Звёздные войны') == 'Фантастика'


    def test_get_books_with_specific_genre_one(self, add_one_book_every_genre):
        assert add_one_book_every_genre.get_books_with_specific_genre('Ужасы') == ['Собака баскервилей']

    def test_get_books_genre_dict_value(self, add_one_book_every_genre):
        assert add_one_book_every_genre.books_genre == {
    'Что делать, если ваш кот хочет вас убить': 'Фантастика'
    , 'Собака баскервилей': 'Ужасы'
    , 'Мой личный враг': 'Детективы'
    , 'Ну Погоди!': 'Мультфильмы'
    , 'Бриллиантовая рука': 'Комедии'
    }

    def test_get_books_for_children_list_value(self, add_one_book_every_genre):
        assert add_one_book_every_genre.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить', 'Ну Погоди!', 'Бриллиантовая рука']

    def test_add_book_in_favorites_nupogodi_add(self, add_one_book_every_genre):
        add_one_book_every_genre.add_book_in_favorites('Ну Погоди!')
        assert add_one_book_every_genre.favorites == ['Ну Погоди!']

    def test_delete_book_from_favorites_nupogodi_one(self, add_one_book_every_genre):
        add_one_book_every_genre.add_book_in_favorites('Ну Погоди!')
        add_one_book_every_genre.add_book_in_favorites('Бриллиантовая рука')
        add_one_book_every_genre.delete_book_from_favorites('Ну Погоди!')
        assert add_one_book_every_genre.favorites == ['Бриллиантовая рука']

    def test_get_list_of_favorites_books_three_list(self, add_one_book_every_genre):
        add_one_book_every_genre.add_book_in_favorites('Бриллиантовая рука')
        add_one_book_every_genre.add_book_in_favorites('Собака баскервилей')
        add_one_book_every_genre.delete_book_from_favorites('Ну Погоди!')
        assert len(add_one_book_every_genre.favorites) == 2

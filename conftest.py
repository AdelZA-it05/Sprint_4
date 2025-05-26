import pytest

# класс BooksCollector, в котором реализован конструктор и методы
from main import BooksCollector


# фикстуры которые возвращают жанры: 'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'

@pytest.fixture(scope = 'session')
def sciencefiction():
    sciencefiction = 'Фантастика'
    return sciencefiction

@pytest.fixture(scope = 'session')
def horror():
    horror = 'Ужасы'
    return horror

@pytest.fixture(scope = 'session')
def detectives():
    detectives = 'Детективы'
    return detectives

@pytest.fixture(scope = 'session')
def cartoons():
    cartoons = 'Мультфильмы'
    return cartoons

@pytest.fixture(scope = 'session')
def comedies():
    comedies = 'Комедии'
    return comedies

@pytest.fixture(scope = 'function')
def add_instance_collector():
    add_instance_collector = BooksCollector()
    return add_instance_collector

# фикстура, которая добавляет любые две книги
@pytest.fixture
def add_two_books(add_instance_collector):
    add_instance_collector.add_new_book('Гордость и предубеждение и зомби')
    add_instance_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_two_books = add_instance_collector
    return add_two_books

# фикстура, возвращает книгу жанра 'Фантастика'
@pytest.fixture
def add_one_sciencefiction_book(add_instance_collector, sciencefiction):
    add_instance_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_instance_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', sciencefiction)
    add_one_sciencefiction_book = add_instance_collector
    return add_one_sciencefiction_book

# фикстура, добавляет по одной книге в каждом жанре
@pytest.fixture
def add_one_book_every_genre(add_instance_collector, sciencefiction, horror, detectives, cartoons, comedies):
    add_instance_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_instance_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', sciencefiction)
    add_instance_collector.add_new_book('Собака баскервилей')
    add_instance_collector.set_book_genre('Собака баскервилей', horror)
    add_instance_collector.add_new_book('Мой личный враг')
    add_instance_collector.set_book_genre('Мой личный враг', detectives)
    add_instance_collector.add_new_book('Ну Погоди!')
    add_instance_collector.set_book_genre('Ну Погоди!', cartoons)
    add_instance_collector.add_new_book('Бриллиантовая рука')
    add_instance_collector.set_book_genre('Бриллиантовая рука', comedies)
    add_one_book_every_genre = add_instance_collector
    return add_one_book_every_genre

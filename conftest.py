import pytest
import genre_list


# класс BooksCollector, в котором реализован конструктор и методы
from main import BooksCollector

@pytest.fixture(scope = 'function')
def add_instance_collector():
    add_instance_collector = BooksCollector()
    return add_instance_collector

# фикстура, возвращает книгу жанра 'Фантастика'
@pytest.fixture
def add_one_sciencefiction_book(add_instance_collector):
    add_instance_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_instance_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre_list.sciencefiction)
    add_one_sciencefiction_book = add_instance_collector
    return add_one_sciencefiction_book

# фикстура, добавляет по одной книге в каждом жанре
@pytest.fixture
def add_one_book_every_genre(add_instance_collector):
    add_instance_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_instance_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre_list.sciencefiction)
    add_instance_collector.add_new_book('Собака баскервилей')
    add_instance_collector.set_book_genre('Собака баскервилей', genre_list.horror)
    add_instance_collector.add_new_book('Мой личный враг')
    add_instance_collector.set_book_genre('Мой личный враг', genre_list.detectives)
    add_instance_collector.add_new_book('Ну Погоди!')
    add_instance_collector.set_book_genre('Ну Погоди!', genre_list.cartoons)
    add_instance_collector.add_new_book('Бриллиантовая рука')
    add_instance_collector.set_book_genre('Бриллиантовая рука', genre_list.comedies)
    add_one_book_every_genre = add_instance_collector
    return add_one_book_every_genre

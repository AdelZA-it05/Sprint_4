import pytest
from dataclasses import dataclass


# класс BooksCollector, в котором реализован конструктор и методы
from main import BooksCollector

@dataclass
class Genrelist:
    genre: str
    genre_name: str


sciencefiction = Genrelist('sciencefiction', 'Фантастика')
horror = Genrelist('horror', 'Ужасы')
detectives = Genrelist('detectives', 'Детективы')
cartoons = Genrelist('cartoons', 'Мультфильмы')
comedies = Genrelist('comedies', 'Комедии')



@pytest.fixture(scope = 'function')
def add_instance_collector():
    add_instance_collector = BooksCollector()
    return add_instance_collector

# фикстура, возвращает книгу жанра 'Фантастика'
@pytest.fixture
def add_one_sciencefiction_book(add_instance_collector):
    add_instance_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_instance_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', sciencefiction.genre_name)
    add_one_sciencefiction_book = add_instance_collector
    return add_one_sciencefiction_book

# фикстура, добавляет по одной книге в каждом жанре
@pytest.fixture
def add_one_book_every_genre(add_instance_collector):
    add_instance_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_instance_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', sciencefiction.genre_name)
    add_instance_collector.add_new_book('Собака баскервилей')
    add_instance_collector.set_book_genre('Собака баскервилей', horror.genre_name)
    add_instance_collector.add_new_book('Мой личный враг')
    add_instance_collector.set_book_genre('Мой личный враг', detectives.genre_name)
    add_instance_collector.add_new_book('Ну Погоди!')
    add_instance_collector.set_book_genre('Ну Погоди!', cartoons.genre_name)
    add_instance_collector.add_new_book('Бриллиантовая рука')
    add_instance_collector.set_book_genre('Бриллиантовая рука', comedies.genre_name)
    add_one_book_every_genre = add_instance_collector
    return add_one_book_every_genre

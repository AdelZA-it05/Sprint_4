# Sprint_4

YandexPraktikum Sprint_4

Список тестов:
test_add_new_book_add_two_books - поверка метода add_new_book - после двух вызовов метода добавилось две книги, количество элементов в словаре books_genre == 2
test_add_new_book_add_one_book - поверка метода add_new_book - добавилась одна книга, количество элементов в словаре books_genre == 1, с использованием параметризации
test_set_book_genre_add_correct - проверка метода set_book_genre - в словаре books_genre значение по ключу наименование книги == жанру заданному при вызове метода
test_set_book_genre_add_correct1 - проверка метода set_book_genre с использованием параиетризации
test_get_book_genre_from_another_book - проверка метода get_book_genre - метод возвращает жанр книги, в тесте метод вызван как параметр метода set_book_genre
test_get_books_with_specific_genre_one - проверка метода get_books_with_specific_genre, в тесте проверка возвращаемый жанр соответствует ожидаемому: 'Ужасы'
test_get_books_genre_dict_value - проверка метода get_books_genre, в тесте проверка, что словарь фикстуры add_one_book_every_genre == ожидамому значению
test_get_books_for_children_list_value - проверка метода get_books_for_children, в тесте проверка на основании фикситуры add_one_book_every_genre
test_add_book_in_favorites_nupogodi_add - проверка метода add_book_in_favorites, в тесте проверка что в списке favorites только добавленное методом значение
test_delete_book_from_favorites_nupogodi_one - проверка метода delete_book_from_favorites, в тесте проверка что в списке favorites только не удалённое значение
test_get_list_of_favorites_books_three_list - проверка метода get_list_of_favorites_books, в тесте проверка что, в списке favorites (добавленно - удалено) количество записей

Фикстуры:
sciencefiction, horror, detectives, cartoons, comedies - жанры книг
add_instance_collector - экземпляр класса BooksCollector
add_two_books - добавление двух книг
add_one_sciencefiction_book - добавление книги жанра: 'Фантастика'
add_one_book_every_genre - добавление по одной книге из каждого жанра

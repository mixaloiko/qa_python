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
        # словарь books_genre, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate_add_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилась 1 книга, так как был дубликат
        # словарь books_genre, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_incorrect_length_add_no_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('')
        collector.add_new_book('Гордость и предубеждение и зомби и Гордость и предубеждение и зомби')

        # проверяем, что добавилось 0 книга, так как обе не подходят по верхней и нижней границе длинны
        # словарь books_genre, который нам возвращает метод get_books_rating, имеет длину 0
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_genre_assigned_to_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # проверяем, что книге назначен жанр
        # словарь books_genre по названию книги возвращает нужный жанр
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_genre_not_assigned_to_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')

        # проверяем, что книге не назначен жанр Роман
        # словарь books_genre по названию книги возвращает уже присвоенный ранее жанр
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_book_does_not_exist(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби 1', 'Ужасы')

        # проверяем, что книге не назначен жанр, так как такой книге в списке нет
        # словарь books_genre по названию книги возвращает None
        assert collector.get_book_genre('Гордость и предубеждение и зомби 1') is None

    def test_get_book_genre_book_exists(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что по существующей книге возвращается жанр
        # словарь books_genre по названию книги возвращает жанр
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is not None

    def test_get_book_genre_book_does_not_exist(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что такой книги нет
        # словарь books_genre по названию книги возвращает None
        assert collector.get_book_genre('Гордость и предубеждение и зомби 1') is None

    def test_get_books_with_specific_genre_return_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # проверяем, что существующая книга по существующему жанру выводится
        # метод get_books_with_specific_genre по названию жанра возвращает список книг этого жанра
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

    def test_get_books_with_specific_genre_return_empty_list_if_wrong_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # проверяем, что существующая книга не выводится по другому жанру
        # метод get_books_with_specific_genre по названию другого жанра возвращает пустой список
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_return_empty_list_if_non_existing_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # проверяем, что существующая книга не выводится по несуществующему жанру
        # метод get_books_with_specific_genre по названию несуществующего жанра возвращает пустой список
        assert collector.get_books_with_specific_genre('Роман') == []

    def test_get_books_genre_return_books_genre_dict(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу и жанр
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # словарь books_genre содержит добавленную книгу
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы'}

    def test_get_books_for_children_return_book_names(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги и жанр
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')

        # метод get_books_for_children возвращает подходящие книги
        assert collector.get_books_for_children() == ['Винни Пух']

    def test_add_book_in_favorites_book_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу в favorites
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # список favorites содержит книгу
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_book_not_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу в favorites
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Винни Пух')

        # список favorites не содержит книгу
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_deleted(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги в favorites
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        #проверяем, что книги добавились
        assert len(collector.get_list_of_favorites_books()) == 2

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга удалилась
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_list_favorites_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги в favorites
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        #проверяем, что книги добавились
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']








    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
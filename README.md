# qa_python

Написано 17 тестов:
1. test_add_new_book_add_two_books - проверяет добавление книг в список;
2.test_add_new_book_duplicate_add_one_book - проверяет, что нельзя дважды добавить одну и ту же книгу в список;
3.test_add_new_book_incorrect_length_add_no_books - проверяет валидацию названия книги по верхней и нижней границе;
4. test_set_book_genre_genre_assigned_to_book - проверяет, что книге присваивается нужный жанр;
5.test_set_book_genre_genre_not_assigned_to_book - проверяет, что книге не присваивается неверный жанр;
6. test_set_book_genre_book_does_not_exist - проверяет, что не присваивается книге жанр, если такой книги в списке нет;
7. test_get_book_genre_book_exists - проверяет, что выводит жанр по названию книги;
8. test_get_book_genre_book_does_not_exist - проверяет, что не выводит жанр по несуществующей книге;
9. test_get_books_with_specific_genre_return_books - проверяет, что выводится книга по существующему жанру;
10. test_get_books_with_specific_genre_return_empty_list_if_wrong_genre - проверяет, что существующая книга не выводится по несоответствующему ей жанру;
11. test_get_books_with_specific_genre_return_empty_list_if_non_existing_genre - проверяет, что не выводится список книг по несуществующему жанру;
12.test_get_books_genre_return_books_genre_dict - проверяет, добавление книги и жанра в словарь;
13. test_get_books_for_children_return_book_names - проверяем, что возвращает книги, которые соответствуют для детского возраста;
14. test_add_book_in_favorites_book_added - проверяет, добавляется ли книга в список favorites_book;
15. test_add_book_in_favorites_book_not_added - проверяет, что не добавляет несуществующую книгу в список favorites_book;
16.test_delete_book_from_favorites_book_deleted - проверяет, что книга удаляется из списка favorites_book;
17. test_get_list_of_favorites_books_list_favorites_books - проверка вывода списка favorites_book
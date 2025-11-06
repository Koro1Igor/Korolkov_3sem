from operator import itemgetter

class Book:
    """Книга"""
    def __init__(self, id, title, price, lib_id):
        self.id = id
        self.title = title
        self.price = price
        self.lib_id = lib_id


class Library:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookLibrary:
    """Связь книги и библиотеки (многие-ко-многим)"""
    def __init__(self, lib_id, book_id):
        self.lib_id = lib_id
        self.book_id = book_id


# --- Данные ---
libs = [
    Library(1, 'Академическая библиотека'),
    Library(2, 'Архивная библиотека №1'),
    Library(3, 'Городская библиотека'),
    Library(4, 'Областная библиотека'),
    Library(5, 'Арт-библиотека')
]

books = [
    Book(1, 'Алые паруса', 450, 1),
    Book(2, 'Преступление и наказание', 550, 1),
    Book(3, 'Мастер и Маргарита', 700, 3),
    Book(4, 'Война и мир', 600, 3),
    Book(5, 'Анна Каренина', 500, 2),
    Book(6, '1984', 400, 4),
    Book(7, 'А зори здесь тихие', 480, 5),
]

books_libs = [
    BookLibrary(1, 1),
    BookLibrary(1, 2),
    BookLibrary(2, 5),
    BookLibrary(3, 3),
    BookLibrary(3, 4),
    BookLibrary(4, 6),
    BookLibrary(5, 7),
    # связи многие-ко-многим
    BookLibrary(1, 3),
    BookLibrary(2, 4),
    BookLibrary(5, 1)
]


def main():
    """Основная функция"""

    # --- Один-ко-многим ---
    one_to_many = [(b.title, b.price, l.name)
                   for l in libs
                   for b in books
                   if b.lib_id == l.id]

    # --- Многие-ко-многим ---
    many_to_many_temp = [(l.name, bl.lib_id, bl.book_id)
                         for l in libs
                         for bl in books_libs
                         if l.id == bl.lib_id]

    many_to_many = [(b.title, b.price, lib_name)
                    for lib_name, lib_id, book_id in many_to_many_temp
                    for b in books if b.id == book_id]

    # === Задание Г1 ===
    print('Задание Г1')
    res_1 = {}
    for l in libs:
        if l.name.startswith('А'):
            # Список книг библиотеки
            l_books = list(filter(lambda i: i[2] == l.name, one_to_many))
            book_titles = [x for x, _, _ in l_books]
            res_1[l.name] = book_titles
    print(res_1)

    # === Задание Г2 ===
    print('\nЗадание Г2')
    res_2_unsorted = []
    for l in libs:
        l_books = list(filter(lambda i: i[2] == l.name, one_to_many))
        if len(l_books) > 0:
            prices = [price for _, price, _ in l_books]
            max_price = max(prices)
            res_2_unsorted.append((l.name, max_price))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    # === Задание Г3 ===
    print('\nЗадание Г3')
    res_3 = sorted(many_to_many, key=itemgetter(2))
    print(res_3)


if __name__ == '__main__':
    main()

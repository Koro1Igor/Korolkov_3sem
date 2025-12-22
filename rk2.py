from operator import itemgetter


class Book:
    def __init__(self, id, title, price, shop_id):
        self.id = id
        self.title = title
        self.price = price
        self.shop_id = shop_id


class Shop:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookShop:
    def __init__(self, shop_id, book_id):
        self.shop_id = shop_id
        self.book_id = book_id


# ---------- ФУНКЦИИ ДЛЯ ТЕСТИРОВАНИЯ ----------

def get_one_to_many(books, shops):
    """Связь один-ко-многим"""
    return [
        (b.title, b.price, s.name)
        for s in shops
        for b in books
        if b.shop_id == s.id
    ]


def get_shops_starting_with_a(books, shops):
    """Задание Г1"""
    one_to_many = get_one_to_many(books, shops)
    result = {}

    for s in shops:
        if s.name.startswith('А'):
            shop_books = [title for title, _, shop in one_to_many if shop == s.name]
            result[s.name] = shop_books

    return result


def get_max_price_by_shop(books, shops):
    """Задание Г2"""
    one_to_many = get_one_to_many(books, shops)
    result = []

    for s in shops:
        prices = [price for _, price, shop in one_to_many if shop == s.name]
        if prices:
            result.append((s.name, max(prices)))

    return sorted(result, key=itemgetter(1), reverse=True)


def get_books_shops_many_to_many(books, shops, books_shops):
    """Задание Г3"""
    temp = [
        (s.name, bs.book_id)
        for s in shops
        for bs in books_shops
        if s.id == bs.shop_id
    ]

    return sorted(
        [(b.title, b.price, shop)
         for shop, book_id in temp
         for b in books if b.id == book_id],
        key=itemgetter(2)
    )

import unittest
from rk2 import (
    Book, Shop, BookShop,
    get_shops_starting_with_a,
    get_max_price_by_shop,
    get_books_shops_many_to_many
)


class TestBookShop(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных (TDD)"""
        self.shops = [
            Shop(1, 'Альфа-Книги'),
            Shop(2, 'Арбатская книга'),
            Shop(3, 'Город книг'),
        ]

        self.books = [
            Book(1, 'Алые паруса', 450, 1),
            Book(2, 'Преступление и наказание', 550, 1),
            Book(3, 'Мастер и Маргарита', 700, 3),
        ]

        self.books_shops = [
            BookShop(1, 1),
            BookShop(1, 2),
            BookShop(3, 3),
            BookShop(1, 3),
        ]

    # ---------- ТЕСТ 1 ----------
    def test_shops_starting_with_a(self):
        result = get_shops_starting_with_a(self.books, self.shops)
        self.assertIn('Альфа-Книги', result)
        self.assertEqual(len(result['Альфа-Книги']), 2)

    # ---------- ТЕСТ 2 ----------
    def test_max_price_by_shop(self):
        result = get_max_price_by_shop(self.books, self.shops)
        self.assertEqual(result[0], ('Город книг', 700))

    # ---------- ТЕСТ 3 ----------
    def test_many_to_many_relation(self):
        result = get_books_shops_many_to_many(
            self.books, self.shops, self.books_shops
        )
        self.assertIn(('Мастер и Маргарита', 700, 'Альфа-Книги'), result)


if __name__ == '__main__':
    unittest.main()
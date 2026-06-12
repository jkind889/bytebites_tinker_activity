import unittest
from models import Food, Catalog, Transaction


class TestByteBites(unittest.TestCase):

    def test_order_total(self):
        burger = Food("Burger", 8.99, "entrees", 4.5)
        soda = Food("Soda", 2.50, "drinks", 4.0)
        fries = Food("Fries", 3.00, "sides", 4.2)

        transaction = Transaction("t001", "c001")
        transaction.add_item(burger)
        transaction.add_item(soda)
        transaction.add_item(fries)

        self.assertAlmostEqual(transaction.compute_total(), 14.49)

    def test_empty_order_total(self):
        transaction = Transaction("t002", "c001")
        self.assertEqual(transaction.compute_total(), 0.0)

    def test_filter_menu_items_by_category(self):
        catalog = Catalog()
        catalog.add_item(Food("Lemonade", 2.99, "drinks", 4.7))
        catalog.add_item(Food("Iced Tea", 2.49, "drinks", 4.3))
        catalog.add_item(Food("Chips", 1.99, "snacks", 3.8))
        catalog.add_item(Food("Cookie", 1.50, "snacks", 4.1))
        catalog.add_item(Food("Sandwich", 6.99, "entrees", 4.6))

        drinks = catalog.filter_by_category("drinks")

        self.assertEqual(len(drinks), 2)
        self.assertTrue(all(item.category == "drinks" for item in drinks))
        drink_names = [item.name for item in drinks]
        self.assertIn("Lemonade", drink_names)
        self.assertIn("Iced Tea", drink_names)


if __name__ == "__main__":
    unittest.main()

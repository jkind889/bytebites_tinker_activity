# Food, Catalog, Transactions, Customer


class Food:
    def __init__(self, name: str, price: float, category: str, rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.rating = rating

    def get_details(self) -> str:
        return f"{self.name} | ${self.price:.2f} | {self.category} | Rating: {self.rating}"


class Catalog:
    def __init__(self):
        self.items: list[Food] = []

    def add_item(self, food: Food) -> None:
        self.items.append(food)

    def remove_item(self, food: Food) -> None:
        self.items.remove(food)

    def filter_by_category(self, category: str) -> list[Food]:
        return [item for item in self.items if item.category == category]

    def get_all_items(self) -> list[Food]:
        return list(self.items)


class Transaction:
    def __init__(self, transaction_id: str, customer_id: str):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.items: list[Food] = []

    def add_item(self, food: Food) -> None:
        self.items.append(food)

    def remove_item(self, food: Food) -> None:
        self.items.remove(food)

    def compute_total(self) -> float:
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, customer_id: str, first_name: str, last_name: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.purchase_history: list[Transaction] = []

    def place_order(self, transaction: Transaction) -> None:
        self.purchase_history.append(transaction)

    def get_purchase_history(self) -> list[Transaction]:
        return list(self.purchase_history)

    def is_verified(self) -> bool:
        return len(self.purchase_history) > 0

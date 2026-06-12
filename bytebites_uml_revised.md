# ByteBites UML Class Diagram (Revised)

```mermaid
classDiagram
    class Food {
        +String name
        +float price
        +String category
        +float rating
        +get_details() String
    }

    class Catalog {
        +List~Food~ items
        +add_item(food: Food) void
        +remove_item(food: Food) void
        +filter_by_category(category: String) List~Food~
        +get_all_items() List~Food~
    }

    class Transaction {
        +String transaction_id
        +String customer_id
        +List~Food~ items
        +add_item(food: Food) void
        +remove_item(food: Food) void
        +compute_total() float
    }

    class Customer {
        +String customer_id
        +String first_name
        +String last_name
        +List~Transaction~ purchase_history
        +place_order(transaction: Transaction) void
        +get_purchase_history() List~Transaction~
        +is_verified() bool
    }

    %% Relationships
    Catalog "1" *-- "0..*" Food : contains
    Customer "1" *-- "0..*" Transaction : has history of
    Transaction "1..*" --> "1" Customer : belongs to
    Transaction "1" *-- "1..*" Food : includes
```

## Changes from Original

- **Composition arrows (`*--`)** on `Catalog→Food`, `Customer→Transaction`, and `Transaction→Food` — these objects are owned by their parent and don't exist independently.
- **Fixed `Transaction → Customer` multiplicity** — changed from informal `many` to proper `1..*` notation.
- **Direction consistency** — all arrows point from owner to owned, or from dependent to its target.

## User Flow

```
1. Customer browses Catalog
   └── Catalog.filter_by_category() or get_all_items()

2. Customer selects Food items
   └── Transaction.add_item() for each selection

3. Customer reviews order
   └── Transaction.compute_total()

4. Customer places order
   └── Customer.place_order(transaction)
   └── Transaction appended to Customer.purchase_history

5. System verifies customer
   └── Customer.is_verified() checks purchase_history is non-empty
```

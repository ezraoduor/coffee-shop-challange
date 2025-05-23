
# Coffee Shop Challenge 

A Python project modeling a coffee shop domain with three core entities: **Customer**, **Coffee**, and **Order**.  
This project demonstrates object relationships, data validation, and aggregate calculations through OOP.

---

## Installation & Setup

1. **Clone the repo**
   ```bash
   git clone [text](https://github.com/ezraoduor/coffee-shop-challange)
   cd coffee-shop-challenge

2. **Install dependencies and activate environment**

pipenv install
pipenv shell

## Project Structure

Coffee_Shop_Challenge/

customer.py

coffee.py

order.py

main.py

README.md

Features Overview

## Project Overview

This challenge implements a simple coffee shop domain with these models and features:

- **Customer**: Stores customer data (name) with validation, manages orders and coffees.
- **Coffee**: Stores coffee data (immutable name), tracks related orders and customers.
- **Order**: Links a customer and coffee with a price, validating types and value ranges.

---

## Features

### Models & Initializers
- **Customer**: Validates name (string, 1–15 characters).
- **Coffee**: Validates name (string, minimum 3 characters), immutable after creation.
- **Order**: Accepts `Customer`, `Coffee`, and `price` (float, 1.0–10.0), price immutable.

### Relationships
- `Order.customer` and `Order.coffee` return associated instances.
- `Customer.orders()` and `Customer.coffees()` return related orders and unique coffees.
- `Coffee.orders()` and `Coffee.customers()` return related orders and unique customers.

### Aggregates & Associations
- `Customer.create_order(coffee, price)`: Creates and links an order.
- `Coffee.num_orders()`: Returns total orders for the coffee.
- `Coffee.average_price()`: Returns average price of orders or 0 if none.

### Bonus Feature
- `Customer.most_aficionado(coffee)`: Class method returning the customer who spent the most on a given coffee.

---
## Author
Ezra Oduor

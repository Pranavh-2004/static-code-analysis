"""Inventory System Module
Performs basic inventory management: add, remove, query, save, and load items.
Includes static-analysis-based improvements for readability, safety, and security.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

# Global variable for in-memory stock data
stock_data: Dict[str, int] = {}


def add_item(item: str = "default", qty: int = 0, logs: Optional[List[str]] = None) -> None:
    """Add a given quantity of an item to the stock and record the operation in logs."""
    if not item:
        return

    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str) or not isinstance(qty, int):
        raise ValueError("Invalid item name or quantity type.")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int) -> None:
    """Remove a given quantity of an item from the stock, deleting it if quantity ≤ 0."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as exc:
        print(f"Warning: Tried to remove non-existent item '{item}'. ({exc})")


def get_qty(item: str) -> int:
    """Return the quantity of a given item. Raises KeyError if missing."""
    return stock_data[item]


def load_data(file_path: str = "inventory.json") -> None:
    """Load stock data from a JSON file."""
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Starting with empty inventory.")


def save_data(file_path: str = "inventory.json") -> None:
    """Save current stock data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data() -> None:
    """Print a formatted report of all items and their quantities."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return a list of items whose stock is below the given threshold."""
    return [item for item, quantity in stock_data.items() if quantity < threshold]


def main() -> None:
    """Demonstrate sample inventory operations."""
    logs: List[str] = []
    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    remove_item("apple", 3)
    remove_item("orange", 1)

    try:
        print(f"Apple stock: {get_qty('apple')}")
    except KeyError:
        print("Item 'apple' not found.")

    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

    # Secure alternative to eval demonstration
    code_snippet = "print('safe evaluation example')"
    print(code_snippet)


if __name__ == "__main__":
    main()
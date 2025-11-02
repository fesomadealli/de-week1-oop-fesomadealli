
# 📚 Library Mini Project (libmini)

A Python-based simulation of a library system that demonstrates core **Object-Oriented Programming (OOP)** principles — including **Encapsulation**, **Inheritance**, and **Polymorphism** — along with the **Factory Pattern** for flexible object creation.

The system models a **Librarian** managing **Books** and **Members**, with loan receipts sent via configurable **Notifiers** (Email or SMS).

---

## 🧠 OOP Concepts in Action

### 🔹 Class
A class is a blueprint for creating objects. It defines attributes and behaviors.

```python
class Book:
    def __init__(self, title):
        self.title = title
```

### 🔹 Object / Instance
An object is a concrete item created from a class.

```python
book1 = Book("1984")  # book1 is an instance of Book
```

### 🔹 Encapsulation
Encapsulation bundles data and methods inside a class, hiding internal logic.

Example:  
A `Library` class might store private lists like `_catalog`, `_loans`, and expose public methods like `add_book()`, `borrow()`, `return_book()`.

### 🔹 Inheritance
Inheritance allows a class to reuse or extend behavior from another.

```python
class Notifier:
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print("Sending Email:", message)
```

### 🔹 Polymorphism
Polymorphism enables different classes to define the same method name with distinct behavior.

```python
notifier.send("Your book has been borrowed.")
# Works for both EmailNotifier and SMSNotifier
```

---

## 🏭 Factory Pattern Overview

### What It Solves
Instead of using complex `if-elif-else` chains to select objects (e.g., menu categories in a kitchen), the Factory Pattern centralizes object creation based on input.

### In This Project
```python
notifier = NotifierFactory().create("email")
```

This replaces manual instantiation like `EmailNotifier()` and allows switching between notification types without changing core logic.

📍 Located in `notify.py`, `NotifierFactory` returns the appropriate notifier object (`EmailNotifier` or `SMSNotifier`) based on the `kind` requested.

---

## 🚀 How to Run

This project uses [Poetry](https://python-poetry.org/) for dependency management.

From the root `libmini` directory, run:

```bash
poetry run python cli.py
```

This will:
- Create 7 `Person` objects from the `de_c4` dictionary
- Convert the last person into a `Librarian` using `make_librarian()`
- Randomly select 3 people to become `Members` via `update_membership()`
- Add 3 books using the `add_book()` method
- Simulate a book loan using `borrow()` from the `Library` class

---

## 🧾 Additional Notes

- Only a `Person` can become a `Member` or `Librarian` (via `super().__init__`)
- Uses **Pydantic** for input validation (e.g., `EmailStr` for email fields)
- Librarians cannot borrow or return books
- Book availability is checked before borrowing
- Availability is updated after borrow/return
- Only the original borrower can return a book
- Loan records are updated on both `Library` and `Member` sides

---

## 📂 Project Structure

```
libmini/
  libmini/
    __init__.py
    models.py       # Person, Member, Librarian, Book, Library
    notify.py       # Notifier interface + Email/SMS + NotifierFactory
    cli.py          # CLI demo entrypoint
  README.md         # Project overview and OOP concepts
  tests/            # Optional test suite
  requirements.txt  # Minimal dependencies
  poetry.lock
  pyproject.toml
  .gitignore
```

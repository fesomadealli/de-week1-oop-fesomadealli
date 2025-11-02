
## ------ PORJECT SUMMARY ------

### Project Title:  Library Mini Project (libmini)

This project demonstrates core **Object-Oriented Programming (OOP)** principles in Python — including **Encapsulation**, **Inheritance**, and **Polymorphism** — along with the **Factory Pattern** for flexible object creation.  

It simulates a small library system where a **Librarian** manages **Books** and **Members**, while using different **Notifiers** (Email or SMS) to send loan receipts.

## ----- OOP CONCEPT DEFINITIONS ------ 

- Class — a blueprint for creating objects. 
- Object/Instance — a concrete item created from a class. 
- Encapsulation — bundling data and methods; hiding internal details behind a clean interface. 
- Inheritance — deriving a new class from an existing one to reuse/extend behavior. 
- Polymorphism — same method name, different behaviors depending on the object. 

### **Class**
A **class** is a **blueprint** for creating objects.  
It defines what data/properties (attributes) the object will have and actions (methods) the object will take.  
Example:  

```
class Book:
    def __init__(self, title):
        self.title = title
```

Here, Book is a class that describes what every book object will look like.

### Object / Instance
An object (or instance) is a **concrete item** created from a class.
Example:

```
book1 = Book("1984")
book1 is an instance of the Book class.
```

### Encapsulation
Encapsulation means **bundling data and methods** together inside a class and **hiding internal details** from outside code.
This keeps the internal logic safe and easy to manage.
Example:
A Library class might have private lists of books (_catalog), book loans (_loans) and members, exposing only public methods like add_book(), borrow() and return_book().

### Inheritance
Inheritance allows you to create a new class from an existing one to reuse or extend its behavior.
Example:

```
class Notifier:
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print("Sending Email:", message)
```        
EmailNotifier inherits from Notifier and overrides its behavior.

### Polymorphism
Polymorphism means using the same method name for different behaviors depending on the object calling it.
Example:
**Both** *EmailNotifier* and *SMSNotifier* have a send() method — but each **behaves differently**.
This lets you call **.send()** on any notifier without caring which one it is.

## ---- FACTORY PATTERN ----
### What is the Factory Pattern?
The Factory Pattern is a design pattern that provides a central place to create objects without exposing the creation logic to the client code. 

Originally to switch between items you need if-else statements that can grow quite complex as the project need expands.
Say *Salome_Kitchen* has menu category for *Swallow* and *Rice* meals. 
To get a meal, we need to loop through each meals in the *Swallow* category to find our desired swallow (say Eba)
Similarly, same pattern repeats for *Rice* category.

Depending on the variants of swallow and rice meals, that would be a significant amount of if-el-f-else statements.
Now add *Soups* *Protein* *Drink* and *Takeout Packaging* to the Kitchen categories and imagine the volume of ifs elifs and elses

Factory Pattern takes this out efficiently.
It lets you decide which class to instantiate at runtime, based on input or configuration.

### Why use it in this project?
Instead of writing:
```
notifier = EmailNotifier()
```
We can write:
```
notifier = NotifierFactory().create("email")
```
Now the program can easily switch between **Email** and **SMS** notifications 
We do this just by changing the input, without altering the rest of the code.

### Where it’s used
In this project, ```NotifierFactory``` in ```notify.py``` is responsible for returning the right notifier object (EmailNotifier or SMSNotifier) depending on the ```kind``` requested.

## ---- HOW TO RUN ----
This poetry use ```Poetry``` 
So, from the main libmini directory, run the CLI using this command:
```
poetry run python cli.py
```
This will:

- Create a Person: Using the Person class in ```models.py``` it creates 7 instances of a Person from the de-c4 dictionary (de-c4 is short for variable name Data_Epic_Cohort_4)
- Create the Librarian: Using the last entry the de-c4 dictionary and calling the ```make_librarian``` method from ```models.py```. It then deletes the last in de-c4 to make sure we cannot use it to make a member later.
- Create 3 Members: Select three names at random from the list of person objects. Then it calls ```update_membership``` method to turn them into members using the Member class.
- Add 3 books: Using ```add_book``` method from Librarian class
- Borrow Book: Using borrow method in Library and supplying Member and Book info. 

### Extra Things To Know About:
- Cannot create a Member or Librarian object that wasnt already a Person object since only a person can be either (hence the use of ```super().__init__``` in parts of the code)
- Uses pydantic to validate inputs. For instance, all objects must supply valid emails where required (pydantic *EmailStr* validator assists with checking this)
- Librarians cannot borrow or return books
- Check Book availabilty before a borrow is made
- Update a book's availabilty after the borrow or a return_book method is called 
- Confirm that the person returning the book borrowed it in the first place
- Updates Book loans both on the Library side (_loans and loan_register) and the Member side (book_loans)



## ------ 📂 Project Structure ------
```
libmini/
  libmini/
    __init__.py
    models.py       # Person, Member, Librarian, Book, Library
    notify.py       # Notifier interface + Email/SMS + NotifierFactory
    cli.py          # demo entrypoint (python -m libmini.cli)
  README.md         # include OOP definitions BEFORE code samples
  tests/            # optional this week (see Bonus)
  requirements.txt  # minimal (none strictly required)
  poetry.lock
  pyproject.toml
  .gitignore
```












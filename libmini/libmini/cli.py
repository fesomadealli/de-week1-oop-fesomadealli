
from models import Data_Epic_Cohort_4, Person, Librarian, Library, Book
from notify import NotifierFactory
import random

def main():
    """_summary_
    The main function to demonstrate the library management system
    and notification sending using the factory pattern.
    """
    library = Library()
    factory = NotifierFactory()

    persons = []
    for entry in Data_Epic_Cohort_4:
        for name, email in entry.items():
            persons.append(Person(name=name, email=email))
            print(f"{name} person created with email: {email}")
  
    librarian = Librarian(persons[-1])
    print(f"Liberarian is created, {librarian.name} with email: {librarian.email}")
    del persons[-1] 
    
    books = [
        Book(title="Anifowoshe The Aeroplane Stopper", author="K1 De Ultimate", isbn="978-0134853987"),
        Book(title="How to Buy a Yacht With 2 Dollars", author="Yu Krim Inahl", isbn="978-0123456789"), 
        Book(title="Getting Married With Forty Naira", author="O.T Law", isbn="978-0132350884")
        ]

    for book in books:
        librarian.add_books(book, library)
        print(f"{book.title} by {book.author} (ISBN: {book.isbn}) is added to library catalog.")
    
    for bks in library.book_shelf:
        print(" -", bks)

    print("Available books in library:\n", library.available_books)
    print("Book Catalog:\n", library._catalog)
    
    # ====== REGISTER MEMBERS ======
    tobe_members = random.sample(persons, 3)
    added_members = []
    for new_member in tobe_members:  
        new_member = librarian.register_member(new_member, library)
        added_members.append(new_member)
        print(f"Member registered: {new_member.name}")

    member_1, member_2, member_3 = added_members[0:3]
    
    # ====== SEND RECEIPTS VIA FACTORY ======
    email_notifier = factory.create("email")
    sms_notifier = factory.create("sms")
    
    # ====== BORROW FLOW ======
    library.borrow(book_isbn=books[0].isbn, member=member_1)
    library.borrow(book_isbn=books[1].isbn, member=member_2)
    library.borrow(book_isbn=books[1].isbn, member=member_3)    # should fail cause already borrowed by member_2
    library.borrow(book_isbn="123-45667890", member=member_3)   # should fail cause book not in catalog
    
    # print("\n Current loan register:")  # After Book Loans
    # library._loans
    
    print("\n Mail Notifications for Book Borrowing:")    
    print(email_notifier.send(to=member_1.email, message=f"Receipt: You borrowed '{books[0].title}' by '{books[0].author}'"))
    print(email_notifier.send(to=member_2.email, message=f"Receipt: You borrowed '{books[1].title}' by '{books[1].author}'"))
    
    print("Member Loans After borrowing:\n")
    print(" -", library.member_loans(member_1))
    print(" -", library.member_loans(member_2))
    print(" -", library.member_loans(member_3))
    
    # ====== RETURN FLOW ======
    library.return_book(book_isbn=books[0].isbn, member=member_1)
    library.return_book(book_isbn=books[1].isbn, member=member_2)
    library.return_book(book_isbn=books[1].isbn, member=member_3) # should fail cause book was borrowed by member_3

    print("\n SMS Notifications for Book Returns:\n")
    print(sms_notifier.send(to=member_1.email, message=f"Receipt: You successfully returned '{books[0].title}'"))    
    print(email_notifier.send(to=member_2.email, message=f"Receipt: You successfully returned '{books[1].title}' by '{books[1].author}'"))

    print("Member Loans After borrowing:\n")
    print(" -", library.member_loans(member_1))
    print(" -", library.member_loans(member_2))
    print(" -", library.member_loans(member_3)) 

    # ====== PRINT CURRENT LOANS REGISTER ======
    print("\n Current loan register (after returns):")  # After Book Returns
    print(library._loans)
    
    # ====== PRINT AVAILABLE BOOKS ======
    print("\n Available books after Book Loans & Returns:")
    print(library.available_books)  # All books should be available now


if __name__ == "__main__":
    main()

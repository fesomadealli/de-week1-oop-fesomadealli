# Models.py
            
#     methods: 
#         # add_book(book),
#         # register_member(member), 
#         # borrow(member, isbn), 
#         # return_book(member, isbn), 
#         # member_loans(member) -> list[Book], 
#         # available_books() -> list[Book]

Data_Epic_Cohort_4 =  (
    {'Alasoluyi Oyinlola': 'alasoluyioyinlola@libmini.com'},
    {'Hezekiah Ajayi-Omoleye': 'hezekiahajayi-omoleye@libmini.com'},
    {'Salome Gabriel': 'salomegabriel@libmini.com'},
    {'Adepitan Gbenga': 'adepitangbenga@libmini.com'},
    {'Marvelous Oluwasina': 'marvelousoluwasina@libmini.com'},
    {'Alli Fesomade': 'allifesomade@libmini.com'},
    {'Unago C. Shege': 'unagocshege@libmini.com'}
)

from pydantic import BaseModel, EmailStr

   
class Book(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    title: str
    author: str
    isbn: str 
    available: bool = True
    
    def __repr__(self) -> str:
        book_status: str = "Available" if self.available else "Not Available"
        return f"Book(title={self.title} \n author: {self.author} \n isbn: {self.isbn} \n status: {book_status})" 


class Person(BaseModel):
    """_summary_
    The base class with name, email (+ __repr__)
    Uses pydantic for data validation.
    
    Args:
        BaseModel (_type_): _description_
    """
    name: str
    email: EmailStr 
    is_member: bool = False
    is_librarian: bool = False
    
    def update_membership(self, 
                          make_member: bool
                          ):
        self.is_member = make_member
        return self.is_member
    
    def make_librarian(self, 
                       make_librarian: bool
                       ): 
        self.is_librarian = make_librarian
        return self.is_librarian
      
    def __repr__(self):
        return f"Person(name={self.name!r} \n email={self.email!r} \n Membership={self.is_member!r})"


class Member(Person):
    """_summary_

    Args:
        Person (_type_): _description_
    """
    book_loans: list[Book] = []
    def __init__(self,
                 person: Person
                 ):

        super().__init__(name=person.name, 
                         email=person.email)
        
        if person.is_member or person.is_librarian: pass
        else: self.is_member = person.update_membership(True)
        
        self.book_loans: list[Book] = []    # manage borrowed books    
                
    def __repr__(self):
        return f"Member(name={self.name!r} \n email={self.email!r} \n Membership={self.is_member!r} \n Borrowed Books={self.book_loans})"
      
class Library(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """
    book_shelf: list[Book] = []
    membership_list: list[Member] = []
    loan_register: dict[EmailStr, set[str]] = {}  
    books_in_store: list[Book] = []                                # member_email -> set[isbn] 
        
    def borrow(self,
               book_isbn: str,                                      # call should proll be library.borrow(member, isbn)
               member: Member
               ):
        # check book in library catalog
        if book_isbn not in self._catalog:
            return f"Book with ISBN '{book_isbn}' not found in Library Catalog"
        else:
            book_to_borrow = self._catalog[book_isbn]
            if not book_to_borrow.available:
                return f"The book '{book_to_borrow.title}' is currently not available."
            else:
                book_to_borrow.available = False                    # mark as borrowed
                member.book_loans.append(book_to_borrow)            # add to member's loans
                if member.email not in self.loan_register:          # update library's loan register
                    self.loan_register[member.email] = set()        # Create the list first
                self.loan_register[member.email].add(book_isbn)     # add new entry
    
    def return_book(self,
                    book_isbn: str, 
                    member: Member
                    ):
        # Check if book exists in library catalog
        if book_isbn not in self._catalog:
            return f"Book with ISBN '{book_isbn}' not found in Library Catalog"
        
        book_to_return = self._catalog[book_isbn]
        
        # Check if member actually borrowed this book
        if book_to_return not in member.book_loans:
            return f"Dear {member.email}, you haven't borrowed the book '{book_to_return.title}' by {book_to_return.author}."
        
        # Update book status
        book_to_return.available = True
        
        # Remove from member's loans
        member.book_loans.remove(book_to_return)
        
        # Update library's loan register
        if member.email in self.loan_register:
            self.loan_register[member.email].discard(book_isbn)
            # Clean up empty sets
            if not self.loan_register[member.email]:
                del self.loan_register[member.email]

    @property
    def _loans(self) -> dict[str, set[str]]:                          # member_email -> set[isbn]                            # manage loans 
        return self.loan_register  
    
    @property
    def _catalog(self) -> dict[str, Book]:                             # isbn -> Book
        return {book.isbn: book for book in self.book_shelf}

    @property
    def available_books(self) -> list[Book]:
        return [book for book in self.book_shelf if book.available]
    
    @staticmethod
    def member_loans(member: 'Member'):
        if len(member.book_loans) > 0:
            return f"{member.email} loaned the following books: '\n' {member.book_loans}"
        else:
            return f"{member.email} has no current book loans"

    def __repr__(self) -> str:
        books_repr = ",\n    ".join(repr(book) for book in self.book_shelf)
        members_repr = ",\n    ".join(repr(member) for member in self.membership_list)
        
        return f"""Library(book_shelf=[
                        {books_repr}
                    ], 
                    membership_list=[
                        {members_repr}
                    ], 
                    loan_register={self.loan_register}, 
                    books_in_store={self.books_in_store}
                )"""

class Librarian(Person):
    """_summary_

    Args:
        Person (_type_): _description_
    """
    def __init__(self,
                 person: Person
                 ):

        super().__init__(name=person.name, email=person.email)
        if person.is_librarian: pass
        else: self.is_librarian = person.make_librarian(True)
        
    def register_member(self, 
                        person: Person,
                        library: Library
                        ) -> Member:
        if person.is_librarian:
            raise ValueError("Librarian cannot be registered as Member")
        new_member = Member(person)
        library.membership_list.append(new_member)
        return new_member

    def revoke_member(self, 
                      person: Person
                      ):
        self.is_member = person.update_membership(False)
        return person
    
    def add_books(self,
                  book: Book,
                  library: Library
                  ):
        # should add book to library's book_shelf
        library.book_shelf.append(book)
    
    def __repr__(self):
        if self.is_librarian: role = "Librarian"
        else: pass
        return f"Librarian(name={self.name!r} \n email={self.email!r} \n role={role})"
        
import myBooks as Book
import myCustomers as Customer
import myLoans as Loan
from myCustomers import Customers
class Library:
    def addNewBook(name, author, yearpublished, type):
        Book.Books.addBook(name, author, yearpublished, type)
    
    def addNewCustomer(id, name, city, age):
        Customers.addcustomer(id, name, city, age)

    def getBookByName(bookName):
        return Book.Books.getBook(bookName)

    def removeBookFromLibrary(name, author):
        Book.Books.removeBook(name, author)

    def disaplyAllBooks():
        print(Book.Books.getBookList())

    def loanBookToCustomer(bookName, customerName):
        bookID = Book.Books.getIDbyName(bookName)
        custID = Customer.Customers.getCustomerIDbyName(customerName)
        Loan.Loans.addLoan(bookID,custID)
        
    def returnBook(bookName):
        bookID = Book.Books.getIDbyName(bookName)
        Loan.Loans.returnBook(bookID)
a = -1
while a != 0:
    print('what would you like to do?\n 1. check for a book\n\
    2. loan a book\n\
    3. return a book\n\
    4. show all books\n\
    5. add a book\n\
    6. remove a book\n\
    7. add new customer\n\
    0. Exit')
    a = int(input('enter choice: '))

    if a == 0:
        print ('goodbye')
        continue
        
    elif a == 1:
        name = input('enter book name: ')
        print(Library.getBookByName(name))
            
    elif a == 2:
        bookName = input('enter book name: ')
        customerName = input('enter customer name: ')
        print(Library.loanBookToCustomer(bookName, customerName))
            
    elif a == 3:
        bookName = input('enter book name: ')
        print(Library.returnBook(bookName))
            
    elif a == 4:
        Library.disaplyAllBooks()
        

    
    elif a == 5:
        name = input('book name: ')
        author = input('author name: ')
        yearPublished = int(input('year of publish: '))
        type = int(input('which type (1,2,3)?'))
        Library.addNewBook(name, author, yearPublished, type)
    
    elif a == 6:
        bookName = input('enter book name: ')
        author = input('by whom?: ')
        Library.removeBookFromLibrary(bookName, author)
        print('book removed')

    elif a == 7:
        id = int(input('enter id: '))
        name = input('enter customer name: ')
        city = input('enter city: ')
        age = int(input('customer age: '))
        Library.addNewCustomer(id, name, city, age)



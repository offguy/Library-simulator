import myconection as connect
import datetime

class Loans:
    loanList = []
    def addLoan(bookID, custID):
        t = datetime.date.today()
        cursor = connect.connect()
        cursor.execute(f'insert into loans(custid, bookid, loandate)values({custID},{bookID},{t})')
        cursor.connection.commit()

    def allLoans():
        cursor = connect.connect()
        cursor.execute(f"select * from loans")
        c = cursor.fetchall()
        return c

    def returnBook(bookid):
        cursor = connect.connect()
        cursor.execute(f"delete from loans where bookid = '{bookid}'")
        cursor.connection.commit()

    def checkLateLoans():
        cursor = connect.connect()
        c = cursor.execute(f'select * from loans where returndate')
        
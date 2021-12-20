import myconection as connect
class Books:
    _globalID = 0
                    
    def addBook(name, author, yearpublished, type):
        Books._globalID += 1
        cursor = connect.connect()
        cursor.execute(f'insert into books (id, name, author, yearpublished, type)values({Books._globalID},"{name}","{author}",{yearpublished},{type})')
        cursor.connection.commit()
    
    def removeBook(name, author):
        cursor = connect.connect()
        cursor.execute(f"delete from books where name = {name} and author = {author}")
        cursor.connection.commit()
    
    def getBook(name):
        cursor = connect.connect()
        cursor.execute(f"select * from books where name = {name}")
        c = cursor.fetchall()
        return c
        
    def getBookList():
        cursor = connect.connect()
        cursor.execute('select * from books')
        result = cursor.fetchall()
        return result

    def getIDbyName(name):
        return Books.getBook()[0] # Books.getBook() returns list, position 0 in list is id

# Books.addBook('hello', 'world', 2021, 3)

import myconection as connect
class Customers:
    def addcustomer(id, name, city, age):
        cursor = connect.connect()
        cursor.execute(f'insert into customers(id,name,city,age)values({id},"{name}","{city}",{age})')
        cursor.connection.commit()
        

    def getCustomer(id):
        cursor = connect.connect()
        cursor.execute(f'select * from customers where id = {id}')
        c = cursor.fetchall()
        return c

    def deleteCustomer(id):
        cursor = connect.connect()
        cursor.execute(f'delete from customers where id = {id}')
        cursor.connection.commit()
    
    def getCustomerIDbyName(name):
        return Customers.getCustomer()[0]

'''
HW09: Basic SQL statements
'''

import sqlite3 as sqlite

conn = sqlite.connect('Northwind_small.sqlite')
cur = conn.cursor()

#----- Q1. Show all rows from the Region table
statement1 = "SELECT * "
statement1 += "FROM Region;"

rows_in_region_table = cur.execute(statement1)
for row in rows_in_region_table:
    (Id, RegionDescription) = row
    print(Id, RegionDescription)

#----- Q2. How many customers are there?
statement2 = "SELECT COUNT(Id) "
statement2 += "FROM Customer;"

num_of_customers = cur.execute(statement2)
print(num_of_customers.fetchone()[0])

#----- Q3. How many orders have been made?
statement3 = "SELECT COUNT(Id) "
statement3 += "FROM [Order];"

num_of_orders = cur.execute(statement3)
print(num_of_orders.fetchone()[0])

#----- Q4. Show the first five rows from the Product table
statement4 = "SELECT * "
statement4 += "FROM Product "
statement4 += "LIMIT 5;"

top_five_rows = cur.execute(statement4)
for row in top_five_rows:
    (Id, ProductName, SupplierId, CategoryId, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued) = row
    print(Id, ProductName, SupplierId, CategoryId, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)

#----- Q5. Show all available categories
statement5 = "SELECT CategoryName "
statement5 += "FROM Category;"

available_categories = cur.execute(statement5)
for row in available_categories:
    CategoryName = row[0]
    print(CategoryName)

#----- Q6. Show the five cheapest products
statement6 = "SELECT ProductName, UnitPrice "
statement6 += "FROM Product "
statement6 += "ORDER BY UnitPrice ASC "
statement6 += "LIMIT 5;"

cheapes_products = cur.execute(statement6)
for row in cheapes_products:
    (ProductName, UnitPrice) = row
    print(ProductName, UnitPrice)

#----- Q7. Show all products that have more than 100 units in stock
statement7 = "SELECT ProductName, UnitsInStock "
statement7 += "FROM Product "
statement7 += "WHERE UnitsInStock > 100;"

products_more_than_100_units_in_stock = cur.execute(statement7)
for row in products_more_than_100_units_in_stock:
    (ProductName, UnitsInStock) = row
    print(ProductName, UnitsInStock)


#----- Q8. Show all columns in the Order table
statement8 = "SELECT * "
statement8 += "FROM [Order]"
statement8 += "LIMIT 1;"

columns_in_order_table = cur.execute(statement8)
for column in columns_in_order_table.description:
    print(column[0])

#----- Q9. Identify each employee's first name and the number of order each employee has made. Sort them by the total number of orders in decreasing order
statement9 = "SELECT COUNT([Order].Id) AS OrderCount, LastName, FirstName "
statement9 += "FROM [Order] INNER JOIN Employee "
statement9 += "ON [Order].EmployeeId = Employee.Id "
statement9 += "GROUP BY EmployeeId "
statement9 += "ORDER BY OrderCount DESC;"

num_of_orders_employee = cur.execute(statement9)
for row in num_of_orders_employee:
    (NumOfOrder, LastName, FirstName) = row
    print(NumOfOrder, LastName, FirstName)

#----- Q10. Identify the products and the corresponding supply companies in Ann Arbor
statement10 = "SELECT p.ProductName, s.CompanyName "
statement10 += "FROM Product AS p INNER JOIN Supplier AS s "
statement10 += "ON p.SupplierId = s.Id "
statement10 += "WHERE s.City = 'Ann Arbor'"

product_company_in_ann_arbor = cur.execute(statement10)
for row in product_company_in_ann_arbor:
    (ProductName, CompanyName) = row
    print(ProductName, CompanyName)

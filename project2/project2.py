import mysql.connector
from mysql.connector import Error
#Function 1 
def print_publishers(cursor):
    cursor.execute("SELECT * FROM publishers")
    rows = cursor.fetchall()
    print("Publisher:")
    for row in rows:
        print(row)
#Function 2 
def create_customer_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS customer (custID INT(3) NOT NULL, custName VARCHAR(30) NULL, zip VARCHAR(10) NULL, city VARCHAR(30) NULL, state VARCHAR(30) NULL, PRIMARY KEY(custID))")
    print("Customer table created")
	#Function 3 
def insert_customers(cursor):
	cursor.execute("INSERT IGNORE INTO customer (custID, custName, zip, city, state) VALUES (1, 'ABRAHAM SILBERSCHATZ', '12345', 'New York', 'NY'), (2, 'HENRY KORTH', '67890', 'Pittsburgh', 'PA'), (3, 'CALVIN HARRIS', '54321', 'Los Angeles', 'CA'), (4, 'MARTIN GARRIX', '09876', 'Amsterdam', 'NL'), (5, 'JAMES GOODWILL', '13579', 'Boston', 'MA')")
	connection.commit()
	print(cursor.rowcount, "customers inserted")

	#function 4 NEEDS work as books are never specified
def find_top_author(cursor):
	cursor.execute("SELECT a.aName, COUNT(*) AS book_count FROM authors a JOIN titleauthors ta ON a.auID = ta.auID GROUP BY a.auID ORDER BY book_count DESC LIMIT 1")
	rows = cursor.fetchall()
	print("Bookworm author:")
	for row in rows:
		print(row[0], "has written", row[1], "books")

		#function 5 List all publishers and the total price of their published titles
def list_publisher_total_price(cursor):
	cursor.execute("SELECT p.pname, SUM(t.price) as total_price FROM publishers p JOIN titles t ON p.pubID = t.pubID GROUP BY p.pname;")
	rows = cursor.fetchall()
	print("Publishers and total price:")
	for row in rows:
		print(row[0], "-", row[1])

		#function 6 
def find_authors_with_java(cursor):
	cursor.execute("""
            SELECT DISTINCT a.aName
            FROM authors a
            JOIN titleauthors ta ON a.auID = ta.auID
            JOIN titles t ON ta.titleID = t.titleID
            JOIN subjects s ON t.subID = s.subID
            WHERE s.sName LIKE '%Java%';
        """)
	rows = cursor.fetchall()
	print("Names of all authors who have wrote a book that has the word Java in its name:")
	for row in rows:
		print(row[0])

		#function 7
def find_authors_with_paperback(cursor):
	cursor.execute("""
            SELECT DISTINCT a.aName
            FROM authors a
            JOIN titleauthors ta ON a.auID = ta.auID
            JOIN titles t ON ta.titleID = t.titleID
            WHERE t.cover = 'Paper back' AND t.price BETWEEN 475 AND 500;
        """)
	rows = cursor.fetchall()
	print("Names of all authors who written a book with price between 475 and 500 and cover type of paperback:")
	for row in rows:
		print(row[0])

		#function 8 is bizarre and I need to ask questions
def find_authors_without_oracle(cursor):
	cursor.execute("""
            SELECT DISTINCT a.aName
            FROM authors a
            JOIN titleauthors ta ON a.auID = ta.auID
            JOIN titles t ON ta.titleID = t.titleID
            JOIN subjects s ON t.subID = s.subID
            WHERE s.sName = 'VISUAL BASIC.NET' AND a.auID NOT IN (
                SELECT DISTINCT ta.auID
                FROM titleauthors ta
                JOIN titles t ON ta.titleID = t.titleID
                JOIN subjects s ON t.subID = s.subID
                WHERE s.sName = 'ORACLE DATABASE'
            );
        """)
	rows = cursor.fetchall()
	print("Names of authors who have wrote books on Visual basic.net but not oracle database: ")
	for row in rows:
		print(row[0])

		#function 9 query
def get_gmail_users(cursor):
	cursor.execute("SELECT aName FROM authors WHERE email LIKE '%@gmail.com'")
	rows = cursor.fetchall()
	print("Names of all whose email address contains gmail: ")
	for row in rows:
		print(row[0])

		#function 10- REVIEW CAREFULLY, THERE MIGHT PRICE DECREASES IN THE ACTUAL SQL DATABASE
def price_controls():
	cursor.execute("UPDATE titles SET price = CASE WHEN pubDate < '2003-01-01' THEN price * 0.75 ELSE price * 0.9 END")
	connection.commit()
	print(cursor.rowcount, "SQL records updated, please do the math to double check")
	



try:
	connection = mysql.connector.connect(host= 'localhost', database = 'project2', user ='root', password = 'Luna@2715')
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Connected to MySQL Server version ", db_Info)
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		print("You're connected to database: ", record)

		#Function 1 please work
	#def print_publishers(connection):
		#cursor.execute("SELECT * FROM publishers")
		#rows = cursor.fetchall()
		#print("Publisher: ")
		#for row in rows:
			#print(row)
		print_publishers(cursor)
		print("function 1 output success")
			
			

			#Function 2 please work
		#def create_customer_table():
			#cursor.execute("CREATE TABLE IF NOT EXISTS customer (custID INT(3) NOT NULL, custName VARCHAR(30) NULL, zip VARCHAR(10) NULL, city VARCHAR(30) NULL, state VARCHAR(30) NULL, PRIMARY KEY(custID))")
			#print("Customer table created")
		create_customer_table(cursor)
		print("function 2 output success")

		#Function 3 line break
		insert_customers(cursor)
		print("function 3 output success")

		#function 4 line break
		find_top_author(cursor)
		print("function 4 output success")

		#function 5 line break
		list_publisher_total_price(cursor)
		print("function 5 output success")

		#function 6 line break
		find_authors_with_java(cursor)
		print("function 6 output success")

		#function 7 line break
		find_authors_with_paperback(cursor)
		print("function 7 output success")

		#function 8 line break
		find_authors_without_oracle(cursor)
		print("function 8 output success")

		#function 9 line break
		get_gmail_users(cursor)
		print("function 9 output success")

		#function 10 line break
		price_controls()
		print("function 10 output success")
			

except Error as e:
	print("Error while connecting to MySQL", e)
finally:
	if(connection.is_connected()):
		cursor.close()
		connection.close()
		print("MySQL connection is closed")


		#end of code template
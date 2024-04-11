import mysql.connector

# Connection
def mySQLfunc_connection():
    print('Connect to MySQL server')
    db = mysql.connector.connect(
        host='localhost',  # ip when it will be on cloud
        user='root',
        passwd='NV27vnmc',
        database='alex_db'
    )
    print(db)  # checking our connection to DB
    print("Connected to the MySQL database")
    mycursor = db.cursor()  # Create a cursor object to interact with the database
    mycursor.close()  # Close the cursor and connection when done
    db.commit()
    db.close()

# SELECT
def mySQLfunc_select():
    print('Connect to MySQL server')
    db = mysql.connector.connect(
        host='localhost',  # ip when it will be on cloud
        user='root',
        passwd='NV27vnmc',
        database='alex_db'
    )
    print(db)  # checking our connection to DB
    print("Connected to the MySQL database")
    mycursor = db.cursor()  # Create a cursor object to interact with the database
    mycursor.execute("SELECT * FROM users")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)
    mycursor.close()  # Close the cursor and connection when done
    db.commit()
    db.close()

# INSERT
def mySQLfunc_insert():
    print('Connect to MySQL server')
    db = mysql.connector.connect(
        host='localhost',  # ip when it will be on cloud
        user='root',
        passwd='NV27vnmc',
        database='alex_db'
    )
    print(db)  # checking our connection to DB
    print("Connected to the MySQL database")
    mycursor = db.cursor()  # Create a cursor object to interact with the database
    sql = "INSERT INTO users (full_name, email) VALUES (%s, %s)"
    val = ("Oleg Kan", "Oleg@gmail.com")
    mycursor.execute(sql, val)
    mycursor.close()  # Close the cursor and connection when done
    db.commit()
    db.close()

# DELETE

# UPDATE

# WHERE

# mySQLfunc_connection()
# mySQLfunc_select()
# mySQLfunc_insert()

# CREATE new table


# SELECT - extracts data from a database
# UPDATE - updates data in a database
# DELETE - deletes data from a database
# INSERT INTO - inserts new data into a database
# CREATE DATABASE - creates a new database
# ALTER DATABASE - modifies a database
# CREATE TABLE - creates a new table
# ALTER TABLE - modifies a table
# DROP TABLE - deletes a table
# CREATE INDEX - creates an index (search key)
# DROP INDEX - deletes an index









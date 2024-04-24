import mysql.connector

# Connection
def mySQL_func_connection():
    print('Connect to MySQL server')
    db = mysql.connector.connect(
        host='localhost',  # ip - on cloud
        user='root',  # username
        passwd='NV27vnmc',  # password
        database='alex_db'  # DB name
    )

    # checking connection to DB
    print(db)
    print("Connected to the MySQL database")

    # Create a cursor object to interact with the database
    mycursor = db.cursor()

    # Close the cursor and connection when done
    mycursor.close()
    db.commit()
    db.close()
    print('\nconnection closed')

# Playing with DB
def interactingwithsql():
    print('Connect to MySQL server')
    db = mysql.connector.connect(
        host='localhost',  # ip - on cloud
        user='root',  # username
        passwd='NV27vnmc',  # password
        database='alex_db'  # DB name
    )

    # checking connection to DB
    print(db)
    print("Connected to the MySQL database")

    # Create a cursor object to interact with the database
    mycursor = db.cursor()

    body_select = '''
    SELECT * FROM users
    '''
    body_union = '''
    SELECT phone_number,full_name FROM users 
    UNION 
    SELECT phone, name FROM users2
    '''
    body_top = '''
    SELECT full_name FROM users limit 2
    '''
    mycursor.execute(body_select)
    data = mycursor.fetchall()
    # print(data)
    # printing for better format
    for line in data:
        print(line)

    # Close the cursor and connection when done
    mycursor.close()
    db.commit()
    db.close()
    print('\nconnection closed')

# SELECT FROM | WHERE | ORDER BY | ASC | DESC | AND | OR | NOT
def mySQL_func_select():
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
    print('\nselect all')
    mycursor.execute("SELECT * FROM users")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    print('\nselect specific')
    mycursor.execute("SELECT full_name, email FROM users")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # SELECT DISTINCT statement is used to return only distinct (different) values.
    print('\nselect DISTINCT')
    mycursor.execute("SELECT DISTINCT full_name, email FROM users")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # Select Where - condition
    print('\nSelect Where - condition')
    mycursor.execute("SELECT full_name, email FROM users WHERE full_name = 'alex dezho'")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # ORDER BY / ASC/ DESC - keyword is used to sort the result-set in ascending or descending order
    print('\nORDER BY')
    mycursor.execute("SELECT * FROM users ORDER BY email ")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # AND operator - condition is used to filter records based on more than one condition
    print('\nAND operator - condition')
    mycursor.execute("SELECT full_name, email FROM users WHERE full_name = 'alex dezho' AND email = 'alex27dz@gmail.com'")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # OR operator is used to filter records based on more than one condition
    print('\nOR operator')
    mycursor.execute("SELECT full_name, email FROM users WHERE full_name = 'alex dezho' or full_name = 'Oleg Kan'")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # NOT operator is used in combination with other operators to give the opposite result
    print('\nNOT operator')
    mycursor.execute("SELECT full_name, email FROM users WHERE NOT full_name = 'alex dezho'")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # Close the cursor and connection when done
    mycursor.close()
    db.commit()
    db.close()
    print('\nconnection closed')

# INSERT INTO
def mySQL_func_insert():
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

    # INSERT INTO more than one statement
    print('\nINSERT INTO user2')
    sql = "INSERT INTO users2 (phone, name) VALUES (%s, %s)"
    val = (888777645,'BOP')
    val2 = (888777662,'Aaron')
    values = [val, val2]
    mycursor.executemany(sql, values)

    # Print back results
    print('\nusers2')
    mycursor.execute("SELECT * FROM users2")
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # Close the cursor and connection when done
    mycursor.close()
    db.commit()
    db.close()
    print('\nconnection closed')

# WHERE - any condition | sub query and aggregation (group by and having count, sum, =, )
def mySQL_func_select_aggregation():
    print('Connect to MySQL server')
    db = mysql.connector.connect(
        host='localhost',  # ip when it will be on cloud
        user='root',
        passwd='NV27vnmc',
        database='alex_db'
    )
    print(db)  # checking our connection to DB
    print("Connected to the MySQL database\n")
    mycursor = db.cursor()  # Create a cursor object to interact with the database

    sql_query = """
    SELECT phone, name
    FROM users2
    WHERE name IN (
        SELECT name
        FROM users2
        GROUP BY name
        HAVING COUNT(*) > 1
    )
    ORDER BY name;
    """
    mycursor.execute(sql_query)
    result = mycursor.fetchall()
    for row in result:
        print(row)

    # Close the cursor and connection when done
    mycursor.close()
    db.commit()
    db.close()
    print('\nconnection closed')

# TOP | Limit
def mySQL_func_select_top_limit ():
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
    print('\nselect all')
    mycursor.execute("SELECT * FROM users2")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    print('\nselect top 2')
    mycursor.execute("SELECT * FROM users2 limit 2")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # Close the cursor and connection when done
    mycursor.close()
    db.commit()
    db.close()
    print('\nconnection closed')

# UNION | JOIN - combining selection from two different tables
def mySQL_func_select_union():
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
    print('\nUNION')
    mycursor.execute("SELECT full_name, phone_number FROM users UNION SELECT name, phone FROM users2")  # Execute a query to fetch data from a table
    rows = mycursor.fetchall()  # Fetch all rows from the result set
    for row in rows:  # Display the fetched data
        print(row)

    # Close the cursor and connection when done
    mycursor.close()
    db.commit()
    db.close()
    print('\nconnection closed')


# MIN MAX
# Having
# DELETE
# UPDATE
# CREATE DATABASE - creates a new database
# CREATE TABLE - creates a new table
# DROP TABLE - deletes a table




def mysql_connection():

    import mysql.connector

    # Connect to the MySQL server
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='NV27vnmc',
        database='alex_db'
    )

    print(type(db))

    # Create a cursor object
    cursor = db.cursor()

    # Define the SQL query
    query = 'SELECT * FROM users'

    # Execute the query
    cursor.execute(query)

    # Fetch all the results - as a list
    results = cursor.fetchall()
    print(results)  # as a list


    # Print the results
    # for row in results:
    #    print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

    '''
    db_name = 'users'
    new_table_with_items = """CREATE TABLE {} (
                                full_name VARCHAR(255),
                                email VARCHAR(255),
                                phone_number VARCHAR(255),
                                id VARCHAR(255),
                                notes VARCHAR(255)
                            )""".format(db_name)
    
    '''


def microsoft_sql():
    import pyodbc  # Open Database Connectivity

    # Define the connection string parameters
    server_name = "ltc-ist-08-cc-0019-sat-sql-ewc3a.database.windows.net,1433"  # Replace with your SQL Server's hostname
    database_name = "CMS_QA"  # Replace with your database name
    username = "CMSIstUser"  # Replace with your SQL Server username
    password = "j22WaVeDPUM4S3K9"  # Replace with your SQL Server password

    # Create a connection string
    connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server_name};Database={database_name};Uid={username};Pwd={password}"

    # Establish a connection to the database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()  # Create a cursor to interact with the database
    cursor.execute("SELECT * FROM TrainingProviderApplicantBusinesses")  # Execute SQL queries
    rows = cursor.fetchall()
    for row in rows:  # Iterate through the results
        print(row)
    cursor.close()  # Close the cursor and connection when done
    connection.close()












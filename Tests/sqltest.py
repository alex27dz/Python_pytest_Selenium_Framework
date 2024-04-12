import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',  # ip when it will be on cloud
    user='root',
    passwd='NV27vnmc',
    database='alex_db'
)
cursor = conn.cursor()

# SQL Insert Statement
sql_insert_query = "INSERT INTO users2 (phone, name) VALUES (%s, %s)"

# Data to insert
records_to_insert = [
    (555444222,'Alice'),
    (888777663, 'Bob'),
    (999888444, 'Dima')
]

try:
    # Executing the SQL statement in batches
    cursor.executemany(sql_insert_query, records_to_insert)

    # Commit your changes in the database
    conn.commit()

    print(cursor.rowcount, "records inserted successfully into table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    # closing database connection.
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")

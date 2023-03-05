import sqlite3

# Establish a connection and cursor
connection=sqlite3.connect('db/sample.sqlite')
cursor=connection.cursor()

# Query all data based on a condition
# cursor.execute("SELECT * FROM events WHERE band='Lions'") # this will modify the cursor obj
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'") # this will modify the cursor obj
rows=cursor.fetchall() # list of tuples
print(rows)

# Query certain columns based on a condition
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows=cursor.fetchall()
print(rows)

# Inserting rows
# new_rows=[('Cats', 'Cat City', '2088.10.17'),
#            ('Hen', 'Hen City', '2088.10.17')]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows) # to add multiple rows to the db
# connection.commit() # write changes

# Query all data
cursor.execute("SELECT * FROM events") # this will modify the cursor obj
rows=cursor.fetchall() # list of tuples
print(rows)
import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# Create a Table

# c.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
#  )""")

# DATA TYPES
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# many_customer = [
#     ('Billal', 'Billu', 'billu@gmail.com'), 
#     ('Rabbi', 'Mama', 'mama@gmail.com'), 
#     ('Shazib', 'Modon', 'modon@gmail.com')]

# c.execute("INSERT INTO customers VALUES('Md', 'Awlad', 'mdawlad@gmail.com')")

# c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customer)

c.execute("SELECT * FROM customers")

print(c.fetchall())



print("Command Execute successfully......")

#Commit our command
conn.commit()

#close our connecion

conn.close()
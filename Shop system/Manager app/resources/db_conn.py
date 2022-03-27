# Import your module for your database
from sqlite3 import connect  # This was just for testing! Delete it!

# Connect to your database here:
database = connect('../shop_database.db')
mycursor = database.cursor()

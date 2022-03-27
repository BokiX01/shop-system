# Import your module for your database
from sqlite3 import connect  # This was just for testing! Delete it!

# Connect to your database here:
database = connect('shop_database.db')  # This was just for testing!
mycursor = database.cursor()

mycursor.execute(
    '''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        price DECIMAL(8,2) NOT NULL,
        discount INTEGER
    );
    '''
)
mycursor.execute(
    '''
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        administrator BOOLEAN DEFAULT FALSE
    );
    '''
)

# Run this code to create tables for the application
database.commit()

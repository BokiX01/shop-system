from .db_conn import database, mycursor


class Items:
    # Adding item to database
    @staticmethod
    def add_item(name, price, discount):
        name = name.lower().replace(' ', '_')
        mycursor.execute(f"INSERT INTO items (name, price, discount) VALUES ('{name}', {price}, {discount});")
        database.commit()

    # Removing item from database
    @staticmethod
    def remove_item(item_id_or_name):
        try:
            item_id_or_name = int(item_id_or_name)
            mycursor.execute(f"DELETE FROM items WHERE item_id = {item_id_or_name};")
        except ValueError:
            item_id_or_name = item_id_or_name.lower().replace(' ', '_')
            mycursor.execute(f"DELETE FROM items WHERE name = '{item_id_or_name}';")
        database.commit()

    # Changing item name, price or applying discount to an item
    @staticmethod
    def change_name_price_discount(item_id_or_name, value_type, value):
        try:
            item_id_or_name = int(item_id_or_name)
            mycursor.execute(f"UPDATE items SET {value_type} = {value} WHERE item_id = {item_id_or_name};")
        except ValueError:
            item_id_or_name = item_id_or_name.lower().replace(' ', '_')
            mycursor.execute(f"UPDATE items SET {value_type} = {value} WHERE name = '{item_id_or_name}';")
        database.commit()

    # Listing all items from database
    @staticmethod
    def list_items():
        mycursor.execute(f"SELECT * FROM items;")
        return mycursor.fetchall()

    # Getting info about specific item
    @staticmethod
    def get_info(item_id_or_name):
        try:
            item_id_or_name = int(item_id_or_name)
            mycursor.execute(f"SELECT name, price, discount FROM items WHERE item_id = {item_id_or_name};")
        except ValueError:
            item_id_or_name = item_id_or_name.lower().replace(' ', '_')
            mycursor.execute(f"SELECT name, price, discount FROM items WHERE name = '{item_id_or_name}';")
        return mycursor.fetchall()

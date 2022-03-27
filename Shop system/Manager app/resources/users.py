from .db_conn import database, mycursor


class Users:
    # Adding user to database
    @staticmethod
    def add_user(username, password, admin=False):
        mycursor.execute(
            f"INSERT INTO users (username, password, administrator) VALUES ('{username}', '{password}', {admin});")
        database.commit()

    # Removing user from database
    @staticmethod
    def remove_user(username):
        mycursor.execute(f"DELETE FROM users WHERE username = '{username}';")
        database.commit()

    # Changing user username, password or administration level
    @staticmethod
    def change_username_password_admin(user, value_type, value):
        mycursor.execute(f"UPDATE users SET {value_type} = '{value}' WHERE username = '{user}';")
        database.commit()

    # List all users
    @staticmethod
    def list_users():
        mycursor.execute(f"SELECT username, administrator FROM users;")
        return mycursor.fetchall()

    # Checking if a specific user is in database
    @staticmethod
    def check_login(username, password):
        mycursor.execute(f"SELECT username FROM users WHERE username = '{username}' AND password = '{password}' AND administrator = TRUE;")
        return mycursor.fetchall()

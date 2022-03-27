from tkinter import *
from resources.items import Items
from resources.users import Users

# Creating root window
root = Tk()
root.title('Warehouse manager')
root.geometry('800x600')

# Configuring root window so window frame can strech
Grid.rowconfigure(root, index=0, weight=1)
Grid.columnconfigure(root, index=0, weight=1)

# Creating window frame for all widgets
frame = Frame(root, padx=5, pady=5)
frame.grid(sticky='NSEW')
frame.config(bg='#383838')

# Configuring window frame so widgets can strech
for i in range(12):
    Grid.rowconfigure(frame, index=i, weight=1)
for i in range(2):
    Grid.columnconfigure(frame, index=i, weight=1)

# Creating configurions for widgets so they can be edited easily
font = ('Arial', 20)
borderwidth = 20
label_config = {'bg': '#383838', 'fg': 'White', 'font': font}
button_config = {'bg': '#c1dbda', 'fg': '#383838', 'font': font, 'borderwidth': borderwidth}
entry_config = {'bg': '#fdffcf', 'font': font, 'borderwidth': borderwidth, 'justify': 'center'}
text_config = {'bg': '#fdffcf', 'borderwidth': borderwidth}
option_config = {'bg': '#383838', 'font': font}


# Menu for items managment
def items_manager():
    for widget in frame.winfo_children():
        widget.grid_forget()

    # Adding new item to database
    def add_item():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Item name: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        item_name = Entry(frame, **entry_config)
        item_name.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='Item price: ', **label_config).grid(row=4, column=0, rowspan=4, sticky='NSEW')
        item_price = Entry(frame, **entry_config)
        item_price.grid(row=4, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Add item', **button_config, command=lambda: (Items.add_item(item_name.get(), int(item_price.get()), 0), add_item())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=items_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Removing item from database
    def remove_item():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Item ID or name: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        item_id_name = Entry(frame, **entry_config)
        item_id_name.grid(row=0, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Remove item', **button_config, command=lambda: (Items.remove_item(item_id_name.get()), remove_item())).grid(row=10, column=0, rowspan=2, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=items_manager).grid(row=10, column=1, rowspan=2, sticky='NSEW')

    # Changing items name
    def change_item_name():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Item ID or name: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        item_id_name = Entry(frame, **entry_config)
        item_id_name.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='New item name: ', **label_config).grid(row=4, column=0, rowspan=4, sticky='NSEW')
        new_name = Entry(frame, **entry_config)
        new_name.grid(row=4, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Change item name', **button_config, command=lambda: (Items.change_name_price_discount(item_id_name.get(), 'name', f"'{new_name.get()}'"), change_item_name())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=items_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Changing items price
    def change_item_price():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Item ID or name: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        item_id_name = Entry(frame, **entry_config)
        item_id_name.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='New item price: ', **label_config).grid(row=4, column=0, rowspan=4, sticky='NSEW')
        new_price = Entry(frame, **entry_config)
        new_price.grid(row=4, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Change item price', **button_config, command=lambda: (Items.change_name_price_discount(item_id_name.get(), 'price', new_price.get()), change_item_price())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=items_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Applying discount to item
    def apply_discount():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Item ID or name: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        item_id_name = Entry(frame, **entry_config)
        item_id_name.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='New item discount: ', **label_config).grid(row=4, column=0, rowspan=4, sticky='NSEW')
        new_discount = Entry(frame, **entry_config)
        new_discount.grid(row=4, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Change item discount', **button_config, command=lambda: (Items.change_name_price_discount(item_id_name.get(), 'discount', new_discount.get()), apply_discount())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=items_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Listing all items from database
    def list_items():
        for widget in frame.winfo_children():
            widget.grid_forget()

        text = ''
        for item in Items.list_items():
            item_id = ''
            for i in range(len(str(item[0])), 6):
                item_id += '0'
            item_id += str(item[0])
            text += f'\tItem ID: {item_id};\tItem name: {item[1].capitalize()};\tPrice: {item[2]} kn'
            if item[3] > 0:
                text += f';\tDiscount: {item[3]}%'
            text += '\n'
        credits_box = Text(frame, **text_config)
        credits_box.grid(row=0, column=0, rowspan=9, columnspan=2, sticky='NSEW')
        credits_box.insert('1.0', text)
        credits_box.config(state=DISABLED)
        Button(frame, text='Back', **button_config, command=items_manager).grid(row=9, column=0, rowspan=3, columnspan=2, sticky='NSEW')

    Button(frame, text='Add item', **button_config, command=add_item).grid(row=0, column=0, rowspan=3, sticky='NSEW')
    Button(frame, text='Remove item', **button_config, command=remove_item).grid(row=0, column=1, rowspan=3, sticky='NSEW')
    Button(frame, text='Change item name', **button_config, command=change_item_name).grid(row=3, column=0, rowspan=3, sticky='NSEW')
    Button(frame, text='Change item price', **button_config, command=change_item_price).grid(row=3, column=1, rowspan=3, sticky='NSEW')
    Button(frame, text='Apply discount', **button_config, command=apply_discount).grid(row=6, column=0, rowspan=3, sticky='NSEW')
    Button(frame, text='List all items', **button_config, command=list_items).grid(row=6, column=1, rowspan=3, sticky='NSEW')
    Button(frame, text='Back', **button_config, command=main).grid(row=9, column=0, rowspan=3, columnspan=2, sticky='NSEW')


# Menu for users managment
def users_manager():
    for widget in frame.winfo_children():
        widget.grid_forget()

    # Adding new user to database
    def add_user():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Username: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='User password: ', **label_config).grid(row=4, column=0, rowspan=4, sticky='NSEW')
        password = Entry(frame, **entry_config, show='*')
        password.grid(row=4, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Add user', **button_config, command=lambda: (Users.add_user(username.get(), password.get()), add_user())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=users_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Removing user from database
    def remove_user():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='User username: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=0, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Remove user', **button_config, command=lambda: (Users.remove_user(username.get()), remove_user())).grid(row=10, column=0, rowspan=2, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=users_manager).grid(row=10, column=1, rowspan=2, sticky='NSEW')

    # Changing users username
    def change_username():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Username: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='New username: ', **label_config).grid(row=4, column=0, rowspan=4, sticky='NSEW')
        new_username = Entry(frame, **entry_config)
        new_username.grid(row=4, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Change username', **button_config, command=lambda: (Users.change_username_password_admin(username.get(), 'username', new_username.get()), change_username())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=users_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Changing users password
    def change_user_password():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Username: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='New password: ', **label_config).grid(row=4, column=0, rowspan=4, sticky='NSEW')
        new_password = Entry(frame, **entry_config, show='*')
        new_password.grid(row=4, column=1, rowspan=4, sticky='NSEW')

        Button(frame, text='Change user password', **button_config, command=lambda: (Users.change_username_password_admin(username.get(), 'password', new_password.get()), change_user_password())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=users_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Changing users administration level
    def change_user_admin_level():
        for widget in frame.winfo_children():
            widget.grid_forget()

        Label(frame, text='Username: ', **label_config).grid(row=0, column=0, rowspan=4, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=0, column=1, rowspan=4, sticky='NSEW')
        Label(frame, text='Administration:\t  YES ', **label_config).grid(row=4, column=0, rowspan=2, sticky='NSEW')
        Label(frame, text='Administration:\t   No ', **label_config).grid(row=6, column=0, rowspan=2, sticky='NSEW')
        new_admin_level = BooleanVar()
        new_admin_level.set(False)
        Radiobutton(frame, **option_config, variable=new_admin_level, value=True).grid(row=4, column=1, rowspan=2, sticky='NSEW')
        Radiobutton(frame, **option_config, variable=new_admin_level, value=False).grid(row=6, column=1, rowspan=2, sticky='NSEW')

        Button(frame, text='Change user administration level', **button_config, command=lambda: (Users.change_username_password_admin(username.get(), 'administrator', new_admin_level.get()), change_user_admin_level())).grid(row=8, column=0, rowspan=4, sticky='NSEW')
        Button(frame, text='Back', **button_config, command=users_manager).grid(row=8, column=1, rowspan=4, sticky='NSEW')

    # Listing all users from database
    def list_users():
        for widget in frame.winfo_children():
            widget.grid_forget()

        text = ''
        for user in Users.list_users():
            text += f'\tUsername: {user[0]};\tAdministrator: {bool(user[1])}\n'
        credits_box = Text(frame, **text_config)
        credits_box.grid(row=0, column=0, rowspan=9, columnspan=2, sticky='NSEW')
        credits_box.insert('1.0', text)
        credits_box.config(state=DISABLED)
        Button(frame, text='Back', **button_config, command=users_manager).grid(row=9, column=0, rowspan=3, columnspan=2, sticky='NSEW')

    Button(frame, text='Add user', **button_config, command=add_user).grid(row=0, column=0, rowspan=3, sticky='NSEW')
    Button(frame, text='Remove user', **button_config, command=remove_user).grid(row=0, column=1, rowspan=3, sticky='NSEW')
    Button(frame, text='Change username', **button_config, command=change_username).grid(row=3, column=0, rowspan=3, sticky='NSEW')
    Button(frame, text='Change user password', **button_config, command=change_user_password).grid(row=3, column=1, rowspan=3, sticky='NSEW')
    Button(frame, text='Change user admin level', **button_config, command=change_user_admin_level).grid(row=6, column=0, rowspan=3, sticky='NSEW')
    Button(frame, text='List all users', **button_config, command=list_users).grid(row=6, column=1, rowspan=3, sticky='NSEW')
    Button(frame, text='Back', **button_config, command=main).grid(row=9, column=0, rowspan=3, columnspan=2, sticky='NSEW')


# Main menu for the application
def main():
    for widget in frame.winfo_children():
        widget.grid_forget()

    Button(frame, text='Items manager', **button_config, command=items_manager).grid(row=0, column=0, rowspan=4, columnspan=2, sticky='NSEW')
    Button(frame, text='Users manager', **button_config, command=users_manager).grid(row=4, column=0, rowspan=4, columnspan=2, sticky='NSEW')
    Button(frame, text='Exit', **button_config, command=quit).grid(row=8, column=0, rowspan=4, columnspan=2, sticky='NSEW')


# Login into the application
def login():
    for widget in frame.winfo_children():
        widget.grid_forget()

    # Checking if there is any users in database
    if Users.list_users() == list():
        # Register for first user whose administration level will be set to True
        Label(frame, text='Warehouse manager register', **label_config).grid(row=0, column=0, rowspan=3, columnspan=2, sticky='NSEW')
        Label(frame, text='Username: ', **label_config).grid(row=3, column=0, rowspan=3, sticky='NSEW')
        Label(frame, text='Password: ', **label_config).grid(row=6, column=0, rowspan=3, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=3, column=1, rowspan=3, sticky='NSEW')
        password = Entry(frame, **entry_config, show='*')
        password.grid(row=6, column=1, rowspan=3, sticky='NSEW')
        Button(frame, text='Register', **button_config, command=lambda: (Users.add_user(username.get(), password.get(), True), login())).grid(row=9, column=0, rowspan=3, columnspan=2, sticky='NSEW')

    else:
        # Checking login information given
        def check(username, password):
            if Users.check_login(username, password) != list():
                main()
            else:
                login()

        Label(frame, text='Warehouse manager login', **label_config).grid(row=0, column=0, rowspan=3, columnspan=2, sticky='NSEW')
        Label(frame, text='Username: ', **label_config).grid(row=3, column=0, rowspan=3, sticky='NSEW')
        Label(frame, text='Password: ', **label_config).grid(row=6, column=0, rowspan=3, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=3, column=1, rowspan=3, sticky='NSEW')
        password = Entry(frame, **entry_config, show='*')
        password.grid(row=6, column=1, rowspan=3, sticky='NSEW')
        Button(frame, text='Login', **button_config, command=lambda: check(username.get(), password.get())).grid(row=9, column=0, rowspan=3, columnspan=2, sticky='NSEW')


login()
mainloop()

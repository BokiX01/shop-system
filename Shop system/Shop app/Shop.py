from tkinter import *
from resources.items import Items
from resources.users import Users
from os.path import exists

# Creating root window
root = Tk()
root.title('Shopping app')
root.geometry('800x600')

# Configuring root window so window frame can strech
Grid.rowconfigure(root, index=0, weight=1)
Grid.columnconfigure(root, index=0, weight=1)

# Creating window frame for all widgets
frame = Frame(root, padx=5, pady=5)
frame.grid(sticky='NSEW')
frame.config(bg='#383838')

# Configuring window frame so widgets can strech
for i in range(20):
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


def main():
    for widget in frame.winfo_children():
        widget.grid_forget()

    global total_price
    global list_of_items
    total_price = 0
    list_of_items = []

    # Adding item in the cart
    def add_item(item_id_or_name):
        item.delete(0, END)
        items_list.config(state=NORMAL)
        text = ''
        for item_info in Items.get_info(item_id_or_name):
            text += f'\tItem name: {item_info[0].capitalize()};\tPrice: {item_info[1]} kn'
            if item_info[2] > 0:
                text += f';\tDiscount: {item_info[2]}%'
            text += '\n'
        list_of_items.append(text)
        items_list.insert('1.0', text)
        items_list.config(state=DISABLED)
        price.config(state=NORMAL)
        global total_price
        total_price += float(item_info[1]) - float(item_info[1]) * float(item_info[2]) / 100
        price.delete(0, END)
        price.insert(0, f'{round(total_price, 2)} kn')
        price.config(state=DISABLED)

    # Removing item from the cart
    def remove_item(item_id_or_name):
        item.delete(0, END)
        items_list.config(state=NORMAL)
        text = ''
        for item_info in Items.get_info(item_id_or_name):
            text += f'\tItem name: {item_info[0].capitalize()};\tPrice: {item_info[1]} kn'
            if item_info[2] > 0:
                text += f';\tDiscount: {item_info[2]}%'
            text += '\n'

        items_list.delete('1.0', END)
        try:
            list_of_items.remove(text)
            price.config(state=NORMAL)
            global total_price
            total_price -= float(item_info[1]) - float(item_info[1]) * int(item_info[2]) / 100
            price.delete(0, END)
            price.insert(0, f'{round(total_price, 2)} kn')
            price.config(state=DISABLED)
        except ValueError:
            pass

        for i in list_of_items:
            items_list.insert('1.0', i)
        items_list.config(state=DISABLED)

    # Checking out and saving receipt into a file
    def check_out():
        file_name = 'receipt0'
        while True:
            if exists(f'receipts/{file_name}'):
                suffix = int(file_name.removeprefix('receipt')) + 1
                file_name = f'receipt{suffix}'
            else:
                with open(f'receipts/{file_name}.txt', 'w') as f:
                    f.writelines(list_of_items)
                    f.write(f'\n\tTotal price: {round(total_price, 2)}')
                main()
                break

    item = Entry(frame, **entry_config)
    item.grid(row=0, column=0, rowspan=4, sticky='NSEW')

    items_list = Text(frame, **text_config, state=DISABLED)
    items_list.grid(row=0, column=1, rowspan=12, columnspan=2, sticky='NSEW')

    Button(frame, text='Add item', **button_config, command=lambda: add_item(item.get())).grid(row=4, column=0, rowspan=4, sticky='NSEW')
    Button(frame, text='Remove item', **button_config, command=lambda: remove_item(item.get())).grid(row=8, column=0, rowspan=4, sticky='NSEW')

    Label(frame, text='Total price: ', **label_config).grid(row=12, column=0, rowspan=4, sticky='NSEW')

    price = Entry(frame, **entry_config)
    price.grid(row=12, column=1, rowspan=4, columnspan=2, sticky='NSEW')
    price.insert(0, f'{total_price} kn')
    price.config(state=DISABLED)

    Button(frame, text='Check out', **button_config, command=check_out).grid(row=16, column=0, rowspan=4, columnspan=3, sticky='NSEW')


# Login into the application
def login():
    for widget in frame.winfo_children():
        widget.grid_forget()

    # Checking if there is any users in database
    if Users.list_users() == list():
        # Register for first user whose administration level will be set to True
        Label(frame, text='Shop register', **label_config).grid(row=0, column=0, rowspan=5, columnspan=2, sticky='NSEW')
        Label(frame, text='Username: ', **label_config).grid(row=5, column=0, rowspan=5, sticky='NSEW')
        Label(frame, text='Password: ', **label_config).grid(row=10, column=0, rowspan=5, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=5, column=1, rowspan=5, sticky='NSEW')
        password = Entry(frame, **entry_config, show='*')
        password.grid(row=10, column=1, rowspan=5, sticky='NSEW')
        Button(frame, text='Register', **button_config, command=lambda: (Users.add_user(username.get(), password.get(), True), login())).grid(row=15, column=0, rowspan=5, columnspan=2, sticky='NSEW')

    else:
        # Checking login information given
        def check(username, password):
            if Users.check_login(username, password) != list():
                main()
            else:
                login()

        Label(frame, text='Shop login', **label_config).grid(row=0, column=0, rowspan=5, columnspan=2, sticky='NSEW')
        Label(frame, text='Username: ', **label_config).grid(row=5, column=0, rowspan=5, sticky='NSEW')
        Label(frame, text='Password: ', **label_config).grid(row=10, column=0, rowspan=5, sticky='NSEW')
        username = Entry(frame, **entry_config)
        username.grid(row=5, column=1, rowspan=5, sticky='NSEW')
        password = Entry(frame, **entry_config, show='*')
        password.grid(row=10, column=1, rowspan=5, sticky='NSEW')
        Button(frame, text='Login', **button_config, command=lambda: check(username.get(), password.get())).grid(row=15, column=0, rowspan=5, columnspan=2, sticky='NSEW')


login()
mainloop()

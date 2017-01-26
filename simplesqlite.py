from database import DB
from menu import Menu, Dialogs

'''Simple application to insert update and delete records from a database'''


def run():
    # create tables
    db = DB()
    db.create_tables()

    # loop
    while True:

        # display menu
        Menu.display()

        # get user input
        selection = Menu.get_user_input()

        if selection == 1:
            # returns a tuple with  ( name, country, number of catches )
            data = Dialogs.show_create()

            db.insert(data)

        if selection == 2:

            data = db.get_all()

            Menu.print_results(data)

        if selection == 5:
            db.close_connection()
            exit()

if __name__ == "__main__":
    run()

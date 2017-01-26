class Menu:

    menu_options = ['create', 'find', 'update', 'delete', 'quit']

    def __init__(self):
        pass

    @staticmethod
    def display():
        print() #empty newline
        menu_num = 1
        for value in Menu.menu_options:
            print(menu_num, value)
            menu_num += 1

    @staticmethod
    def get_user_input():
        while True:
            try:
                selection = int(input('\n'))
                if selection not in range(len(Menu.menu_options) + 1):
                    print("\nWas that a valid menu option?")
                    pass
                else:
                    return selection

            except ValueError as ve:
                print("\nWas that a number?")

            except KeyboardInterrupt as ki:

                exit('Goodbye')


    @staticmethod
    def print_results(data):
        if len(data) == 0:
            print('No data')
        else:
            print(data)


class Dialogs:

    @staticmethod
    def show_create():
        name = input('Enter name\n')
        country = input('Enter country\n')

        while True:
            try:
                catches = int(input('Enter number of catches\n'))
                return name, country, catches

            except ValueError as ve:
                print("\nWas that a number?\n")


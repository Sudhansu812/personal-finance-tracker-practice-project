from cli import show_main_menu, get_string_input, get_numeric_input, get_date_input
from features.tracker import TrackerService as app 

def main():
    while (True):
        choice = show_main_menu()
        if choice == 0:
            app.get_summary()
        elif choice == 1:
            app.add_transaction()
        elif choice == 2:
            app.filter_by_category()
        elif choice == 3:
            app.delete_transaction()
        else:
            return

        input("Press any key to continue...")

if __name__ == '__main__':
    main()
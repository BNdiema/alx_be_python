from shopping_list_manager import  add_items, remove_item, view_items, display_menu


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_items()
        elif choice == '2':
            # Prompt for and remove an item
            remove_item()
        elif choice == '3':
            # Display the shopping list
            view_items()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
shopping_list = []

def add_items():
    items = input("Add an item(s) to the list.")
    items_in_list = [item.strip() for item in items.split(',')]
    shopping_list.extend(items_in_list)
    print(shopping_list)


def remove_item():
    item = input("Remove item from the list.")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed")
    else:
        print(f"{item} is not on the list")
    print(shopping_list)

def view_items():
    if shopping_list:
        print(shopping_list)
    else:
        print("Shopping list is empty.")


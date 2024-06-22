def show_todo_list():
    try:
        with open("todo_list.txt", "r") as file:
            items = file.readlines()
            for i, item in enumerate(items):
                print(f"{i + 1}. {item.strip()}")
    except FileNotFoundError:
        print("No to-do list found.")

def add_item(item):
    with open("todo_list.txt", "a") as file:
        file.write(f"{item}\n")

def remove_item(index):
    with open("todo_list.txt", "r") as file:
        items = file.readlines()
    with open("todo_list.txt", "w") as file:
        for i, item in enumerate(items):
            if i != index - 1:
                file.write(item)

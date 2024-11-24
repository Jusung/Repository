todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"'{task}' added to the list!")

def show_tasks():
    print("\nTodo List:")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")

def remove_task(index):
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"'{removed}' removed from the list.")
    else:
        print("Invalid index!")


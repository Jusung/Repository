todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"'{task}' added to the list!")

def show_tasks():
    print("\nTodo List:")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")

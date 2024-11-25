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

# 1. 완료된 작업 표시 (mark_done)
def mark_done(index):
    if 0 <= index < len(todo_list):
        todo_list[index] += " ✅"
        print(f"Task {index + 1} marked as done!")
    else:
        print("Invalid index!")        

# 2. 모든 작업 초기화 (clear_tasks)
def clear_tasks():
    todo_list.clear()
    print("All tasks cleared!")

# 3. 작업 검색 (search_tasks)
def search_tasks(keyword):
    print(f"\nSearch results for '{keyword}':")
    found = False
    for idx, task in enumerate(todo_list, start=1):
        if keyword.lower() in task.lower():
            print(f"{idx}. {task}")
            found = True
    if not found:
        print("No matching tasks found.")

# 실행 예제
add_task("Learn Python")
add_task("Do Git practice")
show_tasks()
remove_task(0)
show_tasks()
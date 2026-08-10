import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n------ TO-DO LIST ------")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['task']}")
    print()

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Mark task complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as completed: "))
        tasks[num - 1]["completed"] = True
        print("Task completed!")
    except:
        print("Invalid task number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed['task']}")
    except:
        print("Invalid task number.")

# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved successfully!")
            print("Thank you for using the To-Do List App.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
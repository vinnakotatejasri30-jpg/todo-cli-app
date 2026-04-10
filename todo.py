# To-Do List Application (Console-Based)

tasks = []

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        # If file doesn't exist, create it
        open("tasks.txt", "w").close()

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task
def add_task():
    task = input("Enter task: ")
    if task.strip() == "":
        print("Task cannot be empty!")
        return
    tasks.append(task)
    save_tasks()
    print("✅ Task added successfully!")

# View all tasks
def view_tasks():
    if not tasks:
        print("📭 No tasks available")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Remove a task
def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"❌ Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main menu
def main():
    load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
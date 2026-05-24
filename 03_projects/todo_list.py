print("\n🚀 Welcome to the To-Do List App\n")

import os  # (optional, not used yet idk what it means atm)

tasks = []

def main_menu():  # so def is used to define a function, and the code inside it is indented. This function will be called to display the main menu of the app.
    print("\n━━━━━━━━━━━━━━━━━━━━━━")
    print("🗂️  TO-DO LIST MANAGER")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    print("1️⃣  Add Task")
    print("2️⃣  View Tasks")
    print("3️⃣  Mark Complete")
    print("4️⃣  Delete Task")
    print("5️⃣  Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━")


def add_task():
    task = input("✍️  Enter task: ")
    tasks.append({"task": task, "done": False}) #bit confused on this line x_x 
    print("🎉 Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\n📋 YOUR TASKS:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⏳"
        print(f"{i}. {status} {task['task']}")

def mark_complete():
    view_tasks()
    if tasks:
        try:
            num = int(input("✔️ Enter task number to mark complete: "))
            tasks[num - 1]["done"] = True
            print("🎯 Task marked as complete!")
        except:
            print("⚠️ Invalid input. Please enter a valid number.")


def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("🗑️ Enter task number to delete: "))
            removed = tasks.pop(num - 1)
            print(f"🗑️ Deleted: {removed['task']}")
        except:
            print("⚠️ Invalid input. Please enter a valid number.")


# main loop
while True:
    main_menu()
    choice = input("👉 Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Goodbye! Stay Strong lil bro 🚀")
        break
    else:
        print("❌ Invalid option, try again.")
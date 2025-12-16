tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append({"task": task, "status": "Pending"})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"], "-", tasks[i]["status"])

    elif choice == "3":
        num = int(input("Enter task number to update: ")) - 1
        if 0 <= num < len(tasks):
            new_task = input("Enter new task name: ")
            tasks[num]["task"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        num = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["status"] = "Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")


# DecodeLabs Project 1 - To-Do List

tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        print("\n------ YOUR TASKS ------")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
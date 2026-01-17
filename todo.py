tasks = []

while True:
    print("\n====================================")
    print("        TO-DO LIST – TASK MANAGER")
    print("====================================")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Exit the Program")
    print("====================================")

    choice = input("Please select an option (1–4): ")

    if not choice.isdigit():
        print("Invalid input. Please enter numbers only.")
        continue

    choice = int(choice)

    if choice == 1:
        print("\n--- Add Tasks (type 'done' when you finish adding tasks) ---")
        count = 0

        while True:
            new_task = input("Enter a task: ")

            if new_task.lower() == "done":
                if count > 0:
                    print(f"{count} task(s) have been successfully added to your To-Do List.")
                else:
                    print("No tasks were added.")
                break

            tasks.append(new_task)
            count += 1

    elif choice == 2:
        if len(tasks) == 0:
            print("\nYour task list is currently empty.")
        else:
            print("\n--- Your Current Tasks ---")
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i += 1

    elif choice == 3:
        if len(tasks) == 0:
            print("\nThere are no tasks available to delete.")
        else:
            print("\n--- Select a Task to Delete ---")
            i = 1
            for task in tasks:
                print(i, ".", task)
                i += 1

            num = input("Enter the number of the task you want to delete: ")

            if not num.isdigit():
                print("Invalid input. Please enter a valid task number.")
                continue

            num = int(num)

            if 1 <= num <= len(tasks):
                print("\nSelected Task:")
                print(">>", tasks[num - 1])

                confirm = input("Are you sure you want to delete this task? (yes/no): ")

                if confirm.lower() == "yes":
                    deleted_task = tasks.pop(num - 1)
                    print("\n*** TASK DELETED SUCCESSFULLY ***")
                    print("Deleted Task:", deleted_task)

                    if len(tasks) == 0:
                        print("Your task list is now empty.")
                    else:
                        print("\n--- Updated Task List ---")
                        i = 1
                        for task in tasks:
                            print(i, ".", task)
                            i += 1
                else:
                    print("Deletion cancelled. The task was not deleted.")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("\nThank you for using the To-Do List.")
        print("The program has been closed.")
        break

    else:
        print("Please select a valid option between 1 and 4.")

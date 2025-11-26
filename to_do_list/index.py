from prettytable import PrettyTable

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, no_of_todo: int) -> None:
        for i in range(0, no_of_todo):
            task = input(f"Enter taks {i+1}: ")
            self.tasks.append(task)


    def show_tasks(self) -> None:
        if not self.tasks:
            print("⚠ No tasks found.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Task"]

        for idx, task in enumerate(self.tasks, start=1):
            table.add_row([idx, task])

        print(table)

    def update_task(self, task_id: int, new_title: str) -> None:
        if 1 <= task_id <= len(self.tasks):
            old_title = self.tasks[task_id - 1]
            self.tasks[task_id - 1] = new_title
            print(f"✔ Updated: '{old_title}' → '{new_title}'")
        else:
            print("❌ Invalid task ID")

    # DELETE
    def delete_task(self, task_id: int) -> None:
        if 1 <= task_id <= len(self.tasks):
            removed = self.tasks.pop(task_id - 1)
            print(f"🗑 Deleted: {removed}")
        else:
            print("❌ Invalid task ID")



def main():
    todo = Todo()

    while True:
        print("\n=== TODO MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            no_of_task = int(input("Enter no of task: "))
            todo.add_task(no_of_task)

        elif choice == "2":
            todo.show_tasks()

        elif choice == "3":
            todo.show_tasks()
            task_id = int(input("Enter task ID to update: "))
            new_title = input("Enter new task title: ")
            todo.update_task(task_id, new_title)

        elif choice == "4":
            todo.show_tasks()
            task_id = int(input("Enter task ID to delete: "))
            todo.delete_task(task_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()


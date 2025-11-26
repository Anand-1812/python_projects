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

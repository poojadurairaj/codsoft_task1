class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "✓" if task["done"] else "✗"
                print(f"{index}. [{status}] {task['task']}")

    def mark_task_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task['task']},{task['done']}\n")

    def load_from_file(self, filename):
        self.tasks = []
        try:
            with open(filename, "r") as f:
                for line in f:
                    task, done = line.strip().split(",")
                    self.tasks.append({"task": task, "done": bool(done)})
        except FileNotFoundError:
            print("No previous data found.")

def main():
    todo_list = ToDoList()
    filename = "todo.txt"  # File to store tasks persistently

    # Load tasks from file if exists
    todo_list.load_from_file(filename)

    while True:
        print("\n===== ToDo List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save and Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as done: "))
            todo_list.mark_task_done(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            todo_list.save_to_file(filename)
            print("Tasks saved successfully. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

"""Persistent To-Do List - CODSOFT Python Internship Project."""

from pathlib import Path

DATA_FILE = Path("tasks.txt")


def load_tasks():
    """Load tasks from the local text file."""
    if not DATA_FILE.exists():
        return []

    return [line.strip() for line in DATA_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]


def save_tasks(tasks):
    """Save tasks to the local text file."""
    DATA_FILE.write_text("\n".join(tasks), encoding="utf-8")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Tasks ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter a new task: ").strip()

    if not task:
        print("Task cannot be empty.")
    elif task in tasks:
        print("Task already exists.")
    else:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def mark_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark as completed: "))
        task = tasks[number - 1]
        if not task.startswith("[Completed] "):
            tasks[number - 1] = f"[Completed] {task}"
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Task is already completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    """Run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()

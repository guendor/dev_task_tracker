import os
import database as db

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def show_tasks():
    clear_screen()
    print("--- DevTask Tracker ---")
    tasks = db.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "✔️" if task['done'] else "❌"
            print(f"{status} [{task['id']}] - {task['description']}")
    print("------------------------\n")
    
def main_menu():
    # Exibit the main menu and handle user input
    while True:
        show_tasks()
        print("Options:")
        print(" [1] Add Task")
        print(" [2] Update Task Status")
        print(" [3] Delete Task")
        print(" [0] Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            desc = input("Insert task description: ")
            db.add_task(desc)
        elif choice == '2':
            try:
                task_id = int(input("Insert ID of the task to update: "))
                db.update_task_status(task_id, done=1)
            except ValueError:
                print("\n❌ Invalid ID. Please enter a number.")
                input("Press Enter to continue...")
        elif choice == '3':
            try:
                task_id = int(input("Insert ID of the task to delete: "))
                db.delete_task(task_id)
            except ValueError:
                print("\n❌ Invalid ID. Please enter a number.")
                input("Press Enter to continue...")
        elif choice == '0':
            print("\nThank you for using the DevTask Tracker! 👋")
            break
        else:
            print("\n❌ Invalid option. Please try again.")
            input("Press Enter to continue...")
            
if __name__ == "__main__":
    main_menu()
    

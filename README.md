# DevTask Tracker CLI

A simple and efficient command-line task manager built with Python and SQLite. This project demonstrates core database skills, including data modeling and CRUD operations.

This is the final project of my 30-day plan to land a Python developer role, showcasing my ability to build persistent data-driven applications.

## Features

-   **Add Tasks:** Quickly add new tasks to your to-do list.
-   **List All Tasks:** View all your tasks with their current status (done or pending).
-   **Mark as Done:** Update the status of any task to completed.
-   **Delete Tasks:** Remove tasks you no longer need.
-   **Persistent Storage:** All tasks are stored in a local SQLite database (`tasks.db`), ensuring your data is safe even after closing the application.

## Skills Demonstrated

-   **Database Management:** Use of the built-in `sqlite3` library to manage a local database.
-   **SQL Operations:** Implementation of the full CRUD (Create, Read, Update, Delete) cycle.
-   **Data Modeling:** Designing a simple but effective database schema for the tasks table.
-   **Modular Code:** Separation of concerns between the database logic (`database.py`) and the user interface (`main.py`).
-   **Secure Coding:** Use of parameterized queries to prevent SQL injection vulnerabilities.

## How to Run

Since this project uses Python's built-in `sqlite3` library, no external packages are needed.

1.  Clone this repository.
2.  Navigate to the project directory:
    ```bash
    cd dev_task_tracker
    ```
3.  Run the application:
    ```bash
    python main.py
    ```

## Demo

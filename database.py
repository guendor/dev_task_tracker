import sqlite3

DATABASE_FILE = "tasks.db"

def get_db_connection(): 
    # Create a connection to the SQLite database
    conn = sqlite3.connect(DATABASE_FILE)
    # This allows us to access columns by name (e.g., row['description'])
    conn.row_factory = sqlite3.Row 
    return conn

def create_table():
    # Create the tasks table if it doesn't exist
    conn = get_db_connection()
    cursor = conn.cursor()
    # SQL command to create the tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            done BOOLEAN NOT NULL CHECK (done in (0, 1)) DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()
    
def add_task(description):
    # Add a new task to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    
    conn.commit()
    conn.close()
    
def get_all_tasks():
    # Retrieve all tasks from db
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, done):
    # Update the tasks' status (completed or not)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (done, task_id))
    
    conn.commit()
    conn.close()
    
def delete_task(task_id):
    # Delete a task from db
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    
    conn.commit()
    conn.close()
    
# Make sure the table is generated when the module is imported
create_table()
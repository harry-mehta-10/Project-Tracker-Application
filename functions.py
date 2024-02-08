import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def create_project_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
    except sqlite3.Error as e:
        print(e)

def create_project(conn, project_name):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projects (name) VALUES (?)", (project_name,))
        conn.commit()
        print("Project created successfully.")
    except sqlite3.Error as e:
        print(e)

def view_projects(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()

        if not projects:
            print("Oh no! There are no projects to see. Kindly create a new one. ")
        else:
            for project in projects:
                print(f"Project ID: {project[0]}, Name: {project[1]}")
    except sqlite3.Error as e:
        print(e)

def delete_project(conn, project_id):
    try:
        cursor = conn.cursor()

        # Check if the project with the given ID exists
        cursor.execute("SELECT id FROM projects WHERE id=?", (project_id,))
        existing_project = cursor.fetchone()

        if existing_project:
            # Project exists, proceed with deletion
            cursor.execute("DELETE FROM projects WHERE id=?", (project_id,))
            conn.commit()
            print(f"Project with ID {project_id} has successfully been created.")
        else:
            # Project does not exist, display an error message
            print(f"Error: Project with ID {project_id} not found. Please enter a valid project ID.")

    except sqlite3.Error as e:
        print(e)



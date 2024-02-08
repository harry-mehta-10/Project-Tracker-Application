from functions import create_connection, create_project_table, create_project, view_projects, delete_project

def main():
    # Create a database connection
    conn = create_connection('database.db')

    if conn is not None:
        with conn:
            create_project_table(conn)

    while True:
        print()
        print("## PROJECT TRACKER APPLICATION BY HARRY ##\n")

        menu_options = [
            "To see all the projects created",
            "To create a new project",
            "To delete a project",
            "To exit"
        ]

        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter your input (1/2/3/4): ")

        if choice == '1':
            view_projects(conn)
        elif choice == '2':
            project_name = input("Enter project name: ")
            create_project(conn, project_name)
            print(f"Project '{project_name}' created successfully.")
        elif choice == '3':
            project_id = input("Enter project ID to delete: ")
            delete_project(conn, project_id)
        elif choice == '4':
            print("The Project Tracker is getting closed, bye!")
            break 
        else:
            print("The input given is wrong, please try again!")

if __name__ == "__main__":
    main()




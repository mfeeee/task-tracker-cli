import sys, json, os, datetime

current_time = datetime.datetime.now().isoformat()
FILE_NAME = "tasks.json"

# --------------------
#  Database Functions
# --------------------
# Load all tasks
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    else:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

# Save a task
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# --------------------------
#  Business Logic Functions
# --------------------------

# Add an task to the list
def add_task(description): 
        tasks = load_tasks()

        if not tasks:
            new_id = 1
        else:
            new_id = tasks[-1]["id"] + 1

        new_task = {
            "id": new_id,
            "description": description,
            "status": "todo",
            "createdAt": current_time,
            "updatedAt": current_time
        }

        tasks.append(new_task)
        save_tasks(tasks)
        print(f'Task added successfully (ID: {new_task["id"]})')

# List tasks with filter
def filter_tasks(tasks, filter):
    cont = 0
    for task in tasks:
        if task["status"] == filter:
            cont += 1
            print(f'[{task["id"]}] {task["description"]} - {task["status"]}')

    if cont == 0:
        return False
    
    return True

# Show all tasks on the list
def list_tasks(filter=None):
    tasks = load_tasks()

    # Verify if there are tasks
    if not tasks:
        print("No tasks found.")

    # Verify if the list has a filter
    if filter:
        valid_filters = ["todo", "in-progress", "done"] # Types of status

        if filter not in valid_filters:
            print("Invalid filter. Use: \033[4mtodo\033[0m, \033[4min-progress\033[0m, or \033[4mdone\033[0m.")
            sys.exit(1)
        
        if not filter_tasks(tasks, filter):
            print(f"No tasks found with status: {filter}")
    else:
        for task in tasks:
            print(f'[{task["id"]}] {task["description"]} - {task["status"]}')

# Update a task on the list based on ID
def update_task(task_id, new_description):
    tasks = load_tasks()
    task_found = False
    
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = current_time
            task_found = True
            break
    
    if task_found:
        save_tasks(tasks)
        print('Task updated successfully')
    else:
        print(f'Task not found (ID:{task_id})')

# Delete a task on the list based on ID
def delete_task(task_id):
    tasks = load_tasks()
    task_found = False
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            task_found = True
            break
    
    if task_found:
        save_tasks(tasks)
        print('Task deleted succesfully')
    else:
        print(f'Task not found (ID:{task_id})')

# Change a task's status based on ID
def change_status(task_id, new_status):
    tasks = load_tasks()
    task_found = False
        
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = current_time
            task_found = True
            break
    
    if task_found:
        save_tasks(tasks)
        print('Task status updated succesfully')
    else:
        print(f'Task not found (ID:{task_id})')

# CLI Guide
def cli_guide():
    print('Task Tracker CLI Guide:')
    print('- To add a new task: python task-cli \033[4madd\033[0m "Buy groceries"\n')
    print('- To update and delete a task: python task-cli \033[4mupdate [id]\033[0m "Buy groceries and cook dinner"')
    print('                               python task-cli \033[4mdelete [id]\033[0m\n')
    print('- To mark a task as in progress or done: python task-cli \033[4mmark-in-progress [id]\033[0m')
    print('                                         python task-cli \033[4mmark-done [id]\033[0m\n')
    print('- To list all tasks: python task-cli \033[4mlist\033[0m\n')
    print('- To list tasks by status: python task-cli \033[4mlist done\033[0m')
    print('                           python task-cli \033[4mlist todo\033[0m')
    print('                           python task-cli \033[4mlist in-progress\033[0m')

# -------
#  CLI 
# -------
def main():
    # Verify user's input lenght
    if len(sys.argv) <= 1:
        cli_guide()
        sys.exit(1)

    else:
        command = sys.argv[1]
   
        if command == "add":
            if len(sys.argv) < 3:
                print("Invalid command. Use: add \033[4m\"task name\"\033[0m")
                sys.exit(1)

            add_task(sys.argv[2])
        
        elif command == "list":
            if len(sys.argv) == 3:
                list_tasks(sys.argv[2])
            else:
                list_tasks()
        
        elif command == "update":
            if len(sys.argv) < 4:
                print("Invalid command. Use: update \033[4m[id] \"new task name\"\033[0m")
                sys.exit(1)

            update_task(int(sys.argv[2]), sys.argv[3])
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Invalid command. Use: delete \033[4m[id]\033[0m")
                sys.exit(1)

            delete_task(int(sys.argv[2]))
        
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Invalid command. Use: mark-in-progress \033[4m[id]\033[0m")
                sys.exit(1)
            
            change_status(int(sys.argv[2]), "in-progress")

        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Invalid command. Use: done \033[4m[id]\033[0m")
                sys.exit(1)
            
            change_status(int(sys.argv[2]), "done")

        else:
            print(f'Unknown comand: {command}\n')
            cli_guide()
            sys.exit(1)

if __name__ == "__main__":
    main()
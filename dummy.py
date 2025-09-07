print("Welcome to my dummy version of a To Do App")
print("Select an option to get started")
print("1. Add Task\n2. Remove Task\n3. View Task\n4. Exit")
tasks=[]
def add_task ():
    taskname=input("Enter task: ")
    tasks.append({"task":taskname ,"status":False})
    print("Task added successfully")
def remove_task ():
    taskname=input("Enter the task you want to remove: ")
    for task in tasks:
        if task.get("task")==taskname:
            tasks.remove(task)
            print("Task removed!")
        
        return
    print("Task not found")
def view_tasks ():
    if not tasks:
        print("tasks not found")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            status = "[x]" if task["status"] else "[ ]"  # [x] completed, [ ] incomplete
            print(f"{i}. {status} {task['task']}")
        print("------------------\n")
    
while True:
    option=input("Enter option: ")
    if option =="1" :
        add_task()
    elif option=="2":
            remove_task()
    elif option=="3":
         view_tasks()
    elif option=="4":
        print("Exiting the task manager. Goodbye! i love you Lulu <3 keep your tasks in order and stay organized")
        break
    

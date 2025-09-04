tasks=[]

def add_task():
    #get task from user
    task = input ("Enter task:")
    #define task status
    task_info={"task" : task ,"completed":False}
    #add task to the list
    tasks.append(task_info)
    print("task added to the list succesfuly")
    print("-"*30)
    
    

def mark_task_complete():
    # get list of incomplete tasks
    incomplete_tasks=[task for task in tasks if task["completed"]==False]
    
    if not incomplete_tasks:
        print("NO task to mark as complete")
        return

    #show them to the user
    for i ,task in enumerate(incomplete_tasks) :
        print(f'{i+1}-{task["task"]}')
        print("-"*30)
       

    #get the task from the user
    task_num =int(input("Choice the task to compelet: "))
    
    #mark the task as completed
    incomplete_tasks[task_num-1]["completed"]=True
    #print a message to the user
    print("Task mark as completed")
    print("-"*30)
        


def view_tasks():

    #if there are not tasks ,print a message and return
    if not tasks:
        print("NO task to view")
        return

    for i ,task in enumerate(tasks) :
        
        status = "✔️" if task["completed"] else "❌"

        print(f'{i+1}.{task["task"]} {status}')
        print("-"*30)
   

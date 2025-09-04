
from functions import add_task,mark_task_complete,view_tasks

def main():
    message="""
    1- Add tasks to a list
    2- Mark task as complet
    3- Viwe tasks 
    4- Quite"""
    while True:

      print(message)
      choice =input("Enter your choice:")

      if choice == "1":
        add_task()

      elif choice =="2":
        mark_task_complete()

      elif choice =="3":
        view_tasks()

      elif choice =="4":
        break

      else:
        print("Invalid choice , please enter a number between 1 : 4")
        print("-"*30)


if __name__ == "__main__":
    main()
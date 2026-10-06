#   A To-Do List application is a useful project that helps users manage
#  and organize their tasks efficiently. This project aims to create a
#  command-line or GUI-based application using Python, allowing
#  users to create, update, and track their to-do lists

tasks=["task1","task2","task3"]
marked_tasks=[]
while True:
   print("1.view all tasks")
   print('2.add tasks')
   print('3.delete tasks')
   print("4. mark tasks")
   print("5.marked tasks")
   choose=input("select one ")
   if choose=="1":
       print(tasks)

   elif choose=="2":
       added_task=input("Enter the task name you want add ")
       if added_task in tasks:
          print("task is already in list")
       else:
          tasks.append(added_task)
          print("task added successfully")

   elif choose=="3":
       delete_task=input("Enter the task name you want to delete")
       if delete_task in tasks:
        tasks.remove(delete_task)
        print("deleted succesfully")
       else:
        print("task not found")

   elif choose=="4":
        mark_task=input("enter the task name you want mark")
        if mark_task in tasks:
        #  tasks.remove(mark_task)
         marked_tasks.append(mark_task)
         print("task marked successfully")
        else:
           print("enterd task is not fount in list") 

   elif choose=="5":
      print(marked_tasks)

   else:
    print("invaid select")

   menu=input("you want continue, yes/no")
   if menu=="yes":
    continue
   else:
      print("thankyou")
      break
    

    



     


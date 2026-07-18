import json
from datetime import datetime

tasks = []

priority_order = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

def load_tasks():
    global tasks
    try:
        with open("tasks_new.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open("tasks_new.json", "w") as file:
        json.dump(tasks, file, indent=4)

def display_menu():
    print("\n===== STUDY PLANNER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Edit Task")
    print("7. View Statistics")
    print("8. Filter Tasks")
    print("9. Export Tasks")
    print("10. Exit")

load_tasks()

while True:
    display_menu()
    choice = input("Enter your choice (1-10): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        due_date = input("Enter due date (DD-MM-YYYY): ")

        while True:
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            if priority in ["High", "Medium", "Low"]:
                break
            else:
                print("Invalid priority! Please enter High, Medium, or Low.")

        tasks.append({
            "name": task_name,
            "completed": False,
            "priority": priority,
            "due_date": due_date
        })

        save_tasks()
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            tasks.sort(key=lambda task: priority_order[task["priority"]])
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                due_date=datetime.strptime(task["due_date"],"%d-%m-%Y")
                today=datetime.today( )
                if not task["completed"] and due_date < today:
                	overdue="OVERDUE"
                else:
                	overdue=" "
                
                print(f"{i}. {status} - {task['name']} - {task['priority']} - Due: {task['due_date']}-{overdue}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {status} - {task['name']}")

            try:
                task_number = int(input("Enter task number to mark as completed: "))

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    save_tasks()
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    confirm = input(f"Are you sure you want to delete '{tasks[task_number - 1]['name']}'? (Y/N): ").upper()
                    if confirm == "Y":
                    	deleted_task = tasks.pop(task_number - 1) 
                    	save_tasks( )
                    	print("✅ Task deleted successfully!")
                    else:
                    	print("❌ Deletion cancelled.")
                    
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")
    elif choice == "5":
    	keyword = input("Enter task name to search:").lower( )
    	found = False
    	for i, task in enumerate(tasks, start=1):
    		if keyword in task["name"].lower( ):
    			status = "Completed" if task["completed"] else "Pending"
    			print(f"{i}.{status}-{task['name']}-{task['priority']}-Due:{task['due_date']}")
    			found = True
    		if not found:
    			print("No matching task.")
    
    			
    
    
    elif choice == "6":
         if len(tasks) == 0:
         	print("No tasks available.")

         else:
            for i, task in enumerate(tasks, start=1):
            	print(f"{i}. {task['name']}")
            try:
            		task_number = int(input("Enter task number to edit: "))
            		if 1 <= task_number <= len(tasks):
            		  new_name = input("Enter new task name: ")
            		  new_due_date = input("Enter new due date (DD-MM-YYYY): ")
            		  while True:
            		  	new_priority = input("Enter new priority (High/Medium/Low): ").capitalize()
            		  	if new_priority in ["High", "Medium", "Low"]:
            		  	   break
            		  	else:
            		  		print("Invalid priority!")
            		  tasks[task_number - 1]["name"] = new_name
            		  tasks[task_number - 1]["due_date"] = new_due_date
            		  tasks[task_number - 1]["priority"] = new_priority
            		  save_tasks()
            		  print("Task updated successfully!")
            		else:
            		   	print("Invalid task number.")
            		    
            except ValueError:
            		    	print("Please enter a valid number.")

    
        
        

    elif choice == "7":
    	total_tasks=len(tasks)
    	completed_tasks=0
    	for task in tasks:
    		if task["completed"]:
    		      	cimpleted_tasks += 1
    	pending_tasks= total_tasks-completed_tasks
    	if total_tasks > 0:
    		     completion_rate=(completed_tasks/total_tasks)*100
    	else:
    		     completion_rate = 0
    	print("\n====TASK STATISTICS====")
    	print(f"Total Tasks: {total_tasks}")
    	print(f"Completed Tasks: {completed_tasks}")
    	print(f"Pending Tasks:{pending_tasks}")
    	print(f"Completion Rate: {completion_rate: .2f}%")
    	
    		     
    elif choice == "8":
    	print("\n====FILTER TASKS====") 
    	print("1.View All Tasks")   
    	print("2. High Priority")
    	print("3. Medium Priority")
    	print("4. Low Priority")
    	print("5. Completed Tasks")
    	print("6. Pending Tasks")
    	print("7. Sort by due date")
    	
    	filter_choice = input("Choose an option:")
    	print("\nFiltered Tasks:\n")
    	if filter_choice == "7":
    		tasks.sort(key=lambda task: datetime.strptime(task["due_date"], "%d-%m-%Y"))
    	for i, task in enumerate(tasks, start=1):
    		status = "Completed" if task["completed"] else "Pending"
    		if filter_choice in  ["1","7"]:
    			print(f"{i}. {status} - {task['name']} - {task['priority']} - Due: {task['due_date']}")
    		elif filter_choice == "2" and task["priority"] == "High":
    			print(f"{i}. {status} - {task['name']} - {task['priority']} - Due: {task['due_date']}")
    		elif filter_choice == "3" and task["priority"] == "Medium":
    			print(f"{i}. {status} - {task['name']} - {task['priority']} - Due: {task['due_date']}")
    		elif filter_choice == "4" and task["priority"] == "Low":
    			print(f"{i}. {status} - {task['name']} - {task['priority']} - Due: {task['due_date']}")
    		elif filter_choice == "5" and task["completed"]:
    			print(f"{i}. {status} - {task['name']} - {task['priority']} - Due: {task['due_date']}")
    		elif filter_choice == "6" and not task["completed"]:
    			print(f"{i}. {status} - {task['name']} - {task['priority']} - Due: {task['due_date']}")
    
    		
    			      			
    			      		
    			      		
    
    elif choice == "9":
    	 with open("study_report.txt", "w") as file:
    	 	file.write("===== STUDY REPORT =====\n\n")
    	 	for task in tasks:
    	 		status = "Completed" if task["completed"] else "Pending"
    	 		file.write(f"Task Name : {task['name']}\n")
    	 		file.write(f"Priority  : {task['priority']}\n")
    	 		file.write(f"Status    : {status}\n")
    	 		file.write(f"Due Date  : {task['due_date']}\n")
    	 		file.write("----------------------------\n")
    	   
    
    	
    
    elif choice =="10":
        print("Thank you for using Study Planner!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 10.")
 
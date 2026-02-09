def student_management_system(): 
    student_grades = {
        "John": 90,
        "Melissa": 95,
        "David": 70,
        "Sarah": 65,
    }
    
    while True:
        print("\n--- Welcome to the Student Management System! ---")
        print("1 - Search for a Grade")
        print("2 - Register a New Student")
        print("3 - Exit")
        
        choice = input("Please enter the number of the action you want to perform: ")
        
        if choice == "1":
            search_name = input("Which student's grade would you like to see? ").capitalize()
            if search_name in student_grades:
                print(f"The grade for {search_name} is: {student_grades[search_name]}")
            else:
                print(f"Sorry, no student named {search_name} was found.")
                
        elif choice == "2":
            new_student = input("Enter the name of the new student: ").capitalize()
            new_grade = int(input(f"Enter the grade for {new_student}: "))
            
            student_grades[new_student] = new_grade
            print(f"{new_student} has been successfully registered.")
            print(f"Updated List: {student_grades}")
            
        elif choice == "3":
            print("Exiting the system... Have a great day!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

student_management_system()
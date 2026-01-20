roll_no = []
names = []
marks = []

print("===========================================")
print("           Student Marks Manager           ")
print("===========================================")
print()
print()

while True:
    print("   Menu   ")
    print("1. Add student details")
    print("2. View student details")
    print("3. Search by any roll number")
    print("4. Find Student with highest SGPI")
    print("5. Exit")
    print()

    choice=(input("Enter your choice: "))
    print()
    if not choice.isdigit():
        print("\nPlease enter numbers only\n")
        continue
    choice=int(choice)
    if choice==1:
        n=int(input("How many student's details do you want to add: "))
        print()
        i=1
        while i<=n:
            print("------ Enter details of student ",i, "-------")
            print()
            r = int(input("Enter roll number: "))
            if r in roll_no:
                print("Roll number already exists. Please enter a unique roll number.")
                continue
            name = input("Enter student name: ")
            m = float(input("Enter SGPI: "))
            if m<0 or m>10:
                print("\nPlease Enter correct SGPI\n")
                continue

            roll_no.append(r)
            names.append(name)
            marks.append(m)
            i += 1
            print("\n✔ Student details saved successfully!")
            print()
            print()

    elif choice==2:
        if len(roll_no)==0:
            print("\nNo Student data available\n")
        else:
            print("\n----Student Details----")

            for i in range(len(roll_no)):
                print("\nStudent", i + 1)
                print("Roll Number:", roll_no[i])
                print("Name:", names[i])
                print("SGPI:", marks[i])
                print()
                print()

    elif choice==3:
        if len(roll_no)==0:
            print("\nNo Student data available\n")
        else:
            while True:
                search_roll=int(input("Enter the roll number to search: "))
                if search_roll in roll_no:
                    index=roll_no.index(search_roll)
                    print("\n--- Student Found ---")
                    print("Roll Number:", roll_no[index])
                    print("Name:", names[index])
                    print("SGPI:", marks[index])
                    print()
                    print()
                    break
                else:
                    print("Student with that roll number not found")
                    print("Please enter correct Roll")
                print()
                print()

            
                
    elif choice==4:
        if len(roll_no)==0:
            print("\nNo Student data available\n")
        else:
            max_marks=max(marks)
            index=marks.index(max_marks)
            print("\n--- Student with highest SGPI ---")
            print("Roll number: ",roll_no[index])
            print("Name: ",names[index])
            print("SGPI: ",marks[index])
            print()
            print()
    elif choice==5:
        print("\nThank you for using Student Marks Manager")
        break

    else:
        print("\nInvalid choice , Please enter the correct number\n")



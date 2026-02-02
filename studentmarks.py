roll_no = []
names = []
marks = []

print("===========================================")
print("           Student Marks Manager           ")
print("===========================================\n\n") 
# \n is a escape character it mean next line , dont write print() for next line its not convinent

while True:
    print("   Menu   ")
    print("1. Add student details")
    print("2. View student details")
    print("3. Search by any roll number")
    print("4. Find Student with highest SGPI")
    print("5. Exit\n")

    choice= input("Enter your choice: ") # just removed the extra ()
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
            print("------ Enter details of student ",i, "-------\n")
            # r = int(input("Enter roll number: "))
            # user may not enter number so the code would be halted
            r = input("Enter roll number: ")
            if r.isdigit() :
                r = int(r)
            else : 
                print("invalid roll no")
                continue

            if r in roll_no:
                print("Roll number already exists. Please enter a unique roll number.")
                continue
            name = input("Enter student name: ")
            m = float(input("Enter SGPI: ")) # how dp u know user will not enetr "khf" and same thi swill halt the code
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


# this is an img addon i wanted to give u , if u are ok with it , just a tip

# in the code there is one problem when ever user enters wrong imput the code ends 
# but generally we dont want the code to stop on wrong input , like it better to give user 
# another chace for reinput
# like how would u feel if u enter wrong gmail and the website closes 😂 , we don't do it in professional life too

# i am doing it for 1 , but u can , if u want update it for all or just use it next time

# Addon , u have used continue to solve it but there is 1 flaw in it 

# lets take for choice 1 

# I enter roll no : 76 {correct}
# I enter name :- "Nik" {correct}
# I enter SGPA :- 65 {wrong for the condition m < 0 or m > 10} 🤯
# The problem not ur code well destroy the roll no and name i entered 
# I now need to start from the very begning
# Do u see the problem , No ?
# what if ue i code is big , like enter email , phon no ... 
# I filled all details it took 30 min , 35 opt {35 inpt}
# I entered 1 wrong detail and all goon and now i need to restart from the first input 😭

# solution ? :- for each time u need to reask user to enter the value when the enter wrong value 
# Make a fresh loop just for that value

# See the example

# its a general example but logic remains the same 

# a = input("Enter a number :- ")

# while not a.isdigit() :
#   print("Invalid")
#   a = input("Enter a number :- ") 
# re asking here it slef not continue key word , now only this section will loop 
# and not the whole loop 
# so now i dont need to restart the whole form

# There are 1-2 small error like it can break but i guess it ok , for now can be skiped 

# I just though could add value to ur code :)
# Hope it helps 😊

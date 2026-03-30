student_info = {'001' : ["Kian Dela Cruz", 17, 11, 50, 25, 25],
            '002' : ["Nhico Bigcas", 16, 11, 25, 50, 25],
            '003' : ["Justin Pelayo", 16, 12, 25, 50, 50],
            '004' : ["Mishael Masiglat", 18, 12, 50, 50, 50],
            '005' : ["Dylan Arps", 16, 13 , 0, 0, 0],
            '006' : ["RF Decena", 18, 13 , 25, 0, 50]}

def display_menu():
    print("What would you like to do?")
    print("1. View student's info.")
    print("2. View credits.")
    print("3. View endorsements.")
    print("4. View a year level.")
    print("5. Add credits.")
    print("6. View summary.")
    print("7. Passed students")
    print("8. End program")
def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("That is not a valid integer, try again.")

def get_cred(prompt):
    while True:
        try: 
            cred = int(input(prompt))
            if cred > 14: 
                print("Number must be below 14")
            elif cred <= 0:
                print("Number must be above 0")    
            else:
                return cred
                break
        except ValueError:
            print("That is not a valid integer, try again.")

def view_data():
    for stu in student_info:
        print(f"ID: {(stu)} Name: {student_info[stu][0]} Age: {student_info[stu][1]} Year: {student_info[stu][2]}")

def view_credits():
    for stu in student_info:
        print(f"Name: {student_info[stu][0]} ID: {(stu)} Achieved: {student_info[stu][3]} Merit: {student_info[stu][4]} Excellence: {student_info[stu][5]}")

def view_endorsements():
    for stu in student_info:
        print(f"Name: {student_info[stu][0]} ID: {(stu)}")
        if student_info[stu][3] >= 50:
            print("Endorsement: Achieved")
        if student_info[stu][4] >=50:
            print("Endorsement: Merit")
        if student_info[stu][5] >= 50:
            print("Endorsement: Excellence")
        print("-----")

def student_year(student_info):
    year = get_int("From what year do you want to see?: ")
    print()
    print("-----")
    for stu in student_info:
        if student_info[stu][2] == year:
            print(f"Name: {student_info[stu][0]} Age: {student_info[stu][1]} Year: {student_info[stu][2]}")
    print("-----")

def add_cred(student_info, get_int):
    while True:
        print("-----")
        identification = input("From what ID do you want to add to: ")
        credits = get_cred("How many credits do you want to add: ")
        level = input("What level: ").lower()   
        if level == "achieved":
            student_info[identification][3] += credits
        elif level == "merit":
            student_info[identification][4] += credits
        elif level == "excellence":
            student_info[identification][5] += credits
        else:
            print("Invalid level, please input Achieved, Merit, or Excellence")
            print("Try again")
            print()
            continue
        print("All done!")
        print("-----")
        print()
        break

def view_summary():
    for stu in student_info:
        print(f"ID: {(stu)} Name: {student_info[stu][0]} Age: {student_info[stu][1]} Year: {student_info[stu][2]} ")
        if student_info[stu][3] >= 50:
            print("Endorsement: Achieved")
        if student_info[stu][4] >=50:
            print("Endorsement: Merit")
        if student_info[stu][5] >= 50:
            print("Endorsement: Excellence")
        print()

while True:
    print()
    display_menu()
    print()
    choice = input(": ")
    print()
    if choice == "1":
        print("-----")
        view_data()
        print("-----")
    elif choice == "2":
        print("-----")
        view_credits()
        print("-----")
    elif choice == "3":
        print("-----")
        view_endorsements()
        print()
    elif choice == "4":
        student_year(student_info)
    elif choice == "5":
        add_cred(student_info, get_int)    
    elif choice == "6":
        print("---")
        view_summary()
        print("---")
    elif choice == '7':
        print("Students who have passed NCEA:")
        for stu in student_info.values():
            if sum(stu[3:]) >= 80:
                print(f"{stu[0]} Year: {stu[2]}")
    elif choice == "8":
        print("Thanks see you next time")
        break 
    else: 
        print("Invalid input, try again.")
        continue
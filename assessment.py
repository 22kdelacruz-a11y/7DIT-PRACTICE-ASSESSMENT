def display_menu():
    print("What would you like to do?")
    print("1. View student's info.")
    print("2. View NCEA.")
    print("3. View endorsements.")
    print("4. View a year level..")
    print("5. Add credits.")
    print("6. Add students.")
    print("7. View summary.")

student_info = {'001' : ["Kian Dela Cruz", 17, 12, 50, 25, 25],
            '002' : ["Nhico Bigcas", 16, 12, 25, 50, 25],
            '003' : ["Justin Pelayo", 16, 12, 25, 50, 50],
            '004' : ["Mishael Masiglat", 18, 11, 50, 50, 50]}

def view_data():
    for stu in student_info:
        print(f"ID: {(stu)} Name: {student_info[stu][0]} Age: {student_info[stu][1]} Year: {student_info[stu][2]}")

def view_ncea():
    for stu in student_info:
        print(f"ID: {(stu)} Achieved: {student_info[stu][3]} Merit: {student_info[stu][4]} Excellence: {student_info[stu][5]}")

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

def view_endorsements():
    for stu in student_info:
        print(f"ID: {(stu)}")
        if student_info[stu][3] >= 50:
            print("Endorsement: Achieved")
        if student_info[stu][4] >=50:
            print("Endorsement: Merit")
        if student_info[stu][5] >= 50:
            print("Endorsement: Excellence")
        print("-----")

def get_int()

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
        view_ncea()
        print("-----")
    elif choice == "3":
        print("-----")
        view_endorsements()
        print()
    elif choice == "4":
        year = input("From what year do you want to see?: ")
        print(f"Year {year}")
        for stu in student_info:
            if student_info[stu][2] == year:
                pass
    elif choice == "5":
        while True:
            print("-----")
            identification = input("From what ID do you want to add to: ")

            level = input("What level: ").lower()
            cred = int(input("How many credits?: "))
            
            if level == "achieved":
                student_info[identification][3] += cred
            elif level == "merit":
                student_info[identification][4] += cred
            elif level == "excellence":
                student_info[identification][5] += cred
            else:
                print("Try again")
                continue
            print("All done!")
            print("-----")
            print()
            break
    elif choice == "7":
        print("---")
        view_summary()
        print("---")
class School_Management_System:
    def __int__(self):
        self.students = {}
        self.next_student_id = 1001     # auto-increment ID

# ___________________ NEW ADMISSION _______________________

def new_admission(self):
    Name = input("Enter your name: ")

    try:
        age = int(input("Enter your age: "))

    except ValueError:
        print("age must be a number")
        return

    if age < 5 or age > 18:
        print("age must be between 5 and 18")
        return

    try:
        student_class = int(input("Enter class (1-12): "))
    except ValueError:
        print("class must be a Number")
        return
    if student_class < 1 or student_class > 12:
        print("student class must be between 1 and 12")
        return
    mobile = input("Enter guardian mobile number: ")

    if not (mobile.isdigit() and len(mobile) == 10):
        print("mobile number must be exactly 10 digits")
        return

    # Assign student ID
    student_id = self.next_student_id
    self.next_student_id += 1

    # Store student record
    self.students[student_id] = {
        "name": Name,
        "age": age,
        "class": student_class,
        "mobile": mobile
    }
    print(F"admission successfully! student Id: {student_id}")

# ---------------- VIEW STUDENT ----------------
def view_student(self):
     try:
         student_Id = int(input("Enter student ID: "))
     except ValueError:
         print("Invalid student ID")
         return
     if student_Id not in self.students:
         print("Student ID not found")
         return
     student = self.students[student_Id]
     print("\n📋 Student Details")
     print(f"Student ID : {student_Id}")
     print(f"Name       : {student['name']}")
     print(f"Age        : {student['age']}")
     print(f"Class      : {student['class']}")
     print(f"Mobile     : {student['mobile']}")
# ---------------- UPDATE STUDENT ----------------
def Update_student(self):
    try:
        student_Id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID")
        return
    if student_Id not in self.students:
        print("Student ID not found")
        return
    print("\n1. Update Mobile Number")
    print("2. Update Class")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_mobile = input("Enter new mobile number: ")
        if not (new_mobile.isdigit() and len(new_mobile) == 10):
            print("Mobile number must be exactly 10 digits")
            return
        self.students[student_Id]["mobile"] = new_mobile
        print("Mobile number updated successfully")
    elif choice == "2":
        try:
           new_class = input("Enter new class (1-12): ")
        except ValueError:
            print("class must be a Number")
            return
        if new_class < 1 or new_class > 12:
            print("class must be between 1 and 12")
            return
        self.students[student_Id]["class"] = new_class
        print("Class updated successfully")
    else:
        print("Invalid choice")

# ---------------- REMOVE STUDENT ----------------
def remove_student(self):
    try:
        student_Id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID")
        return
    if student_Id  in self.students:
        del self.students[student_Id]
        print("Student ID removed successfully")
    else:
        print("Student ID record not found")

# ---------------- MAIN PROGRAM ----------------
school = School_Management_System()

while True:
    print("\n🏫 School Management System")
    print("1. New Admission")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        school.new_admission()
    elif choice == "2":
        school.view_student()
    elif choice == "3":
        school.update_student()
    elif choice == "4":
        school.remove_student()
    elif choice == "5":
        print("Exiting system... Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again.")




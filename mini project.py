students=[]
while True:
    print("""
    1. Add students
    2. view students
    3. search students
    4. exit
    """)
    choice=input("enter option:")
    if choice=="1":
        name =input("name:")
        age=input("age:")
        course=input("course:")

        student={
            "name":name,
            "age":age,
            "course":course
        }

        students.append(student)
        print("student add successfully")
    elif choice=="2":
        for student in students:
            print(student)
    elif choice=="3":
        search=input("enter name:")
        for student in students:
            if student["name"]==search:
                print(student)
    elif choice=="4":
        break
    else:
        print("wrong option")
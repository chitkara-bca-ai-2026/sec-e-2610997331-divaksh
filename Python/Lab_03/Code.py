def box(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def lines(title):
    print("\n" + "-" * 50)
    print(f"{title:^50}")
    print("-" * 50)

box("STUDENT RECORD DISPLAY")

student_name = input("Enter Student Name: ")
age = input("Enter Student Age: ")
marks = input("Enter Student Marks: ")

lines(f"Student details\n\n"
      f"Name: {student_name}\n"
      f"Age: {age}\n"
      f"Marks: {marks}")
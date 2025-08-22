class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks < 50:
            return "F"
        elif 50 <= self.marks <= 59:
            return "C"
        elif 60 <= self.marks <= 74:
            return "B"
        elif 75 <= self.marks <= 89:
            return "A"
        elif 90 <= self.marks <= 100:
            return "A+"
        else:
            return "Invalid Marks"

    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")


# Example usage
if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks (0-100): "))

    student = Student(name, roll_no, marks)
    student.display_details()

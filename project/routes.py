class Student:

    def __init__(self, student_id, name, branch, year):

        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year

    def display_info(self):

        print("-" * 40)
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Branch     :", self.branch)
        print("Year       :", self.year)
        print("-" * 40)

    def __str__(self):

        return f"{self.student_id} - {self.name}"

    def __repr__(self):

        return (
            f"Student(student_id='{self.student_id}', "
            f"name='{self.name}')"
        )
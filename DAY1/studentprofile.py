class StudentProfile:
    def __init__(self,name, student_id, course, email, skills):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.email = email
        self.skills = skills
    def display(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Course:", self.course)
        print("Email:", self.email)
        print("Skills:", self.skills)

student1 = StudentProfile( "Vinodini", "TEC101", "B.Tech ECE", "vinodini@gmail.com", ["Python", "SQL", "HTML"])
student2 = StudentProfile( "Rahul", "TEC102", "B.Tech CSE", "rahul@gmail.com", ["Java", "Python", "SQL"])
student3 = StudentProfile( "Anu", "TEC103", "B.Tech EEE", "anu@gmail.com", ["C", "Python", "MATLAB"])
student1.display()
student2.display()
student3.display()


        
        
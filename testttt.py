class Student:
    def __init__(self, name=None, major=None, id=None):
        self.name = name
        self.major = major
        self.id = id
 
class FullTimeStudent(Student):
    def __init__(self, name=None, major=None, id=None, joined_project=None):
        super().__init__(name, major, id)
        self.joined_project = joined_project
        self.research_profile = None


class PartTimeStudent(Student):
    counter = 0
    def __init__(self, name=None, major=None, id=None, min_hour=None, max_hour=None):
        super().__init__(name, major, id)
        self.min_hour = min_hour
        self.max_hour = max_hour
        PartTimeStudent.counter += 1

    @staticmethod
    def getcount():
        return print (f' There are {PartTimeStudent.counter} part-time students')



class Lecturer:
    def __init__(self, id=None, name=None, rank=None):
        self.id = id
        self.name = name
        self.rank = rank
        self.project_led = None
        self.joined_project = []
        self.research_profile = None

class Project:
    def __init__(self, name=None, budget=None):
        self.name = name
        self.budget = budget
        self.leader = None
        self.members = []


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.lecturers = []
        self.projects = []

    def add_student(self, student):
        self.students.append(student.name)

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer.name)

    def add_project(self, project):
        self.projects.append(project.name)

    def get_students(self):
        return self.students

    def get_lecturers(self):
        return self.lecturers

    def get_projects(self):
        return self.projects

# testing
greenwich = SchoolSystem()

student1 = FullTimeStudent("huy1", "Math", 1, "Project A")
student2 = PartTimeStudent("huy2", "Physics", 2, 10, 20)
greenwich.add_student(student1)
greenwich.add_student(student2)
lecturer1 = Lecturer(1, "Dr. Smith", "Professor")
greenwich.add_lecturer(lecturer1)
project1 = Project("Project A", 10000)
greenwich.add_project(project1)

print(greenwich.get_students()) 
print(greenwich.get_lecturers())  
print(greenwich.get_projects())  



PartTimeStudent.getcount()

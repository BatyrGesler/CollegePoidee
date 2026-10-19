class student:
    def __init__(self, name):
        self.name = name
        self.__ocenki = {}


    def add_grades(self, subject, ocenka):
        if ocenka > 5 or ocenka < 1:
            raise ValueError ("Grades only 1-5")
        if subject not in self.__ocenki:
            self.__ocenki[subject] = []
        self.__ocenki[subject].append(ocenka)

    def average(self, subject = None):
        marks = []
        for subject_marks in self.__ocenki.values():
            marks += subject_marks

        else:
            if subject in self.__ocenki:
                marks = self.__ocenki[subject]
            else:
                marks = []

        if len(marks) == 0:
            return 0
        return sum(marks) / len(marks)

    def grades(self):
        kopia = {}
        for subject in self.__ocenki:
            kopia[subject] = self.__ocenki[subject].copy()
        return kopia

def get(student):
    return student.average()

class group:
    def __init__(self):
        self.students = []


    def add_student(self, student):
        self.students.append(student)

    def top_students(self, n):
        list = sorted(self.students, key=get, reverse=True)
        return list[:n]

    def report(self):
        list = sorted(self.students, key=get, reverse=True)
        print("Name       Avg")
        print("-----------------------------")
        for student in list:
            print(f"{student.name:<10} {student.average():.2f}")



anna = student("Anna")
anna.add_grades("Math", 5)
anna.add_grades("Math", 4)
anna.add_grades("Physics", 5)

boris = student("Boris")
boris.add_grades("Math", 3)
boris.add_grades("Physics", 4)

dana = student("Dana")
dana.add_grades("Math", 5)
dana.add_grades("Physics", 5)

group = group()
group.add_student(anna)
group.add_student(boris)
group.add_student(dana)

print("Anna math", anna.average("Math"))
print("Anna physics", anna.average("physics"))
print("Boris physics", boris.average("Math"))
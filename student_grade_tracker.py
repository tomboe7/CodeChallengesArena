class GradeTracker:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print("Grade added: ", grade)

    def calculate_average_grade(self):
        if self.grades:
            average_grade = sum(self.grades) / len(self.grades)
            print("Average grade:", average_grade)
        else:
            print("No grades available.")

# Usage example
grade_tracker = GradeTracker()

grade_tracker.add_grade(85)
grade_tracker.add_grade(92)
grade_tracker.add_grade(78)

grade_tracker.calculate_average_grade()

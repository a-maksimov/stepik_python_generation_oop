from dataclasses import dataclass


class Student:
    def __init__(self):
        self._tests_taken = {}

    @property
    def tests_taken(self):
        if not self._tests_taken:
            return 'No tests taken'
        return self._tests_taken

    def take_test(self, test_paper, answers):
        result = sum(
            [answer == correct_answer for answer, correct_answer in zip(answers, test_paper.answers)]
        ) / len(test_paper.answers)
        passed = result >= test_paper.requirement
        passed_string = 'Passed!' if passed else 'Failed!'
        result = round(result * 100, 0)
        self._tests_taken.update({test_paper.subject: f'{passed_string} ({int(result)}%)'})


@dataclass
class Testpaper:
    subject: str
    answers: list
    requirement: str

    def __post_init__(self):
        self.requirement = float(self.requirement.strip('%')) / 100


# TEST_3:
papers = [
    Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
    Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
    Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
    Testpaper(
        'Informatics',
        ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
         '18B', '19D', '20D'],
        '90%'
    )
]

student1 = Student()
student2 = Student()

student1.choices = [
    ['1C', '2B', '3D', '4C', '5B'],
    ['1A', '2D', '3A', '4D'],
    ['1B', '2D', '3D', '4C', '5B', '6C', '7C'],
    ['1B', '2A', '3C', '4C', '5A', '6B', '7C', '8B', '9D', '10C', '11A', '12D', '13C', '14A', '15B', '16A', '17C',
     '18B', '19C', '20B']
]

student2.choices = [
    ['1A', '2A', '3A', '4A', '5C'],
    ['1A', '2C', '3C', '4A'],
    ['1A', '2B', '3C', '4A', '5D', '6D', '7D'],
    ['1B', '2A', '3C', '4C', '5A', '6D', '7C', '8D', '9A', '10B', '11D', '12A', '13B', '14B', '15C', '16D', '17A',
     '18A', '19D', '20C']
]

for student in [student1, student2]:
    for i in range(4):
        student.take_test(papers[i], student.choices[i])
print(student1.tests_taken)
print(student2.tests_taken)


# TEST_3:
# {'Maths': 'Failed! (20%)', 'Chemistry': 'Failed! (0%)', 'Computing': 'Failed! (14%)', 'Informatics': 'Failed! (30%)'}
# {'Maths': 'Failed! (40%)', 'Chemistry': 'Failed! (50%)', 'Computing': 'Failed! (29%)', 'Informatics': 'Failed! (30%)'}

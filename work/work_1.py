import csv
import sys
import logging

logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
"""  добавлен модуль logging для логирования ошибок и полезной информации. 
            Логи записываются в файл student.log с указанием времени,
            уровня ошибки и сообщения. Уровень ошибки установлен на logging.ERROR, 
            чтобы записывать только ошибки.
"""


class Student:
    """
    Класс, представляющий студента.
    ... (другие атрибуты и методы) ...
    """

    def __init__(self, name=None, subjects_file=None):
        self.name = name
        self.subjects = {}
        if subjects_file:
            try:
                self.load_subjects(subjects_file)
            except Exception as e:
                logging.error(f"Ошибка при загрузке предметов из файла: {str(e)}")

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                logging.error("ФИО должно состоять только из букв и начинаться с заглавной буквы")
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            logging.error(f"Предмет {name} не найден")
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            logging.error("Оценка должна быть целым числом от 2 до 5")
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            logging.error("Результат теста должен быть целым числом от 0 до 100")
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            logging.error(f"Предмет {subject} не найден")
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)

'''  блок кода, который проверяет переданные аргументы командной строки и 
создаёт экземпляр класса Student с заданным именем и файлом предметов. 
Если передача параметров неверна, выводится сообщение об использовании.
'''

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python student.py <name> <subjects_file>")
        sys.exit(1)

    name = sys.argv[1]
    subjects_file = sys.argv[2]

    student = Student(name, subjects_file)
    print(student)

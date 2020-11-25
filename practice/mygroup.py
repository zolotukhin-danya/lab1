groupmates = [
 {
 "name": "Темирлан",
 "surname": "Дзариев",
 "exams": ["Информатика", "ОБД", "Web"],
 "marks": [4, 3, 4]
 },
 {
 "name": "Кирилл",
 "surname": "Сорокин",
 "exams": ["История", "ОАП", "Философия"],
 "marks": [4, 5, 5]
 },
 {
 "name": "Елизавета",
 "surname": "Вязовова",
 "exams": ["Философия", "ИС", "ОАП"],
 "marks": [5, 4, 4]
 },
 {
 "name": "Дарья",
 "surname": "Вязовова",
 "exams": ["ОБД", "ОАП", "Обществознание"],
 "marks": [5, 5, 4]
 },
 {
 "name": "Анастасия",
 "surname": "Алпатова",
 "exams": ["Обществознание", "Web", "ИС"],
 "marks": [5, 5, 5]
 },
 {
 "name": "Данила",
 "surname": "Золотухин",
 "exams": ["ОАП", "ИС", "ОБД"],
 "marks": [5, 4, 5]
 },
 {
 "name": "Светлана",
 "surname": "Захарова",
 "exams": ["Информатика", "Философия", "История"],
 "marks": [5, 5, 5]
 }
]
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10),
u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
student["surname"].ljust(10), str(student["exams"]).ljust(30),
str(student["marks"]).ljust(20))
print_students(groupmates)

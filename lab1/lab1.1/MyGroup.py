#Работу выполнил студент группы УБСТ2301 Анисимов Олег
#Лабораторная работа №1 - Задание 1

#Список одногруппников
groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Олег",
        "surname": "Анисимов",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [4, 3, 2]
    },
    {
        "name": "Наталья",
        "surname": "Радомановна",
        "exams": ["История", "Социология", "Право"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Максим",
        "surname": "Карташев",
        "exams": ["Английский", "Русский", "Немецкий"],
        "marks": [5, 3, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Рудкова",
        "exams": ["Философия", "История", "Экономика"],
        "marks": [4, 5, 4]
    }
]

#Функция вывода спсика студентов
def print_students(students):
    print(u"Имя:".ljust(15), u"Фамилия:".ljust(15), u"Экзамены:".ljust(45), u"Оценки:".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(15),
              str(student["exams"]).ljust(45),
              str(student["marks"]).ljust(20))

#Функция фильтрации студентов, у которых средний балл больше либо равен введенному значению
def filter_students_by_avg(students, min_avg):
    return [s for s in students if sum(s["marks"]) / len(s["marks"]) >= min_avg]

#Cтандартная конструкция в Python
if __name__ == "__main__":
    #Вывод списка студентов
    print("Список студентов:")
    print_students(groupmates)

    while True:  # бесконечный цикл
        try:
            #Ввод значения пользователя
            threshold = float(input("\nВведите средний балл для фильтрации: "))
            # проверка на отрицательные числа
            if threshold < 0:
                print("Ошибка: средний балл не может быть отрицательным!")
                continue  # возвращаемся к запросу ввода заново
            #Вызов функции фильтрации
            filtered = filter_students_by_avg(groupmates, threshold)
            #Вывод результов
            print(f"\nСтуденты со средним баллом больше и равного {threshold}:")
            if filtered:
                print_students(filtered)
            else:
                print("Нет студентов, удовлетворяющих условию.")
        except ValueError:
            print("Ошибка: введите число.")

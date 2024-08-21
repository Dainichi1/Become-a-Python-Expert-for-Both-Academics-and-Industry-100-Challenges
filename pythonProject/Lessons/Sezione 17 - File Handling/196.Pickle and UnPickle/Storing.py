


import pickle, Student

# Creazione di 3 oggetti Student
students = [
    Student.Student("Alice", 20, "A"),
    Student.Student("Bob", 22, "B"),
    Student.Student("Charlie", 21, "C")
]

# Apertura del file in modalità binaria per scrittura
with open('students.data', 'wb') as file:
    for student in students:
        pickle.dump(student, file)  # Pickle: Salva l'oggetto nel file

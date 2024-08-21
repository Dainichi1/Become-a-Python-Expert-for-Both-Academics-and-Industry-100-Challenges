
import pickle,Student

# Apertura del file in modalità binaria per lettura
with open('students.data', 'rb') as file:
    while True:
        try:
            student = pickle.load(file)  # Unpickle: Carica l'oggetto dal file
            student.display()
        except EOFError:
            break  # Termina quando raggiunge la fine del file



# (.venv) PS E:\PYTHON-LEZIONI\pythonProject\Lessons\Sezione 17 - File Handling\196.Pickle and UnPickle> python Reading.py
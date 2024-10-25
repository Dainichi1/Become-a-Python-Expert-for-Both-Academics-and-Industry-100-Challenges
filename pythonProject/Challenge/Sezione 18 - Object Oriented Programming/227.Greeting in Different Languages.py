class English:
    def greetings(self):
        print('Hello')

class French:
    def greetings(self):
        print('Bonjour')

def greet(language):
    language.greetings()

e = English()
f = French()

greet(e)
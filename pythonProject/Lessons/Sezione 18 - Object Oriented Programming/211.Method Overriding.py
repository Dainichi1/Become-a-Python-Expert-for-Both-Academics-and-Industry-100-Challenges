# Definizione della classe base (genitore)
class Iphone6:
    # Metodo 'home' della classe Iphone6
    def home(self):
        print("Home button present on iPhone 6")

# Definizione della classe derivata (figlio) che eredita da Iphone6
class IphoneX(Iphone6):
    # Metodo 'home' della classe IphoneX, che sovrascrive il metodo 'home' della classe genitore
    def home(self):
        # Uso di 'super()' per richiamare il metodo 'home' della classe genitore
        super().home()  # Questo è opzionale e viene utilizzato solo se si vuole chiamare anche il metodo del genitore
        print("No physical Home button on iPhone X")

# Creazione di un'istanza della classe Iphone6 e chiamata del metodo 'home'
iphone6 = Iphone6()
iphone6.home()  # Output: Home button present on iPhone 6

# Creazione di un'istanza della classe IphoneX e chiamata del metodo 'home'
iphonex = IphoneX()
iphonex.home()
# Output:
# Home button present on iPhone 6 (se usiamo super() per chiamare il metodo del genitore)
# No physical Home button on iPhone X

import re
from collections import Counter

# Testo di input
text = ('Python is an easy programmers language. '
        'Python syntax is like the English language. '
        'Python language is easy to learn and adapt compared to Java and C. '
        'In Python language, the same task can be performed using fewer lines of code. Its easy learning and easy to code.')

# Trova tutte le parole nel testo (considera solo parole alfabetiche)
word = re.findall(r'\b\w+\b', text)
'''
Il pattern r'\b\w+\b':

Il prefisso r indica una stringa raw (grezza), che tratta i backslash \ come caratteri normali, evitando di doverli doppiare (es. \\).
\b: Specifica un confine di parola (word boundary). Un confine di parola è la posizione tra un carattere alfanumerico (a-z, A-Z, 0-9, _) e un carattere non alfanumerico (come uno spazio, punteggiatura, ecc.).
\w+: Cerca una sequenza di uno o più caratteri alfanumerici o underscore (_).
\w corrisponde a [a-zA-Z0-9_].
Il segno + indica "uno o più" caratteri consecutivi.
\b: Il secondo confine di parola chiude la parola.
'''


# Conta le occorrenze delle parole
count = Counter(word)

# Stampa le 3 parole più comuni
print("Le 3 parole più comuni sono:", count.most_common(3))




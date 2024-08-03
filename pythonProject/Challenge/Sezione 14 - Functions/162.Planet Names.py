def planet (id) :

    pianeti = {
        1: "Mercurio",
        2: "Venere",
        3: "Terra",
        4: "Marte",
        5: "Giove",
        6: "Saturno",
        7: "Urano",
        8: "Nettuno",
        9: "Plutone"  # Considerato un pianeta nano
    }

    for i in pianeti:
        if i == id:
            return pianeti[i]

id = int (input('Enter the Planet id: ' ))
v = planet(id)
print(v)





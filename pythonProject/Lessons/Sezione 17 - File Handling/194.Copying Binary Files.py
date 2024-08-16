file = open('Python1.jpeg','rb') # 'rb' = leggo in modalità binaria. aggiungo la 'b' perchè sto leggendo una immagine
data = file.read()

copy_file = open('Python2.jpeg','wb')
copy_file.write(data)

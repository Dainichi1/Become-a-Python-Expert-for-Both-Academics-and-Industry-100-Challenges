from zipfile import *

f = ZipFile ('images.zip', 'w', ZIP_DEFLATED)

f.write('731_java.jpg')
f.write('C++_logo.png')
f.write('javascript.jpg')
f.write('Logo_C_sharp.svg.png')
f.write('png-transparent-python-logo-thumbnail.png')

f.close()


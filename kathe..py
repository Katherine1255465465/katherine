## usando for
## rangos, listas, cadenas de texto

for x in range (1,11) :
    print (x)

    
for e in [1,2,3,4,5]:
    print (e)


for z in "hola mundo":
    print (z)
for y in ["lunes","martes", "miercoles", "jueves", "viernes"]:
    print ("hoy es: ",y)

control = 0

while control < 1:
 print (" ")
print (" bienbenido")
print (" ")
print ("1. numeros de 0 a 10")
print ("2. numeros romanos")
print ("3. dias de la semana")
print ("4. numeros primos")
print ("5. salir")
print (" ")
options =int (input ("ingresa opcion:" ))

if options == 1:
    for x in range (0,11):
        print (x)

if options == 2:
    for x in ["I","II","III","IV","V"]:
        print (X)
        
if options ==3:
    for x in ["lunes","martes","miercoles","jueves","viernes"]:
        print (x)

if options == 4:
    for x in [1,3,7]:
        print (x)

if options == 5:
    control = 2

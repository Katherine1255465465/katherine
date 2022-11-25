class menu:
    def __init__(self):
        self.nombre = input("registra tu nombre")
        self.apellidos = input("registra tus apellidos")
        self.edad = input("registra tu edad")
        self.grado = input("registra tu grado")
        self.seccion = input("registra tu seccion")
        self.ID = input("registra tu ID")
        self.direccion = input("registra tu direccion")
        sel.telefono = input ("registra tu telefono")
class personal (menu):
    def nombres (self):
        print (f"nombres:", self.nombres)
    def apellidos (self):
        print (f"apellidos:", self.apellidos)
    def edad (self):
        print (f"edad:", self.edad)
class educacion (menu):
    def grado (self):
        print (f"grado:", self.grado)
    def seccion (self):
        print (f"seccion:", self.seccion)
    def ID (self):
        print (f"ID:", self.ID)
class contacto (menu):
    def direccion (self):
        print (f"direccion:", self.direccion)
    def telfono (self):
        print (f"telefono:", self.telefono)




x = menu()
y = 0
while y < 5:
    print ("bienvenido al menu")
    print ("")
    print ("1. datos personales")
    print ("2. datos escolares")
    print ("3. datos de contacto")
    print ("4. salir")
    print ("")
    op = input ("que desea registrar?")

    x = menu()
    if op == 1:
        h = personal()
        x.nombres()
        x.apellidos()
        x.edad()
        print("")
    if op == 2:
        s = educacion()
        x.grado()
        x.seccion()
        x.ID()
    if op == 3:
        d = contacto()
        x.dirreccion()
        x.telefonos()
    if op == 4:
        print ("estas saliendio del sistema, vuelve pronto")
        y = 10


x = menu()
h = personal()
s = educacion() 
d = contacto()
        

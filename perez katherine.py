from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("Menu Ejemplo")

menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo",menu=file)
file.add_command(label="Nuevo Archivo")
file.add_command(label="Abrir")
file.add_command(label="Guardar")

edit = Menu(menubar,tearoff=0)
menu.add_cascade(label="Modificar",menu=edit)
edit.add_command(label="Cortar")
edit.add_command(label="Copiar")
edit.add_command(label="Pegar")
edit.add_command(label="Seleccionar todo")

help_=Menu(Menubar,tearoff=0)
menubar.add_cascade(label="Ayuda",menu=help_)
help_.add_command(label="Preguntas frecuentes")
help_.add-command(label="Acerca de...")

root.config(Menu=menubar)

root.mainloop()


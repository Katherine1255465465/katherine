from tkinter impoprt Tk, Frame, Ganvas, Button, IntVar, Att.

import random
from pygame import mixer

x,y = 15.15
direction = "
posicion_x = 15
posicion_y = 15
posicion_food = (15,15)
posicion_snake = [(75,75)]
nueva_posicion = [(15,15)]

mixer.init()

def coodenadas_snake



    global direccion, posicion_snake,x,y,nueva_posicion

    if direccion =="up":# arriba
        y = y-30
        nueva posicion[0:] = [(x,y)]
        if y >=495:
           y=15
        elif y <=0:
           y=465


    elif direccion=="down": #abajo
        y = y+30
        nueva posicion[0:] = [(x,y)]
        if y >=495:
           y =15
        elif y <=0:
           y=15.



           

       elif direccion == "left": # izquierda
           x = x-30
           nueva posicion[0:] = [(x,y)]
           if x >=495:
               x = 0
           elif x <=0:
               x=465

               
        

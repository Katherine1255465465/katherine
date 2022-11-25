try:
    print (x)
except:
    print("a corrido un error")




try:
 print(x)
except NameError:
     print("la variable no se ha declarado")
except:
     print ("algo anda mal")






     x = -1
     if x <0:
        raise Exception ("perdon, el numero es menor a 0")





x = "hello"
    
if not type(x)is int:
        raise TypeError ("only integers are allowed")







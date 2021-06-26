#  *** Menú  ***
#Area del triángulo
#Area del cuadrado
#Area del círculo
#Que edad tengo
#Salir



def menu():
    print("     ***  MENU  ***    ")
    print("1. Area del triángulo")
    print("2. Area del cuadrado")
    print("3. Area del círculo")
    print("4. Que edad tengo")
    print("5. Salir")
    op = input ("Escriba la opcion:")
    op = int(op)
    if op==1: Area_del_triangulo()
    elif op==2: Area_del_cuadrado()
    elif op==3: Area_del_círculo()
    elif op==4: Que_edad_tengo()
    else: exit()

def Area_del_triangulo():
    print("")
    base=input("Ingrese Base: ")
    altura=input("Ingrese altura: ")
    area=int (base) * int (altura) / 2.0
    print ("el resultado es: " + str (area))
    print("")
    menu()
    
def Area_del_cuadrado():
    print("")
    a=float(input("ingrese el lado del cuadrado:\n"))
    area=a*a
    print(str(area))
    print("")
    menu()

def Area_del_círculo():
    print("")
    import math
    print("Ingrese el radio del circulo:")
    r = float (input())
    a= math.pi * (r*r)
    print("El area del circulo con radio ",r," Es: ",a)
    print("")
    menu()

def Que_edad_tengo():
    print("")
    nacimiento = int(input("Ingrese año de nacimiento:"))
    actual = int(input("Ingrese año actual: "))
    edad = actual - nacimiento
    print ("Mi edad es:",edad, "años")
    print("")
    menu()
menu()

from types import TracebackType 
import numpy as np
import re
import click

def entrada_funcion():
    badnum=True
    while(badnum==True):
        try:
            grado = int(input("Grado de la funcion:"))
            badnum = False
        except ValueError:
            print("el grado de f(x) debe ser un numero!")
            badnum=True
                   
    print("Introduce los terminos de la funcion para saltarse terminos pulsar ENTER o CERO")
    funcion_entrada = []
    

    for i in range(grado+1):
        print(i)
        if(i<grado):
            equis = float (input(f"introduce X^{grado-i}*"))
            funcion_entrada.append(equis)
        else:
            equis = float (input(f"termino independiente:"))
            funcion_entrada.append(equis)

    print(funcion_entrada)
  
    return funcion_entrada


# Defining Function
def f(x):
    return x**6 + x**2 + 0

# Defining derivative of function

def newtonRaphson(x0,epsilon,iteraciones,fcoefs):
 repetir = True
 while repetir == True: 
    repetir = False

    fx = np.poly1d(fcoefs)
    dx = np.polyder(fx)

    print("\n------ DATOS---------")
    print(f"f(x)")
    print(fx)
    print(f"d(x)")
    print(dx)
    print(f"Tolerancia/Epsion: {epsilon}")
    print('\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    pasadas = 1
    nosalto = True
    condition = True
    while condition:
        if dx(x0) == 0.0:
            print(' ERROR no se puede dividir entre 0 !!')
            break

        # Calcular siguiente punto
        x1 = x0 - fx(x0)/dx(x0)
        print('Prueba-%d, x = %0.5f --> f(x) = %0.5f' % (pasadas, x1, fx(x1)))
        x0 = x1
        pasadas = pasadas + 1

        if pasadas > iteraciones:
            nosalto = False
            break
        
        condition = abs(fx(x1)) > epsilon
    
    if nosalto==True:
        print('\nRaiz : %0.8f' % x1)
    else:
        print('\nNo converge')
    
    if click.confirm('Buscar otra raiz?'): 
         x0 = click.prompt('Introduce semilla', type=float)
         repetir = True
         click.echo('Well done!')
    else:
        opcion = click.prompt('''\n ¿ Que deseas hacer ?
        1-Modificar iteraciones maximas 
        2-Modificar precision
        3-Cambiar de Funcion
        4-Salir ! 
        ''' ,type=click.IntRange(1,4))

        if(opcion ==1):
            repetir = True
            iteraciones= click.prompt('Iteraciones maximas', type=click.IntRange(min=1))
        if(opcion ==2):
            repetir = True
            epsilon= click.prompt('Introduce precison', type=float)
        if(opcion ==3):
            repetir = True
            fcoefs = entrada_funcion()
        if(opcion==4):
            print("Adios!")
            repetir = False


def entrada_opciones():
  
    iteraciones= click.prompt('Iteraciones maximas', type=click.IntRange(min=1))
    epsilon= click.prompt('Introduce precison', type=float)
    x0 = click.prompt('Introduce semilla', type=float)
    
    # Casteando a valores para funcion newton 
    x0 = float(x0)
    epsilon = float(epsilon)
    iteraciones = int(iteraciones)
    return x0,epsilon,iteraciones

def menu():

    print("Bienvenido al programa:")
    funcion_entrada = entrada_funcion()
    x0,epsilon,iteraciones = entrada_opciones()
    newtonRaphson(x0,epsilon,iteraciones,funcion_entrada)
    

menu()
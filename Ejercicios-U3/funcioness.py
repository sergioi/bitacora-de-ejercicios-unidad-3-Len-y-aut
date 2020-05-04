#-*- coding: utf-8 -*-

#Funcion matimaticas

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def divicion(a,b):
    try:
        return float(a/b)
    except:
        print('El resultado produce un error de division cero')

def elevacion(a,b):
   return a**b
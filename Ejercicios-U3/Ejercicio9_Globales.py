
#creación datos para optimizar procesos de operaciones matemáticas
import funcioness

a = int (input("ingrese un numero: "))
b = int (input("ingrese un numero: "))

print ("La suma es: ", funcioness.suma(a,b))
print ("La resta es: ", funcioness.resta(a,b))
print ("La multiplicacion es: ", funcioness.multiplicar(a,b))
print ("La divicion es: ", funcioness.divicion(a,b))
print ("elevacion : ", funcioness.elevacion(a,b))


#--------------------------------------------------------------

#CODIGO SIN OPTIMIZACION

# def suma(a,b):
#    return a+b
#
#def resta(a,b):
#    return a-b
#
#def multiplicar(a,b):
#    return a*b
#
#def divicion(a,b):
#    try:
#        return float(a/b)
#    except:
#        print('El resultado produce un error de division cero')
# 
# a = int (input("ingrese un numero: "))
#b = int (input("ingrese un numero: "))
#
#print ("La suma es: ", aritmetica.suma(a,b))
#print ("La resta es: ", aritmetica.resta(a,b))
#print ("La multiplicacion es: ", aritmetica.multiplicar(a,b))
#print ("La divicion es: ", aritmetica.divicion(a,b))
# 
# 

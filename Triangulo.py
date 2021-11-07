
x = int  (input("Ingrese lado 1  del triangulo (numero entero)"))
y = int  (input("Ingrese lado 2 del triangulo (numero entero)"))
z = int  (input("Ingrese lado 3 del triangulo (numero entero)"))

if ( x == y and y == z):
    print('Equilatero')
elif ( x != y and y != z and x !=z ):
    print('Escaleno ')
else :
        print('Isosceles')

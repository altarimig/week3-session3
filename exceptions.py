"""# Syntax exceptions
try:
    numero = input("Ingresa un número")
    numero / 3
except Exception as ex:
    print("Ocurrió una excepción: " + str(ex))
finally:
    print("Se terminó de ejecutar")"""

"""while True:
    try:
        x = int(input("Por favor ingrese un número: "))
        print("El número ingresado es: " + str(x))
        break
    except ValueError:
        print("Debes ingresar un número. Intente nuevamente...")"""

##### RETO #####
while True:
    try:
        x = int(input("Ingrese un número cualquiera: "))
        print(f"El resultado de la división del número ingresado es: {x / 2}")
        break
    except ValueError:
        print("Debes ingresar un número, si deseas que te muestre la división por dos. Inténtalo nuevamente")

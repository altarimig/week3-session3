# Syntax exceptions
try:
    numero = input("Ingresa un número")
    numero / 3
except Exception as ex:
    print("Ocurrió una excepción: " + str(ex))
finally:
    print("Se terminó de ejecutar")
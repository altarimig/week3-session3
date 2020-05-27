"""palabras = ["gato", "perro", "ventana", "defenestrado"]
for val in palabras:
    if val == "ventana":
        break
    print(val)
print("Final!!!")"""

##### RETO #####

lista = [1, 3, 20, 10, 50, 100, 31, 1000]
for val in lista:
    if val == 3:
        print(val)
    if val % 2 == 0:
        print(f"El valor {val} es par")
    if val == 50:
        break
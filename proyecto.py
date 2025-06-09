import random
import time
random.seed(42)


# Lista para analizar en caso de una lista ordenada
lista1 = []
for i in range (1, 101):
    lista1.append(int(i))

# Lista para analizar en caso de una lista desordenada
lista2 = []
for i in range (1, 101):
    aleatorio = random.randint(0, 100)
    lista2.append(aleatorio)

# Busqueda lineal
def buscar_var_lineal(lista, numero):
    flag = False # Se define una bandera para indicar cuando el ciclo debe cortar sin la necesidad de un break
    ct = 0 # Variable con la que el programa va a iterar la lista
    while flag == False:
        try:
            if lista[ct] == numero:
                # Se encontro el numero!
                fin = (time.time()) * 1000
                return fin
            else:
                ct += 1
        except IndexError:
            # El numero no esta en la lista!
            fin = (time.time()) * 1000
            return fin


# Busqueda binaria
def buscar_var_bin(lista, numero):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        mitad = lista[medio]

        if mitad == numero:
            # Se encontro el numero!
            fin = (time.time()) * 1000
            return fin
        elif mitad < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    # El numero no esta en la lista!
    fin = (time.time()) * 1000
    return fin


# Se define el valor que se intenta buscar
num = int(input("Ingrese el numero que desea buscar: "))
variables_scan = [num]
producto = num
for i in range(0, 5):
    producto = producto + 10
    variables_scan.append(producto)
print(f"variables a escanear: {variables_scan}")

resultados = []
for i in range(len(variables_scan)):
    # ANALISIS EMPIRICO DE CADA METODO CON CADA TIPO DE LISTA
    # --------------- BUSQUEDA LINEAL ---------------

    # Lista ordenada
    valor_inicio1 = (time.time()) * 1000
    valor_final1 = buscar_var_lineal(lista1, variables_scan[i])
    tiempo_de_ejecucion_li_ord = valor_final1 - valor_inicio1
    resultados.append({
        "numero_buscado": variables_scan[i],
        "metodo": "lineal",
        "orden": "ordenada",
        "tiempo": tiempo_de_ejecucion_li_ord
    })
    
    
    

    # Lista desordenada
    valor_inicio2 = (time.time()) * 1000
    valor_final2 = buscar_var_lineal(lista2, variables_scan[i])
    tiempo_de_ejecucion_li_des = valor_final2 - valor_inicio2
    resultados.append({
        "numero_buscado": variables_scan[i],
        "metodo": "lineal",
        "orden": "desordenada",
        "tiempo": tiempo_de_ejecucion_li_des
    })



    # --------------- BUSQUEDA BINARIA ---------------

    # Lista ordenada
    valor_inicio3 = (time.time()) * 1000
    valor_final3 = buscar_var_bin(lista1, variables_scan[i])
    tiempo_de_ejecucion_bin_ord = valor_final3 - valor_inicio3
    resultados.append({
        "numero_buscado": variables_scan[i],
        "metodo": "binaria",
        "orden": "ordenada",
        "tiempo": tiempo_de_ejecucion_bin_ord
    })

    # Lista desordenada
    valor_inicio4 = (time.time()) * 1000
    lista_ordenada = sorted(lista2)
    valor_final4 = buscar_var_bin(lista_ordenada, variables_scan[i])
    tiempo_de_ejecucion_bin_des = valor_final4 - valor_inicio4
    resultados.append({
        "numero_buscado": variables_scan[i],
        "metodo": "binaria",
        "orden": "desordenada",
        "tiempo": tiempo_de_ejecucion_bin_des
    })

# Inicializamos las listas vacías
lineal_ordenada = []
lineal_desordenada = []
binaria_ordenada = []
binaria_desordenada = []

# Clasificamos los resultados en una sola pasada
for r in resultados:
    if r["metodo"] == "lineal" and r["orden"] == "ordenada":
        lineal_ordenada.append(r)
    elif r["metodo"] == "lineal" and r["orden"] == "desordenada":
        lineal_desordenada.append(r)
    elif r["metodo"] == "binaria" and r["orden"] == "ordenada":
        binaria_ordenada.append(r)
    elif r["metodo"] == "binaria" and r["orden"] == "desordenada":
        binaria_desordenada.append(r)

print("- "*10, "BUSQUEDA LINEAL EN LISTA ORDENADA", "- " * 10)
for i in lineal_ordenada:
    print(i)

print("- " * 10, "BUSQUEDA LINEAL EN LISTA DESORDENADA", "- " * 10)
for i in lineal_desordenada:
    print(i)

print("- "*10, "BUSQUEDA BINARIA EN LISTA ORDENADA", "- "*10)
for i in binaria_ordenada:
    print(i)

print("- "*10, "BUSQUEDA BINARIA EN LISTA DESORDENADA", "- "*10)
for i in binaria_desordenada:
    print(i)
        
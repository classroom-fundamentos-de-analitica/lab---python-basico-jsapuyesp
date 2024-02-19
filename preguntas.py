"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
#Lectura y limpieza de datos
with open("./data.csv", "r") as file:
    datos = file.readlines()

datoscsv = [line.replace("\n", "") for line in datos]

datosFin = [line.split("\t") for line in datoscsv]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    for dato in datosFin:
        suma += int(dato[1])
    return suma


def pregunta_02():
    """
        Retorne la cantidad de registros por cada letra de la primera columna como la lista
        de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista1 = []
    lista2 = []
    for dato in datosFin:
        letra = dato[0]
        if letra in lista1:
            value = lista1.index(letra)
            lista2[value] += 1
        else: 
            lista1.append(letra)
            lista2.append(1)
    
    lista = list(zip(lista1, lista2))

    return sorted(lista, key = lambda x: x[0])



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista1 = []
    lista2 = []
    for dato in datosFin:
        letra = dato[0]
        if letra in lista1:
            value = lista1.index(letra)
            lista2[value] += int(dato[1])
        else:
            lista1.append(letra)
            lista2.append(int(dato[1]))
    
    lista = list(zip(lista1,lista2))

    return sorted(lista, key= lambda x: x[0])


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    lista1 = []
    lista2= []
    for dato in datosFin:
        fecha = dato[2].split('-')
        mes = fecha[1]
        if mes in lista1:
            val = lista1.index(mes)
            lista2[val] += 1
        else:
            lista1.append(mes)
            lista2.append(1)
    lista = list(zip(lista1, lista2))
    return sorted(lista, key=lambda x: x[0])


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    lista1 = []
    lista2 = []
    listaMax = []
    listaMin = []

    for dato in datosFin:
        letra = dato[0]
        if letra in lista1:
            val = lista1.index(letra)
            lista2[val].append(int(dato[1]))
        else:
            lista1.append(letra)
            lista2.append([int(dato[1])])
    for ele in lista2:
        listaMax.append(max(ele))
        listaMin.append(min(ele))

    lista = list(zip(lista1, listaMax, listaMin))
    return sorted(lista, key=lambda x: x[0])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista1 = []
    lista2 = []
    listaMax = []
    listaMin = []

    for dato in datosFin:
        res = []
        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)
        for k in res.keys():
            letra = k
            if letra in lista1:
                val = lista1.index(letra)
                lista2[val].append(int(res[k]))
            else:
                lista1.append(letra)
                lista2.append([int(res[k])])

    for ele in lista2:
        listaMax.append(max(ele))
        listaMin.append(min(ele))

    lista = list(zip(lista1, listaMin, listaMax))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista1 = []
    lista2 = []
    for dato in datosFin:
        num = int(dato[1])
        if num in lista1:
            val = lista1.index(num)
            lista2[val].append(dato[0])
        else:
            lista1.append(num)
            lista2.append([dato[0]])

    lista = list(zip(lista1, lista2))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista1 = []
    lista2 = []
    for dato in datosFin:
        num = int(dato[1])
        if num in lista1:
            val = lista1.index(num)
            if not dato[0] in lista2[val]:
                lista2[val].append(dato[0])
        else:
            lista1.append(num)
            lista2.append([dato[0]])

    for l in lista2:
        l = l.sort()

    lista = list(zip(lista1, lista2))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista1 = []
    lista2 = []
    lista3 = []

    for dato in datosFin:
        res = []
        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)
        for k in res.keys():
            letra = k
            if letra in lista1:
                val = lista1.index(letra)
                lista2[val].append(int(res[k]))
            else:
                lista1.append(letra)
                lista2.append([int(res[k])])

    for ele in lista2:
        lista3.append(len(ele))
    lista = dict(zip(lista1, lista3))
    return lista


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista1 = []
    lista2 = []
    lista3 = []

    for dato in datosFin:
        res = []
        lista1.append(dato[0])

        lista = dato[3].split(',')

        lista2.append(len(lista))

        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)

        lista3.append(len(res))

    lista = list(zip(lista1, lista2, lista3))
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dic = {}

    for dato in datosFin:
        valor = int(dato[1])
        for letra in dato[3].split(','):
            if letra in dic:
                dic[letra] += valor
            else:
                dic[letra] = valor
    return dic


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dic = {}

    for dato in datosFin:
        res = []
        letra = dato[0]

        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)
        res = dict([a, int(x)] for a, x in res.items())
        valor = sum(res.values())
        if letra in dic:
            dic[letra] += valor
        else:
            dic[letra] = valor

    return dic

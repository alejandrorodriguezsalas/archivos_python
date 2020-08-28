#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
import re

def contar_lineas(archivo):
    cont = 0
    archivo.seek(0)
    for linea in archivo:
        print(linea,end='')
        cont += 1
    return cont


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    fi = open('texto.txt','r') 
    print('\nCantidad de lineas leídas:',contar_lineas(fi))
    fi.close


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    fi = open('notas.txt', 'r')
    fo = open('copia_nota.txt','w')
    for linea in fi:
        fo.write(linea)
    print('\nLa cantidad de lineas copiadas es: ',contar_lineas(archivo=fi))
    fi.close
    fo.close


    # Recuerde cerrar los archivos al final ;)


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    with open(archivo) as csvfile:
        data = list(csv.DictReader(csvfile))
    
    cont_2_ambi = 0
    cont_3_ambi = 0
    
    for i in range(len(data)):
        if data[i].get('ambientes') == '2':
            cont_2_ambi += 1
        elif data[i].get('ambientes') == '3':
            cont_3_ambi += 1
    
    print('cantidad de propiedades de 2 ambientes: ',cont_2_ambi)
    print('cantidad de propiedades de 3 ambientes: ',cont_3_ambi)
    csvfile.close


def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"
    '''
    print('\nPara salir ingrese FIN en fruta/verdura\n')
    while True:
        verdura = str(input('Ingrese fruta/verdura: '))
        if verdura == 'fin' or verdura == 'FIN':
            break
        cantidad = int(input('Ingrese cantidad: '))
        inventario[verdura] = cantidad
    print(inventario)
    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"


def ej5():
    # Ejercicios con archivos CSV
    # inventario = {'Fruta Verdura': 'manzana', 'Cantidad': 10}

    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    csvfile = open('Verduleria.csv', 'w', newline='')

    header = ['Verduras y Frutas', 'Cantidad']

    writer = csv.DictWriter(csvfile, fieldnames=header)
    
    writer.writeheader()
    
    
    print('Para salir ingrese FIN en fruta/verdura')
    

    while True:
        fruta = str(input('Ingrese fruta/verdura: '))
        if fruta == 'FIN' or fruta == 'fin':
            break
        cantidad = int(input('Ingrese cantidad: '))
        writer.writerow({'Verduras y Frutas': fruta, 'Cantidad': cantidad})
    
    csvfile.close()


if __name__ == '__main__':
    print("\n               Bienvenidos a otra clase de Inove con Python\n")
    print("\n   Ej1: Archivo TXT, contar lineas")
    ej1()
    print("\n\n   Ej2: Archivo TXT, copiar archivo")
    ej2()
    print("\n\n   Ej3: Archivo CSV, busqueda")
    ej3()
    print("\n\n   Ej4: Diccionario, escritura")
    ej4()
    print("\n\n   Ej5: Archivo CSV, escritura con diccionario")
    ej5()
    print('\n********************************* FIN DEL PROGRAMA *********************************')

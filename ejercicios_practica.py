#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
import re

def pasar_HMS_seg(HMS):
    h,m,s = HMS.split(':') 
    return int(h) * 3600 + int(m) * 60 + int(s)


def pasar_seg_HMS(seg):
    h = seg // 3600
    m = (seg%3600) // 60
    s = (seg%3600) % 60
    hsm = str(h) + ':' + str(m) + ':' + str(s)
    return hsm


def estadisticas(archivo,division,diciplina):
    acum = 0
    cont = 0
    max_tiempo = None
    min_tiempo = None
    for i in range(len(archivo)):
        if archivo[i].get('Division') == division:
            if archivo[i].get(diciplina) == '':
                continue
            segundos_totales = (pasar_HMS_seg(HMS=archivo[i].get(diciplina)))
            acum += segundos_totales
            cont += 1
            if max_tiempo == None or max_tiempo < segundos_totales:
                max_tiempo = segundos_totales
            if min_tiempo == None or min_tiempo > segundos_totales:
                min_tiempo = segundos_totales

    min_tiempo = pasar_seg_HMS(seg=min_tiempo)
    max_tiempo = pasar_seg_HMS(seg=max_tiempo)
    prom = pasar_seg_HMS(seg=acum//cont)

    print('''Estadisticas de la division {} en {}:
    Minimo tiempo: {}
    Máximo tiempo: {}
    Tiempo promedio de los competidores: {}
    '''.format(division,diciplina,min_tiempo,max_tiempo,prom))
   

def ej1():
    print("\n   Ej1:Cuenta caracteres\n")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    fi = open('texto.txt','r')
    contenido = fi.read()
    cantidad_letras = len(contenido)
    print('Cantidad de caracteres de "texto.txt: ',cantidad_letras)
    fi.seek(0)
    cantidad_letras = 0
    for line in fi:
        print(line,end='')
        cantidad_letras += len(line)
    print('Cantidad de caracteres de "texto.txt: ',cantidad_letras)
    fi.close()
    

def ej2():
    print("\n   Ej2:Transcribir!\n")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    fi = open('Ej2.txt','w')
    print('Para salir solo ingrese enter')
    while True:
        linea = [str(input('Ingrese linea de texto que desee agragar al archivo\n')),'\n']
        if linea[0] == '':
            break
        cantidad_letras += len(linea[0])
        fi.writelines(linea)
    fi.close()
    print('Cantidad de caracteres escritos: ',cantidad_letras)


def ej3():
    print("\n   Ej3:Escrutinio de los alquileres de Capital Federal\n")
    #cantidad_ambientes = 2

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    print('''Ingrese una cantidad de ambientes para analizar:
    1- Cantidad de alquileres en "pesos" disponible
    2- Promedio de valor de alquileres
    3- Máximo valor de alquiler en pesos
    4- Minimo valor de alquiler en pesos''')
    amb = str(input('¿Que cantidad de ambientes desea analizar?  '))
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    cont = 0
    acum = 0
    max_precio = None
    min_precio = None
    

    for i in range(len(data)):
        if data[i].get('ambientes') == amb and data[i].get('moneda') == 'ARS':
            cont += 1
            precio = float(data[i].get('precio'))
            acum += precio
            if max_precio == None or max_precio < precio:
                max_precio = precio
            if min_precio == None or min_precio > precio:
                min_precio = precio
    
    csvfile.close()

    print('''
    1- Cantidad de alquileres en "pesos" disponible : {}
    2- Promedio de valor de alquileres: {}
    3- Máximo valor de alquiler en pesos: {}
    4- Minimo valor de alquiler en peso: {}'''.format(cont,acum/cont,max_precio,min_precio))

    
def ejercicio_extra():
    print('\n   Ej4:Estadisticas')
    print("Ahora sí! buena suerte :)\n")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
    with open('2019 Ironman World Championship Results.csv',) as csvfile:
        data = list(csv.DictReader(csvfile))
    
    print(''' Veremos las estadisticas de las diciplinas de Swim, Bike y Run en las divisiones:
    - MPRO
    - M45-49
    - M25-29
    - M18-24
    ''')

    estadisticas(archivo=data,division='MPRO',diciplina='Swim')
    estadisticas(archivo=data,division='MPRO',diciplina='Bike')
    estadisticas(archivo=data,division='MPRO',diciplina='Run')

    estadisticas(archivo=data,division='M45-49',diciplina='Swim')
    estadisticas(archivo=data,division='M45-49',diciplina='Bike')
    estadisticas(archivo=data,division='M45-49',diciplina='Run')

    estadisticas(archivo=data,division='M25-29',diciplina='Swim')
    estadisticas(archivo=data,division='M25-29',diciplina='Bike')
    estadisticas(archivo=data,division='M25-29',diciplina='Run')

    estadisticas(archivo=data,division='M18-24',diciplina='Swim')
    estadisticas(archivo=data,division='M18-24',diciplina='Bike')
    estadisticas(archivo=data,division='M18-24',diciplina='Run')

    csvfile.close()


if __name__ == '__main__':
    print("\n\n             Ejercicios de práctica\n")
    ej1()
    ej2()
    ej3()
    ejercicio_extra()
    print('\n********************************* FIN DEL PROGRAMA *********************************')

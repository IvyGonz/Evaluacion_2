# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:54:05 2020

@author: IvyGonz
"""
class tareas:
    def principal ():
        Menu = tareas ()
        opcion = None 
        while (opcion != '0'):
           print ("""¡Vamos hacer la tarea!
       Escoga que quiere hacer primero:
           1- Realizar las tareas pendientes
           2- Repasar
           0- Descansar""")
           if opcion == '1':
                   Menu.asignatura
           elif opcion == '2':
                   Menu.repaso
           else:
               print ("Recuerda terminar la tarea y no dejarlo a ultimo momento <3 ")
               print ("¡Hasta la proxima!")
               pass
            
    def asignatura ():
        Busq = tareas ()
        opcion = None
        while (opcion != '0'):
            print ("""Escoga una asignatura:
                1- Fisica
                2- Matematica
                3- Socio humanistica
                0- Volver""")
            if opcion == '1':
                respuesta = 'si'
                while (respuesta == 'si'):
                    print ("Asignatura: Fisica")
                    print ("F= m x a")
                    print ("")
                    print ("Ingrese la masa: ")
                    masa = int(input())
                    print ("Ingrese la aceleracion: ")
                    aceleracion = input()
                    Fuerza = masa * aceleracion
                    print ("La fuerza es igual a: ", Fuerza)
                    print ()
                    print ("¿Desea volver a realizar otra operacion? Si/No")
                    respuesta = input()
                    if respuesta == 'si':
                        print()
                    else:
                        pass
            elif opcion == '2':
                respuesta = int(input())
                opcion = 'si'
                while (respuesta != 0):
                    print ("Asignatura: Matematicas")
                    print ("Realice operaciones de suma, resta y multiplicación: ")
                    print ("")
                    print ("Ingrese el primer numero: ")
                    n1 = int(input())
                    print ("Ingrese el segundo numero: ")
                    n2 = int(input())
                    print ("""Escoga una operacion:
                           1- suma
                           2- resta
                           3- multiplicacion
                           0- volver""")
                    if respuesta == '1':
                        while (opcion == 'si'):
                            resultado = n1 + n2
                            print ("El resultado de la suma es: ", resultado)
                            print ()
                            print ("¿Desea volver a realizar otra operacion? Si/No")
                            opcion = input()
                            if opcion  == 'si':
                                print()
                            else:
                                pass
                    elif respuesta == '2':
                        while (opcion == 'si'):
                            resultado = n1 - n2
                            print ("El resultado de la resta es: ", resultado)
                            print ()
                            print ("¿Desea volver a realizar otra operacion? Si/No")
                            opcion = input()
                            if opcion == 'si':
                                print()
                            else:
                                pass
                    elif respuesta == '3':
                        while (opcion == 'si'):
                            resultado = n1 * n2 
                            print ("El resultado de la multiplicacion es: ", resultado)
                            print ()
                            print ("¿Desea volver a realizar otra operacion? Si/No")
                            opcion = input()
                            if opcion == 'si':
                                print()
                            else:
                                pass
                    else:
                        pass
            elif opcion == '3':
                opcion = input ()
                while (opcion != 0):
                    print ("Asignatura: Socio humanistica")
                    print ("Investigar cuales son las normas de convivencia.")
                    print ("")
                    print ("""¿Donde desea buscar la información?
                               1- Busqueda por internet
                               2- Biblioteca
                               3- Apuntes del cuaderno
                               0- Volver""")
                    if opcion == '1':
                        Busq.busqueda
                    if opcion == '2':
                        Busq.busqueda
                    if opcion == '3':
                        Busq.busqueda
                    else:
                        pass
            else:
                pass
        
    def busqueda ():
        opcion = input()
        if opcion == '1':
            print ("Buscaste en internet...")
            print ("Las normas de convivencia constituyen el marco legal que canalizan las iniciativas para favorecer la convivencia, el respeto mutuo, la tolerancia y el ejercicio efectivo de derechos y deberes...")
            print ("Hipervinculo: https://www.ecured.cu/Normas_de_convivencia")
            print ("")
        if opcion == '2':
            print ("Libros disponibles acerca del tema: ")
            print ("")
            print ("--Las normas de convivencia-- por Valentina Martinez")
            print ("--El respeto entre estudiantes-- por Enmamuel Caraballo")
            print ("--Como ser sociable y no morir en el intento-- por Ricardo Ferrer")
            print ()
        if opcion == '3':
            print ("No tienes nada anotado en el cuaderno...")
            print ()

    def repaso (self):
        opcion = None 
        while (opcion != '0'):
            print ("Repasa las materias mas importantes: ")
            print ("")
            print ("""Escoga una asignatura:
                1- Fisica
                2- Matematica
                0- Volver""")
            if opcion == '1':
                respuesta = 'si'
                while (respuesta == 'si'):
                    print ("Asignatura: Fisica")
                    print ("F= m x a")
                    print ("")
                    print ("Ingrese la masa: ")
                    masa = int(input())
                    print ("Ingrese la aceleracion: ")
                    aceleracion = input()
                    Fuerza = masa * aceleracion
                    print ("La fuerza es igual a: ", Fuerza)
                    print ()
                    print ("¿Desea volver a realizar otra operacion? Si/No")
                    respuesta = input()
                    if respuesta == 'si':
                        print()
                    else:
                        pass
            elif opcion == '2':
                respuesta = int(input())
                opcion = 'si'
                while (respuesta != 0):
                    print ("Asignatura: Matematicas")
                    print ("Realice operaciones de suma, resta y multiplicación: ")
                    print ("")
                    print ("Ingrese el primer numero: ")
                    n1 = int(input())
                    print ("Ingrese el segundo numero: ")
                    n2 = int(input())
                    print ("""Escoga una operacion:
                           1- suma
                           2- resta
                           3- multiplicacion
                           0- volver""")
                    if respuesta == '1':
                        while (opcion == 'si'):
                            resultado = n1 + n2
                            print ("El resultado de la suma es: ", resultado)
                            print ()
                            print ("¿Desea volver a realizar otra operacion? Si/No")
                            opcion = input()
                            if opcion  == 'si':
                                print()
                            else:
                                pass
                    elif respuesta == '2':
                        while (opcion == 'si'):
                            resultado = n1 - n2
                            print ("El resultado de la resta es: ", resultado)
                            print ()
                            print ("¿Desea volver a realizar otra operacion? Si/No")
                            opcion = input()
                            if opcion == 'si':
                                print()
                            else:
                                pass
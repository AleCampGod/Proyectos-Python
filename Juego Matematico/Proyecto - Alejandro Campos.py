import random

def Menu():
    print(" ")
    print("*********************************")
    print("*             Menu              *")
    print("*********************************")
    print("*1. Jugar                       *")
    print("*2. Reglas                      *")
    print("*3. Salir                       *")
    print("*********************************")

def Menu2():
    print(" ")
    print("*********************************")
    print("*          Menu Jugar           *")
    print("*********************************")
    print("*1. Jugar Nivel 1               *")
    print("*2. Jugar Nivel 2               *")
    print("*3. Jugar Nivel 3               *")
    print("*4. Volver al menu principal    *")
    print("*********************************")

def Nivel1():
    Puntuacion = 0
    Vidas = 3
    while True:
        try:
            print(f"Tus vidas son {Vidas}.")
            print(f"Tu puntuación es {Puntuacion}.")
            if Vidas > 0:
                Random1 = random.randint(1, 10)
                Random2 = random.randint(1, 10)
                OperacionRandom = ["Suma", "Resta"]
                OperacionRandom = random.choice(OperacionRandom)

                if OperacionRandom == "Suma":
                    RespuestaJugador = int(input(f"\nCual es el resultado de sumar {Random1} + {Random2}?: "))
                    RespuestaCorrecta = Random1 + Random2

                elif OperacionRandom == "Resta":
                    RespuestaJugador = int(input(f"\nCual es el resultado de restar {Random1} - {Random2}?: "))
                    RespuestaCorrecta = Random1 - Random2

                if RespuestaJugador == RespuestaCorrecta:
                    Puntuacion += 1
                    print("*********************************")
                    print("*Felicidades respuesta correcta *")
                    print("*+1 punto.                      *")
                    print("*********************************")

                elif RespuestaJugador != RespuestaCorrecta:
                    Vidas -= 1
                    print("*********************************")
                    print("*Lo siento respuesta incorrecta *")
                    print("*-1 vida                        *")
                    print("*********************************")

            elif Vidas == 0:
                print(" ")
                print("************************************")
                print("*            GAME OVER             *")
                print("************************************")
                print("*Te quedaste sin vidas.            *")
                print(f"*Tu puntuación {Puntuacion}                   *")
                print("************************************")
                input("\nPresione ENTER para continuar.")
                break
        except ValueError as e:
            Vidas -= 1
            print("******************************************")
            print("*Error: Debes ingresar un número válido. *")
            print("*-1 vida                                 *")
            print("******************************************")

def Nivel2():
    Puntuacion = 0
    Vidas = 3
    while True:
        try:
            print(f"Tus vidas son {Vidas}.")
            print(f"Tu puntuación es {Puntuacion}.")
            if Vidas > 0:
                Random1 = random.randint(1, 50)
                Random2 = random.randint(1, 50)
                OperacionRandom = ["Suma", "Resta", "Multiplicacion"]
                OperacionRandom = random.choice(OperacionRandom)

                if OperacionRandom == "Suma":
                    RespuestaJugador = int(input(f"\nCual es el resultado de sumar {Random1} + {Random2}?: "))
                    RespuestaCorrecta = Random1 + Random2

                elif OperacionRandom == "Resta":
                    RespuestaJugador = int(input(f"\nCual es el resultado de restar {Random1} - {Random2}?: "))
                    RespuestaCorrecta = Random1 - Random2

                elif OperacionRandom == "Multiplicacion":
                    RespuestaJugador = int(input(f"\nCual es el resultado de multiplicar {Random1} x {Random2}?: "))
                    RespuestaCorrecta = Random1 * Random2

                if RespuestaJugador == RespuestaCorrecta:
                    Puntuacion += 1
                    print("*********************************")
                    print("*Felicidades respuesta correcta *")
                    print("*+1 punto.                      *")
                    print("*********************************")
                elif RespuestaJugador != RespuestaCorrecta:
                    Vidas -= 1
                    print("*********************************")
                    print("*Lo siento respuesta incorrecta *")
                    print("*-1 vida                        *")
                    print("*********************************")

            elif Vidas == 0:
                print(" ")
                print("************************************")
                print("*            GAME OVER             *")
                print("************************************")
                print("*Te quedaste sin vidas.            *")
                print(f"*Tu puntuación {Puntuacion}                   *")
                print("************************************")
                input("\nPresione ENTER para continuar.")
                break
        except ValueError as e:
            Vidas -= 1
            print("******************************************")
            print("*Error: Debes ingresar un número válido. *")
            print("*-1 vida                                 *")
            print("******************************************")

def Nivel3():
    Puntuacion = 0
    Vidas = 3
    while True:
        try:
            print(f"Tus vidas son {Vidas}.")
            print(f"Tu puntuación es {Puntuacion}.")
            if Vidas > 0:
                Random1 = random.randint(1, 100)
                Random2 = random.randint(1, 100)
                while Random2 == 0:
                    Random2 = random.randint(1, 100)
                OperacionRandom = ["Suma", "Resta", "Multiplicacion", "Division"]
                OperacionRandom = random.choice(OperacionRandom)

                if OperacionRandom == "Suma":
                    RespuestaJugador = int(input(f"\nCual es el resultado de sumar {Random1} + {Random2}?: "))
                    RespuestaCorrecta = Random1 + Random2

                elif OperacionRandom == "Resta":
                    RespuestaJugador = int(input(f"\nCual es el resultado de restar {Random1} - {Random2}?: "))
                    RespuestaCorrecta = Random1 - Random2

                elif OperacionRandom == "Multiplicacion":
                    RespuestaJugador = int(input(f"\nCual es el resultado de multiplicar {Random1} x {Random2}?: "))
                    RespuestaCorrecta = Random1 * Random2
 
                elif OperacionRandom == "Division":
                    try:
                        RespuestaJugador = float(input(f"\n¿Cuál es el resultado de dividir {Random1} / {Random2}?: "))
                        RespuestaCorrecta = round(Random1 / Random2, 2)
                        
                        if abs(RespuestaJugador - RespuestaCorrecta) < 0.01:
                            Puntuacion += 1
                            print("************************************")
                            print("* ¡Felicidades! Respuesta correcta *")
                            print("* +1 punto.                        *")
                            print("************************************")
                            continue
                        else:
                            Vidas -= 1
                            print("***********************************")
                            print("* Lo siento, respuesta incorrecta *")
                            print("* -1 vida                         *")
                            print("***********************************")
                            continue
                    except ValueError:
                        Vidas -= 1
                        print("***********************************")
                        print("* Entrada inválida                *")
                        print("* Ingresa un número con decimales *")
                        print("* Ejemplo: 1.75                   *")
                        print("***********************************")
                        continue
                
                if RespuestaJugador == RespuestaCorrecta:
                        Puntuacion += 1
                        print("*********************************")
                        print("*Felicidades respuesta correcta *")
                        print("*+1 punto.                      *")
                        print("*********************************")

                elif RespuestaJugador != RespuestaCorrecta:
                        Vidas -= 1
                        print("*********************************")
                        print("*Lo siento respuesta incorrecta *")
                        print("*-1 vida                        *")
                        print("*********************************")

            elif Vidas == 0:
                print(" ")
                print("************************************")
                print("*            GAME OVER             *")
                print("************************************")
                print("*Te quedaste sin vidas.            *")
                print(f"*Tu puntuación {Puntuacion}                   *")
                print("************************************")
                input("\nPresione ENTER para continuar.")
                break
        except ValueError as e:
            Vidas -= 1
            print("******************************************")
            print("*Error: Debes ingresar un número válido. *")
            print("*-1 vida                                 *")
            print("******************************************")

while True:
    Menu()
    try:
        opcion = int(input("\nSeleccione la opción que desea realizar: "))
    except ValueError as e:
        print("Digite una opción valida.")
        input("\nPresione ENTER para continuar.")
        continue

    if opcion == 1:
        Menu2()
        try:
            opcion = int(input("\nSeleccione la dificultad que desea jugar: "))

            if opcion == 1:
                Nivel1()
            elif opcion == 2:
                Nivel2()
            elif opcion == 3:
                Nivel3()
            elif opcion == 4:
                Menu()
            else:
                print("Digite una opción valida.")
                input("\n Presione ENTER para continuar.")
        except ValueError as e:
            print("Digite una opción valida.")
            input("\n Presione ENTER para continuar.")
            continue
    elif opcion == 2:
        print("**************************************************************************************************************************")
        print("*                                                         REGLAS                                                         *")
        print("**************************************************************************************************************************")
        print("* 1. Inicias con 3 vidas y 0 puntos.                                                                                     *")
        print("* 2. Hay 3 dificultades: Fácil, Medio y Difícil, representadas por Nivel 1, Nivel 2 y Nivel 3.                           *")
        print("* 3. En cada dificultad recibirás números que dependiendo de la dificultad deberás sumar, restar, multiplicar o dividir. *")
        print("* 4. En la dificultad Fácil recibirás números del 1 al 10 y deberás sumarlos o restarlos.                                *")
        print("* 5. En la dificultad Media recibirás números del 1 al 50 y deberás sumarlos, restarlos o multiplicarlos.                *")
        print("* 6. En la dificultad Difícil recibirás números del 1 al 100 y deberás sumarlos, restarlos, multiplicarlos o dividirlos. *")
        print("* 7. En la división, recuerda dar tu respuesta con 2 decimales y usar como separador (.), por ejemplo: 1.75.             *")
        print("* 8. Cada vez que salgas y entres a una dificultad, se reiniciarán tus vidas y tu puntuación.                            *")
        print("* 9. Cuando te quedes sin vidas, se mostrará una pantalla con tu puntuación final y serás enviado al menú.               *")
        print("* 10. Si deseas dejar de jugar, selecciona la opción 3 en el menú para salir del juego.                                  *")
        print("**************************************************************************************************************************")
        input("\nPresione ENTER para continuar.")
    elif opcion == 3:
        print("Gracias por jugar!")
        print("Cerrando el programa...")
        break
    else:
        print("Digite una opción valida.")
        input("\nPresione ENTER para continuar.")


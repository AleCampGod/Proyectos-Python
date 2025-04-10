import pyodbc
import random
from datetime import datetime

SERVER = 'ALEJANDRO'
DATABASE = 'ProyectoFinal'

CONN_STR = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'

def ConectarBD():
    try:
        conn = pyodbc.connect(CONN_STR)
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

def Historial(Nombre, Palabra, IntentosRestantes, LetrasAdivinadas):
    conn = ConectarBD()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Historial (NombreUsuario, Palabra, IntentosRestantes, LetrasAdivinadas, Fecha) "
            "VALUES (?, ?, ?, ?, ?)", 
            (Nombre, Palabra, IntentosRestantes, ",".join(LetrasAdivinadas), datetime.now())
        )
        conn.commit()
        conn.close()
        print("* Historial guardado correctamente. *")
    else:
        print("No se pudo conectar a la base de datos.")

PALABRAS = [
    "python", "computadora", "programacion", "desarrollo", "software",
    "inteligencia", "algoritmo", "variable", "funcion", "bucle",
    "base", "datos", "conexion", "servidor", "cliente", "sistema",
    "hardware", "redes", "seguridad", "virtualizacion"
]

def Reglas():
    print("************************************************************************")
    print("*                        REGLAS DEL JUEGO                              *")
    print("************************************************************************")
    print("*1. Debes adivinar la palabra oculta, letra por letra.                 *")
    print("*2. Solo puedes ingresar una letra por intento.                        *")
    print("*3. Si la letra está en la palabra, se mostrará en su posición.        *")
    print("*4. Si fallas, pierdes una vida. Tienes un máximo de 6 vidas.          *")
    print("*5. Si adivinas la palabra antes de que se acaben los vidas, ganas.    *")
    print("*6. Si pierdes, se revelará la palabra secreta.                        *")
    print("************************************************************************\n")
    input("Presione ENTER para continuar.")

def Ahorcado():
    Palabra = random.choice(PALABRAS)
    Oculta = ["_"] * len(Palabra)
    LetrasAdivinadas = set()
    vidas = 6

    Nombre = input("\nIngrese su nombre: ")

    while vidas > 0 and "_" in Oculta:
        print("\nPalabra: ", " ".join(Oculta))
        print(f"Letras adivinadas: {', '.join(LetrasAdivinadas) if LetrasAdivinadas else 'Ninguna'}")
        print(f"Intentos restantes: {vidas}")
        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("¡Error! Ingresa solo una letra válida (sin números o espacios).")
            continue

        if letra in LetrasAdivinadas:
            print("Ya intentaste con esa letra. Intenta otra diferente.")
            continue

        LetrasAdivinadas.add(letra)

        if letra in Palabra:
            for i, l in enumerate(Palabra):
                if l == letra:
                    Oculta[i] = letra
            print("¡Letra correcta!")
        else:
            vidas -= 1
            print("Letra incorrecta.")

        if vidas == 0:
            break
            
    if "_" not in Oculta:
        print(f"\n ¡Felicidades, {Nombre}! \nAdivinaste la palabra: {Palabra}")
        Historial(Nombre, Palabra, vidas, list(LetrasAdivinadas))
        input("Presione ENTER para continuar.")
    else:
        print("\nGame Over.")
        print(f"La palabra era: {Palabra}")
        Historial(Nombre, Palabra, vidas, list(LetrasAdivinadas))
        input("Presione ENTER para continuar.")


def Menu():
    while True:
        try:
            print("\n**********************************")
            print("*BIENVENIDO AL JUEGO DEL AHORCADO*")
            print("**********************************")
            print("*1. Jugar                        *")
            print("*2. Ver reglas                   *")
            print("*3. Salir                        *")
            print("**********************************")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Ahorcado()
            elif opcion == "2":
                Reglas()
            elif opcion == "3":
                print("Gracias por jugar.")
                print("Cerrando...")
                break
            else:
                print("Opción inválida.")
        except ValueError as e:
            print("Ingrese una opción valida.")

if __name__ == "__main__":
    Menu()

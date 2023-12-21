#Son las varibles con las que inicia el juego y la interfaz del usuario

A = str(input("Ingrese el nombre del jugador: "))
B = "Bienvenido "
print(B + A)

C = str(input("Quieres jugar?")) .upper()
D = "SI"
E = "NO"
F = "!!__EMPECEMOS__!!"
G = "VUELVE PRONTO"

def BIEN(WIN):
                    
    print("!!CORREECTO!!")
    print(WIN)
    print("PUNTOS")
    return WIN + (20)

def MAL(SCORE):
    
    print("!!FALLASTE!!")
    print("TE QUEDAN:")
    print(SCORE)
    print ("VIDAS")
    return SCORE -(1)

def MALFINAL(SCORE):
    print("TE QUEDAN:")
    print(SCORE)
    print("VIDAS")
    print("!!HAS PERDIDO :(!!") 
    print("GRACIAS POR JUGAR " + A)

import random

BASEDEDATOS = ["PALABRA","PABLABRA2","PALABLRA3"]

PALABRA = ["M","U","R","C","I","E","L","A","G","O"]
PROBLEMA = ["M","_","R","C","_","_","L","_","G","_"]
#INDEX [0,1,2,3,4,5,6,7,8,9]

PALABRA2 = ["R","I","A","C","H","U","E","L","O"]
PROBLEMA2 = ["R","_","_","C","H","_","_","L","_"]
#INDEX [0,1,2,3,4,5,6,7,8]

PALABRA3 = ["C","O","M","U","N","I","C","A","R","S","E"]
PROBLEMA3 = ["C","_","M","_","N","_","C","_","R","S","_"]
#INDEX [0,1,2,3,4,5,6,7,8]



if(C == D):
    print("!!__GENIAL__!!")
    print(F)

    FILE = random.choice(BASEDEDATOS)

    if(FILE == BASEDEDATOS[0]):
        
        (print("!!INTETNA ADIVINAR LA SIGUIENTE PALABRA COMPLETA!!"))
        print(PROBLEMA)
        LETRA = str(input("INGRESA TU RESPUESTA :")) .upper()
        if (LETRA == "MURCIELAGO"):
                print("!!WOW ERES UN GENIO!!")
                print("!!_-FELICIDADES GANASTE-_!!")
                print("GRACIAS POR JUGAR " + A)
        else:
            print("NO ESTA CORRECTO, INTENTA CON UNA LETRA " + A)

            SCORE = 5
            WIN = 0
            print(PROBLEMA)

            while WIN <= 99:
                LETRA = str(input("INTENTA INGRESA UNA LETRA:_")).upper()
                if PALABRA[1] == LETRA:
                    PROBLEMA[1] = "U"
                    WIN = BIEN(WIN)
                    print(PROBLEMA)
                elif PALABRA[4] == LETRA:
                    PROBLEMA[4] = "I"
                    WIN = BIEN(WIN)
                    print(PROBLEMA)
                elif PALABRA[5] == LETRA:
                    PROBLEMA[5] = "E"
                    WIN = BIEN(WIN)
                    print(PROBLEMA)
                elif PALABRA[7] == LETRA:
                    PROBLEMA[7] = "A"
                    WIN = BIEN(WIN)
                    print(PROBLEMA)
                elif PALABRA[9] == LETRA:
                    PROBLEMA[9] = "O"
                    WIN = BIEN(WIN)
                    print(PROBLEMA)
                else:
                    SCORE = MAL(SCORE)
                    print("vidas")
                    print(PROBLEMA)

                    if SCORE <= (0):
                        MALFINAL(SCORE)
                        break
            else:
                print("!!_-FELICIDADES GANASTE-_!!")
                print("GRACIAS POR JUGAR " + A)

    elif (FILE == BASEDEDATOS[1]):

        (print("!!INTETNA ADIVINAR LA SIGUIENTE PALABRA COMPLETA!!"))
        print(PROBLEMA2)
        LETRA = str(input("INGRESA TU RESPUESTA :")) .upper()
        if (LETRA == "RIACHUELO"):
                print("!!WOW ERES UN GENIO!!")
                print("!!_-FELICIDADES GANASTE-_!!")
                print("GRACIAS POR JUGAR " + A)
        else:
            print("NO ESTA CORRECTO, INTENTA CON UNA LETRA " + A)

            SCORE = 5
            WIN = 0
            print(PROBLEMA2)
            while WIN <= 99:
                LETRA = str(input("INTENTA INGRESA UNA LETRA:_")).upper()
                if PALABRA2[1] == LETRA:
                    PROBLEMA2[1] = "I"
                    WIN = BIEN(WIN)
                    print(PROBLEMA2)
                elif PALABRA2[2] == LETRA:
                    PROBLEMA2[2] = "A"
                    WIN = BIEN(WIN)
                    print(PROBLEMA2)
                elif PALABRA2[5] == LETRA:
                    PROBLEMA2[5] = "U"
                    WIN = BIEN(WIN)
                    print(PROBLEMA2)
                elif PALABRA2[6] == LETRA:
                    PROBLEMA2[6] = "E"
                    WIN = BIEN(WIN)
                    print(PROBLEMA2)
                elif PALABRA2[8] == LETRA:
                    PROBLEMA2[8] = "O"
                    WIN = BIEN(WIN)
                    print(PROBLEMA2)
                else:
                    SCORE = MAL(SCORE)
                    print(PROBLEMA2)

                    if SCORE <= (0):
                        print("TE QUEDAN:")
                        print(SCORE)
                        print("VIDAS")
                        print("!!HAS PERDIDO :(!!") 
                        print("GRACIAS POR JUGAR " + A)
                        break
            else:
                print("!!_-FELICIDADES GANASTE-_!!")
                print("GRACIAS POR JUGAR " + A)

    elif (FILE == BASEDEDATOS[2]):

        (print("!!INTETNA ADIVINAR LA SIGUIENTE PALABRA COMPLETA!!"))
        print(PROBLEMA3)
        LETRA = str(input("INGRESA TU RESPUESTA :")) .upper()
        if (LETRA == "COMUNICARSE"):
                print("!!WOW ERES UN GENIO!!")
                print("!!_-FELICIDADES GANASTE-_!!")
                print("GRACIAS POR JUGAR " + A)
        else:
            print("NO ESTA CORRECTO, INTENTA CON UNA LETRA " + A)

            SCORE = 6
            WIN = 0
            print(PROBLEMA3)
                            #PROBLEMA3 = ["C","_","M","_","N","_","C","_","R","S","_"]
            while WIN <= 99:
                LETRA = str(input("INTENTA INGRESA UNA LETRA:_")).upper()
                if PALABRA3[1] == LETRA:
                    PROBLEMA3[1] = "O"
                    WIN = BIEN(WIN)
                    print(PROBLEMA3)
                elif PALABRA3[3] == LETRA:
                    PROBLEMA3[3] = "U"
                    WIN = BIEN(WIN)
                    print(PROBLEMA3)
                elif PALABRA3[5] == LETRA:
                    PROBLEMA3[5] = "I"
                    WIN = BIEN(WIN)
                    print(PROBLEMA3)
                elif PALABRA3[7] == LETRA:
                    PROBLEMA3[7] = "A"
                    WIN = BIEN(WIN)
                    print(PROBLEMA3)
                elif PALABRA3[10] == LETRA:
                    PROBLEMA3[10] = "E"
                    WIN = BIEN(WIN)
                    print(PROBLEMA3)
                else:
                    SCORE = MAL(SCORE)
                    if SCORE <= 0:
                        print("TE QUEDAN:")
                        print(SCORE)
                        print("VIDAS")
                        print("!!HAS PERDIDO :(!!") 
                        print("GRACIAS POR JUGAR " + A)
                        break
            else:
                print("!!_-FELICIDADES GANASTE-_!!")
                print("GRACIAS POR JUGAR " + A)


elif (C == E):   
    print("ENTENDIDO, " + G + " " + A)
else:
    print("Respuesta no identificada reinica el juego por favor " + A)

#Aqui finaliza el juego y se cierra.G
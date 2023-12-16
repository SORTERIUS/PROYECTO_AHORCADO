#Son las varibles con las que inicia el juego y la interfaz del usuario

A = str(input("Ingrese el nombre del jugador: "))
B = "Bienvenido "
print(B + A)
print("POR FAVOR ACTIVA LAS MAYUSCULAS")
C = str(input("Quieres jugar?")) .upper()
D = "SI"
E = "NO"
F = "!!__EMPECEMOS__!!"
G = "VUELVE PRONTO"

#Aquí empieza el inicio del juego y le permite al usuario intentar adivinar la palabra completa

if(C == D):
    print("!!__GENIAL__!!")
    print(F)
    str(print("!!INTETNA ADIVINAR LA SIGUIENTE PALABRA COMPLETA!!"))
    str(print("--!!M _ RC _ _ L _ G _.!!--"))
    LETRA = str(input("INGRESA TU RESPUESTA :")) .upper()
    if (LETRA == "MURCIELAGO"):
            print("!!WOW ERES UN GENIO!!")
            print("!!_-FELICIDADES GANASTE-_!!")
            print("GRACIAS POR JUGAR " + A)
    else:
        print("NO ESTA CORRECTO, INTENTA CON UNA LETRA " + A)

        #Si falla la palabra completa puede intentar adivinarla una por una, a continuacion se ven las listas y las variables

        PALABRA = ["M","U","R","C","I","E","L","A","G","O"]
        PROBLEMA = ["M","_","R","C","_","_","L","_","G","_"]
        #INDEX [0,1,2,3,4,5,6,7,8,9]
     
        SCORE = 6
        WIN = 0
        print(PROBLEMA)

        # Aqui empieza el bucle que permite al usuario intentar adivinar letra por letra
        #  hasta completarla, solo tiene 5 vidas para adivinar, caso contratio pierde  

        while WIN <= 99:
            LETRA = str(input("INTENTA INGRESA UNA LETRA:_"))
            if PALABRA[1] == LETRA:
                PROBLEMA[1] = "U"
                print("!!CORREECTO!!")
                WIN += (20)
                print(WIN)
                print("PUNTOS")
                print(PROBLEMA)
            elif PALABRA[4] == LETRA:
                PROBLEMA[4] = "I"
                print("!!CORREECTO!!")
                WIN += (20)    
                print(WIN) 
                print("PUNTOS")
                print(PROBLEMA)
            elif PALABRA[5] == LETRA:
                PROBLEMA[5] = "E"
                print("!!CORREECTO!!")
                WIN += (20)
                print(WIN)
                print("PUNTOS")
                print(PROBLEMA)
            elif PALABRA[7] == LETRA:
                PROBLEMA[7] = "A"
                print("!!CORREECTO!!")
                WIN += (20)
                print(WIN)
                print("PUNTOS")
                print(PROBLEMA)
            elif PALABRA[9] == LETRA:
                PROBLEMA[9] = "O"
                print("!!CORREECTO!!")
                WIN += (20)
                print(WIN)
                print("PUNTOS")
                print(PROBLEMA)
            else:
                SCORE -= (1)
                print("!!FALLASTE!!")
                print("TE QUEDAN:")
                print(SCORE)
                print("VIDAS")
                print(PROBLEMA)
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
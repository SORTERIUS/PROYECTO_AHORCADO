A = str(input("Ingrese el nombre de usuario: "))
B = "Bienvenido "
print(B + A)
C = str(input("Quieres jugar?"))
D = "SI"
E = "NO"
F = "!!__EMPECEMOS__!!"
G = "ADIOS"

if(C == D):
    print(F)
    str(print("!!INTETNA ADIVINAR LA SIGUIENTE PALABRA COMPLETA!!"))
    str(print("--!!M,_,R,C,_,_,L,_,G,_.!!--"))
    LETRA = str(input("INGRESA TU RESPUESTA :"))
    if (LETRA == "MURCIELAGO"):
            print("!!CORRECTO!!")
            print("GANASTE")
    else:
        print("FALLASTE INTENTA CON UNA LETRA")

        PALABRA = ["M","U","R","C","I","E","L","A","G","O"]
        PROBLEMA = ["M","_","R","C","_","_","L","_","G","_"]

        print(PROBLEMA)
        
        for JUEGO in range (5):
            LETRA = str(input("INTENTA INGRESA UNA LETRA:_"))
            print(PROBLEMA)
            if PALABRA[1] == LETRA:
                PROBLEMA[1] = "U"
                print("!!CORREECTO!!")
                print(PROBLEMA)

            elif PALABRA[4] == LETRA:
                PROBLEMA[4] = "I"
                print("!!CORREECTO!!")
                print(PROBLEMA)
                
            elif PALABRA[5] == LETRA:
                PROBLEMA[5] = "E"
                print("!!CORREECTO!!")
                print(PROBLEMA)

            elif PALABRA[7] == LETRA:
                PROBLEMA[7] = "A"
                print("!!CORREECTO!!")
                print(PROBLEMA)

            elif PALABRA[9] == LETRA:
                PROBLEMA[9] = "O"
                print("!!CORREECTO!!")
                print(PROBLEMA)
            else:
             print("!!MAL -1P!!")

    print("SE AGOTARON TU VIDAS :( SIGUE INTENTANGOLO")
        
else:
    print("GRACIAS " + G)
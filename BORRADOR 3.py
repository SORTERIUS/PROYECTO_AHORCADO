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
        #INDEX [0,1,2,3,4,5,6,7,8,9]
        X = "GANASTE"
        Z = "!!MAL!!"
        SCORE = 5
        WIN = 0
        print(PROBLEMA)

        while SCORE <= 5:
            
            while WIN <= 99:  
                LETRA = str(input("INTENTA INGRESA UNA LETRA:_"))
                if PALABRA[1] == LETRA:
                    PROBLEMA[1] = "U"
                    print("!!CORREECTO!!")
                    print(PROBLEMA)
                    WIN += (20)
                    print(WIN)
                elif PALABRA[4] == LETRA:
                    PROBLEMA[4] = "I"
                    print("!!CORREECTO!!")
                    print(PROBLEMA)
                    WIN += (20)    
                    print(WIN)   
                elif PALABRA[5] == LETRA:
                    PROBLEMA[5] = "E"
                    print("!!CORREECTO!!")
                    print(PROBLEMA)
                    WIN += (20)
                    print(WIN)
                elif PALABRA[7] == LETRA:
                    PROBLEMA[7] = "A"
                    print("!!CORREECTO!!")
                    print(PROBLEMA)
                    WIN += (20)
                    print(WIN)
                elif PALABRA[9] == LETRA:
                    PROBLEMA[9] = "O"
                    print("!!CORREECTO!!")
                    print(PROBLEMA)
                    WIN += (20)
                    print(WIN)
                else:
                    SCORE -= (1)
                    print(SCORE)
            print("ganaste")
            break
        
        print("SE AGOTARON TU VIDAS :( SIGUE INTENTANGOLO")
        
else:
    print("GRACIAS " + G)
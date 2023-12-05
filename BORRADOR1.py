A = str(input("Ingrese el nombre de usuario: "))
B = "Bienvenido "
print(B + A)
C = str(input("Quieres jugar?"))
D = "SI"
E = "NO"
F = "!!__EMPECEMOS__!!"
G = "ADIOS"

if(C == D.lower()):
    print(F)
    str(print("ADIVINA LA SIGUIENTE PALABRA"))
    Z = "M"
    Y = "U"
    X = "R"
    W = "C"
    V = "I"
    U = "E"
    T = "L"
    S = "A"
    R = "G"
    Q = "O"
    str(print("M_RC__L_G_"))
    LETRA = str(input("ESCRIBE UNA LETRA:_"))
    if (LETRA == "MURCIELAGO"):
            print("!!CORRECTO!!")
            print("GANASTE")
    else:
        print("MAl")
        for i in range(5):
            LETRA = str(input("ESCRIBE UNA LETRA:_"))
            if (LETRA == "u" ):
                print("!!CORRECTO!!")
                print(Z+Y+X+W+"__L_G_")
            elif (LETRA == "i"):
                print("!!CORRECTO!!")
                print(Z+Y+X+W+V+"_L_G_")
            elif (LETRA == "e"):
                print("!!CORRECTO!!")
                print(Z+Y+X+W+V+U+"L_G_")
            elif (LETRA == "a"):
                print("!!CORRECTO!!")
                print(Z+Y+X+W+V+U+T+S+"G_")
            elif (LETRA == "o"):
                print("!!CORRECTO!!")
                print(Z+Y+X+W+V+U+T+S+R+Q)
            else:
                print("MAl")
        print("vidas agotadas, perdiste")
    
else:
    print("GRACIAS " + G)



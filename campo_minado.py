


def explocion():
    print("BOOM!!")
    print("BOOM! elegiste una area minada :( ")

def ganaste():
    print("eres un ganador :)")

campo = [[1, 0, 0],
         [0, 1, 0],
         [1, 1, 1] ]

texto = ["Cesped", "bomba"]

print("estas en un campo minado \n elija entre 0 y 2 para x y para y")
x = int(input("posicion en x? (entre 0 y 2) "))
y = int(input("posicion en y? (entre 0 y 2) "))

if (x <= 2 & y <= 2):
    posicion = campo[x][y]
    print("elegiste" + texto[posicion])
    if (posicion == 1):
        explocion()
    else:
        ganaste()
else:

    print("!Te saliste del campo!")
    explocion()

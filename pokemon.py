from hashlib import new


class pokemon:

    def __init__(self, nombre, vida, ataque):
        self.grito = "pika"
        self.nombre =  nombre
        self.vida = vida
        self.ataque =  ataque

    
def inicio():
    print("esto es despues del inicio")
    chamander = pokemon("chamander", 100, 24)
    chamander.vida = chamander.vida - 6
    chamander.grito = "chaaaaaa"
    print(chamander.nombre)
    print(chamander.vida)
    print(chamander.grito)
    


inicio()
print("Esto es antes del inicio")


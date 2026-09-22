"""
Crear Entrenador, Listar Entrenadores, Borrar por Pokemon, Pelea Pokemon, Fin

Lista de Tuplas vacia inicialmente, cada tupla guarda el nombre del entrenador, el del pokemon, ataque y vida.

prueba con 5 pokemones y listar, luego borra 1 pkemon y listar y que dos pk peleen y listar
"""
from random import randint 
class Pokemon:
    def __init__(self, Torena, Poke, atk, vida):
        self.Torena = Torena
        self.Poke = Poke
        self.atk = atk
        self.vida = vida
        
    """
    def __str__(self):
            return(f"Entrenador: {self.Torena}, Pokemon: {self.Poke}, Puntos de ataque: {self.atk}, Puntos de vida: {self.vida}")
    """
    
LisTu = []
def CrearEntrenador(Torena, Poke):
    for l in LisTu:
        if (l.Torena == Torena and l.Poke == Poke):
            print("Ya existen")
            return
    
    p = Pokemon(Torena, Poke, randint(150,250), randint(500,900))
    LisTu.append(Pokemon(p.Torena, p.Poke,p.atk,p.vida))
    
def ListaEntrenador():
    print("Lista de entrenadores con sus pokemones y estadisticas: ")
    for l in LisTu:
        print(l)

def BorraPorVida(vida):
        for i in range(1,len(LisTu)):
            j=i
            while j>=0 and LisTu[j-1].vida > LisTu[j].vida:
                LisTu[j-1], LisTu[j] = LisTu[j], LisTu[j-1]
                j-=1
        #Busqueda lineal
        for i, p in enumerate(LisTu):
            if p.vida == vida:
                LisTu.pop(i)
                print(f"Pokemon con vida {vida} eliminado.")
                return
        print("No se encontró pokemon con ese valor de vida")
        
def PeleaPokemon():
    print()
        
CrearEntrenador("Ash", "Pikachu")
CrearEntrenador("Misty", "Piplup")
opc = 0
while opc != 5:
    opc = input("Opciones:\n1. Agregar Entrenador(a)\n2. Mostrar Todo\n3. Borrar Pokemon\n4. Pelear\n5. Salir\nIngrese número de opción: ")
    if opc == "1":
        print("Agregar combo inseparable.-")
        Torena = input("Ingrese nombre del Trainer: ")
        Poke = input("Ingrese el nombre del Pokemon: ")
        CrearEntrenador(Torena,Poke)
        
    elif opc =="2":
        ListaEntrenador()
        
    elif opc == "3":
        break
    elif opc == "4":
        break
    elif opc == "5":
        break
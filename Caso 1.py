"""
Cree un proyecto Python para almacenar y administrar una lista Puestos de trabajo disponibles en una empresa. 
Cada Puesto de trabajo tiene los siguientes atributos: codigo (int), descripcion (string), areaSolicitante (string), y sueldo (float). Cree una lista de Puestos de trabajo, 
y haga un aplicativo que tenga el siguiente menú repetitivo. Si el nombre de la opción está entre paréntesis es una función que debe llamar desde el menú:

1 AgregaPuesto(): Registrar un nuevo Puesto de trabajo, para lo cual buscará linealmente tal que debe validar que no haya otro Puesto de trabajo con el mismo  código, 
descripcion o areaSolicitante e insertará el nuevo Puesto de trabajo.

2 MostrarTodo(): mostrará todos los Puesto de trabajo creados sin ordenar

3 BorraPuesto(): Pedirá un codigo, luego ordenará por método de inserción usando el código de menos a más y 
mediante búsqueda lineal buscará el Puesto de trabajo cuyos codigos coincidan y los eliminará de la lista.

4 BuscaSueldo(): Ordenará la lista por la talla usando método de selección de más a menos. Luego preguntará un sueldo a buscar,
y usando la búsqueda binaria encontrará todos los Puesto de trabajo con ese sueldo. 
Recuerde que como esta ordenado si hubieran varios Puesto de trabajo con el mismo sueldo van a estar justo antes o después. 
Use la menor cantidad de operaciones a la lista para mostrar lo solicitado

5 Salir: Termina el programa

Tras terminar el código agregue 6 Puesto de trabajo con los datos que considere y ejecute cada función creada"""

#def AgregaPuesto(codigo:int, descripcion, areaSolicitante:str, sueldo:float ):


class P_T:
    def __init__(self, cod, descr, areaSol, sueldo):
        self.cod = cod
        self.descr = descr
        self.areaSol = areaSol
        self.sueldo = sueldo
        
    def __str__(self):
        return f"{self.cod}, {self.descr}, {self.areaSol}, {self.sueldo}"
Puestos = []

#1 Agregar
def AgregarPuesto(cod,descr,areaSol,sueldo):
    for p in Puestos:
        if (p.cod == cod or p.descr == descr or p.areaSol == areaSol):
            print("Ya existe un puesto como ese")
            return
    Puestos.append(P_T(cod,descr,areaSol,sueldo))
    print("Puesto de trabajo añadido exitosamente")
    
#MostrarTodo
def MostrarTodo():
    print()

def BorrarPuesto():
    print()
    
def BuscarPuesto():
    print()
opc = 0    
while opc != 5:
    opc == input("Opciones:\n1. Agregar un puesto\n2. Mostrar Todo\n3. Borrar Puesto\n4. Buscar Puesto\n5. Salir\nIngrese número de opción: ")
    if opc == 1:
        print("Agregar Puesto")
        
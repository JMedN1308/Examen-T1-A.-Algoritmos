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

class P_T:
    def __init__(self, cod, descr, areaSol, sueldo):
        self.cod = cod
        self.descr = descr
        self.areaSol = areaSol
        self.sueldo = sueldo
     #Para ver que contiene el __init__ se hace el __str__   
    def __str__(self):
        return f"Codigo: {self.cod}, Descripcion: {self.descr}, Area: {self.areaSol}, Sueldo: {self.sueldo}"

puestos = []

#1 Agregar
def AgregarPuesto(cod, descr, areaSol, sueldo):
    for p in puestos:
        if (p.cod == cod or p.descr == descr or p.areaSol == areaSol):
            print("Error: Ya existe un puesto con ese codigo, descripcion o area.")
            return
        
    puestos.append(P_T(cod, descr, areaSol, sueldo))
    print("Puesto de trabajo añadido exitosamente")
    
#MostrarTodo
def MostrarTodo():
    print("\nLista de puestos de trabajo: ")
    for p in puestos:
        print(p)

def BorrarPuesto(cod):
    #Ordenado por insercion(n-1)
    for i in range(1,len(puestos)):
        j=i
        while j>=0 and puestos[j-1].cod > puestos[j].cod:
            puestos[j-1], puestos[j] = puestos[j], puestos[j-1]
            j-=1
    #Busqueda lineal
    for i, p in enumerate(puestos):
        if p.cod == cod:
            puestos.pop(i)
            print(f"Puesto con código {cod} eliminado.")
            return
    print("No se encontró el puesto")
    
def BuscarSueldo(sueldo):
    #Orden por selección descendente
    for i in range(len(puestos)):
        max_idx = i 
        for j in range(i+1, len(puestos)):
            if puestos[j].sueldo > puestos[max_idx].sueldo:
                max_idx = j
        puestos[i], puestos[max_idx] = puestos[max_idx], puestos[i]
    
    #Busqueda binaria
    low, high = 0, len(puestos)-1
    found =[]
    while low <=high:
        mid = (low + high)//2
        if puestos[mid].sueldo == sueldo:
            #Buscar vecinos con mismo sueldo
            i = mid
            while i>= 0 and puestos[i].sueldo == sueldo:
                found.append(puestos[i])
                i-=1
            i = mid +1
            while i < len(puestos) and puestos[i].sueldo == sueldo:
                found.append(puestos[i])
                i+=1
            break
        elif puestos[mid].sueldo < sueldo:
            high = mid-1
        else:
            low = mid+1
    if found:
        print("\nPuestos encontrados con sueldo ",sueldo)
        for f in found:
            print(f)
    else:
        print("No se encotraron puestos con ese sueldo.")
    

AgregarPuesto(101, "Analista de Datos", "TI", 3500)
AgregarPuesto(102, "Diseñador Gráfico", "Marketing", 2800)
AgregarPuesto(103, "Contador", "Finanzas",4000)
AgregarPuesto(104, "Ingeniero de Software", "Almacen", 5000)
AgregarPuesto(105, "Asistente Administrativo", "Administracion", 2800)
AgregarPuesto(106, "Gerente de Ventas", "Comercial",6000)

opc = 0    
while opc != 5:
    opc = input("Opciones:\n1. Agregar un puesto\n2. Mostrar Todo\n3. Borrar Puesto\n4. Buscar Sueldo\n5. Salir\nIngrese número de opción: ")
    if opc == "1":
        print("Agregar Puesto.-")
        cod = int(input("Ingrese Código: "))
        descr = str(input("Ingrese descripción del puesto: "))
        areaSol = str(input("Ingrese el area solicitante: "))
        sueldo = float(input("Ingrese sueldo: "))
        AgregarPuesto(cod, descr, areaSol, sueldo)
        
    elif opc == "2":
        MostrarTodo()
        
    elif opc == "3":
        print("Borrar Puesto.-")
        cod = int(input("Ingrese codigo a borrar: "))
        BorrarPuesto(cod)
        
    elif opc == "4":
        print("Buscar sueldo.-")
        sueldo = float(input("Ingrese sueldo a buscar: "))
        BuscarSueldo(sueldo)
        
    elif opc == "5":
        break
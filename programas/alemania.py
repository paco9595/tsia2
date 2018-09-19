import os
visitados = []
datos = []
visitados = []
class Nodo:
    def __init__(self, id, valor=0, padre='padre'):
        self.id = id
        self.hijo = []
        self.valor = valor
        self.padre = padre
def menu(opciones, texto, incio= -1):
    inteneto = 1
    os.system ("clear")
    opcion = -100
    while(opcion < 0 or opcion > len(opciones)):
        while True:
            print('\t Menu Selecione una opcion')    
            print(texto)
            for i, x in enumerate(opciones):
                if i == incio:
                    print(str(i+1)+ "-. "+ str(x) + ' inicio')
                else:
                    print(str(i+1)+ "-. "+ str(x))
            try:
                opcion = int(input("ingrese una opcion valida: ")) - 1 
                if opcion >= 0 and opcion < len(opciones) and not opcion == incio:
                    return opcion
                os.system ("clear")
                print("ingrese una opcion valida")
            except:
                os.system ("clear")
                print("ingrese una opcion valida")
def LeerDatos(nombre):
    try :
        archivo = open(nombre,"r")
        suma = ""
        aux = []
        datos = []
        i = 0
        for linea in archivo.readlines():
            for x in linea:
                if x != " " and x != "\n" and x != "-":
                    suma += x
                else:
                    if(len(suma) > 0):
                        aux.append(int(suma))
                        suma = ""
            if(len(aux)>0):
                i += 1
                datos.append(aux)
                aux = []
        return datos
    except ValueError:
        print('format error')
        return

def leerNombres(nombre):
    try :
        archivo = open(nombre,"r")
        suma = ""
        aux = ''
        datos = []
        i = 0
        for linea in archivo.readlines():
            for x in linea:
                if x != " " and x != "\n" and x != "-":
                    suma += x
                else:
                    if(len(suma) > 0):
                        aux=suma
                        suma = ""
            if(len(aux)>0):
                i += 1
                datos.append(aux)
                aux = []
        return datos
    except ValueError:
        print('format error')
        return
def Generar_arbol(nodo_inicial,nodo_final):
    global datos
    global visitados
    estado = Nodo(nodo_inicial)
    aux= []
    while True:
        if (nodo_final == estado.id):
            print estado.id, estado.hijo, estado.valor
            visitados.append(nodo_final)
            return estado.valor
        estado.hijo = sacar_hijos(estado,Nodo(nodo_inicial))
        print  estado.id, estado.hijo, estado.valor
        while len(estado.hijo)  == 0 :
            print 'regreso', estado.id, estado.padre.id, estado.padre.hijo
            aux.append(estado.id)
            estado = estado.padre
            estado.hijo = sacar_hijos(estado,Nodo(nodo_inicial),aux)
        hijo = min(estado.hijo)
        estado = Nodo(hijo[1], estado.valor + hijo[0], estado)

def sacar_hijos(nodo,nodo_inicial,regreso=[]):
    global datos
    global visitados
    posibles = []
    hijos = [[a,i] for i,a in enumerate(datos[nodo.id]) if a > 0]
    visitados = buscar_nodo(nodo,nodo_inicial)
    for x in regreso:
        visitados.append(x)
    t= True
    for x in hijos:
        for y in visitados:
            if x[1] == y:
                t = False
        if t:
            posibles.append(x)
        else:
            t = True
    return posibles
            
def buscar_nodo(nodo,nodo_inicial):
    if nodo.padre == 'padre':
        return [nodo_inicial.id]
    aux = buscar_nodo(nodo.padre,nodo_inicial)
    aux.append(nodo.id)
    return aux



def main():
    global datos
    global visitados
    datos = LeerDatos('./datos/alemania.txt')
    nombres = leerNombres('./datos/nombre_alemania.txt')
    inicio = menu(nombres, "selecione la ciudad de inicio")
    final = menu(nombres,' selecione la ciudad final', inicio)

    valor = Generar_arbol(inicio,final)
    print 'camino'
    for i,x in enumerate(visitados):
        print x+1, nombres[x]

    print 'el costo es', valor
main()
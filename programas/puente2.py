visitados = []

class Nodo:
     def __init__(self,estado,valor=0,hijo=[],lampara=True,padre='padre'):
        self.estado = estado # son las personas de los puentes posicion 0 es el lado derecho
        self.valor = valor # es el tiempo que llevan en cursar el puente
        self.hijo = hijo # son los las personas que se pueden cambiar de lado
        self.lampara = lampara # es un boleano que true la lapara esta del lado derecho
        self.padre = padre # es el estado anterior 

def estado_visitadas(estado):
    global visitados 
    for visitado in visitados:
        if visitado == estado:
            return False
    return True

def generar_hijos(nodo):
    aux = []
    lado = nodo.lampara and nodo.estado[0] or nodo.estado[1]
    for i in range(len(lado)):
        for j in range(len(lado)):
            if j>=i:
                lado_derecho = [x for x in nodo.estado[0]]
                lado_izquierdo = [x for x in nodo.estado[1]]
                if nodo.lampara:
                    lado_izquierdo.append(lado[i])
                    lado_derecho.pop(i)
                    lado_izquierdo.append(lado[j])
                    lado_derecho.pop(j-1)
                else:
                    lado_derecho.append(lado[i])
                    lado_izquierdo.pop(i)
                    lado_derecho.append(lado[j])
                    lado_izquierdo.pop(j-1)
                if estado_visitadas([lado_derecho,lado_izquierdo]) and not((i==j) and nodo.lampara):
                    aux.append(Nodo([lado_derecho,lado_izquierdo],(nodo.valor + max([lado[i],lado[j]])),[],not(nodo.lampara), nodo))
    return aux
def algoritmo(estado_inicial,estado_final,camino):
    global  visitados
    nodo = Nodo(estado_inicial)
    aux= []
    while True:
        if comparar_estado_final(nodo.estado,estado_final) and camino:
            print '-----------'
            print 'estado ',nodo.estado
            print 'hijos ',[ x.estado for x in nodo.hijo]
            print 'valor', nodo.valor
            print 'lampara', nodo.lampara
            return nodo
        nodo.hijo = generar_hijos(nodo)
        print '-----------'
        print 'estado ',nodo.estado
        print 'hijos ',[ x.estado for x in nodo.hijo]
        print 'valor', nodo.valor
        print 'lampara', nodo.lampara
        while len(nodo.hijo) == 0 :
            print 'regreso', nodo.estado, nodo.padre   
            visitados.append(nodo.estado)
            if not(type(nodo.padre) is str):
                nodo = nodo.padre
            else:
                print generar_hijos(nodo)
                return nodo
            nodo.hijo = generar_hijos(nodo)
        hijoId = min([[x.valor,i ] for i,x in enumerate(nodo.hijo)])[1]
        visitados.append(nodo.estado)
        nodo = nodo.hijo[hijoId]

def comparar_estado_final(estado,final):
    if (len(estado[0])>0):
        return False
    for x in estado[1]:
        try:
            final[1].index(x)
        except ValueError:
            return False
    return True

def leerDatos(archivo):
    archivo = open(archivo,"r")
    suma=""
    aux=[]
    datos=[]
    for linea in archivo.readlines():
        for x in linea:
            if x!=" " and x!="\n":
                suma+=x
            else:
                if(len(suma)>0):
                    aux.append(int(suma))
                    suma=""
        if(len(aux)>0):
            datos.append(aux)
            aux=[]
    for i,x in enumerate(datos):
        datos[i] = x[0]
        
    return datos
def main():
    global visitados
    lado_derecho = leerDatos('./datos/puente.txt')
    estado_inicial= [lado_derecho,[]]
    estado_final = [[],lado_derecho]
    visitados.append(estado_inicial)
    print algoritmo(estado_inicial,estado_final,False).estado




main()
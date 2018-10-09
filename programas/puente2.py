class Nodo:
     def __init__(self,estado,valor=0,hijo=[],lampara=True):
        self.estado = estado
        self.valor = valor
        self.hijo = hijo
        self.lampara = lampara
    
def generar_hijos(nodo):
    lado = nodo.lampara and nodo.estado[0] or nodo.estado[1]
    for i in range(len(lado)):
        for j in range(len(lado)):
            if i != j and j>i:
                lado_derecho = [x for x in nodo.estado[0]]
                lado_izquierdo = [x for x in nodo.estado[1]]
                if nodo.lampara:
                    lado_izquierdo.append(lado[i])
                    lado_izquierdo.append(lado[j])
                    lado_derecho.pop(i)
                    lado_derecho.pop(j-1)
                else:
                    lado_derecho.append(lado[i])
                    lado_derecho.append(lado[j])
                    lado_izquierdo.pop(i)
                    lado_izquierdo.pop(j-1)
                
                nodo.hijo.append(Nodo([lado_derecho,lado_izquierdo],max([i,j]),[],False))
    return nodo
def algoritmo(nodo):
    

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
                    aux.append(float(suma))
                    suma=""
        if(len(aux)>0):
            datos.append(aux)
            aux=[]
    for i,x in enumerate(datos):
        datos[i] = x[0]
        
    return datos

def main():
    lado_derecho = leerDatos('./datos/puente.txt')
    estado_inicial= [[],lado_derecho]
    lado_izquierdo = []
    nodo_inicial = Nodo([lado_derecho,lado_izquierdo])
    algoritmo(nodo_inicial)
    # print nodo_inicial.estado
    # nodo_inicial = generar_hijos(nodo_inicial)
    # for x in nodo_inicial.hijo:
    #     print x.estado




main()
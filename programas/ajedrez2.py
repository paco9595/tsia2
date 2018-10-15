import os
class Tablero:
    def __init__(sefl,juego,coverage=0):
        self.juego = juego
        self.coverage = coverage

class Alfil:
    def __init__(self,tablero):
        self.posiciones = []
        self.tablero = tablero
        self.coverage = 0
        self.atacar()
        self.sacar_covertura(self.tablero)
    def atacar(self):
        tablero_atacado=[]
        for x in range(8):
            aux =[]
            for y in range(8):
                try:
                    self.posiciones.index([x,y])
                    aux.append(1)
                except ValueError:
                    aux.append(0)
            tablero_atacado.append(aux)
        for i,posicion in enumerate(self.posiciones):
            for x in range(1,min(posicion)+1):
                # print(x),[posicion[0]-x, posicion[1]-x], len(tablero_atacado)
                tablero_atacado[posicion[0]-x][posicion[1]-x] = 1
            for x in range(0,7-max(posicion)):
                # print [posicion[0]+x,posicion[1]-x]
                tablero_atacado[posicion[0]+x][posicion[1]-x] = 1
            for x in range(0,7-max(posicion)+1):
                # print(x), [posicion[0]-x,posicion[1]+x]
                tablero_atacado[posicion[0]-x][posicion[1]+x] = 1
            for x in range(1,7-max(posicion)+1):
                # print(x), [posicion[0]+x,posicion[1]+x]
                tablero_atacado[posicion[0]+x][posicion[1]+x] = 1
        return self.sacar_covertura(tablero_atacado),tablero_atacado
    def sacar_covertura(self,tablero):
        counter = 0
        for x in tablero:
            for y in x:
                counter += y
        return (counter*100)/float(len(self.tablero)*len(self.tablero[0]))
    
class Torre:
    def __init__(self,tablero):
        self.posiciones = []
        self.tablero = tablero
        self.coverage = 0
        self.atacar()
        self.sacar_covertura(self.tablero)
    def atacar(self):
        tablero_atacado=[]
        for x in range(8):
            aux =[]
            for y in range(8):
                try:
                    self.posiciones.index([x,y])
                    aux.append(1)
                except ValueError:
                    aux.append(0)
            tablero_atacado.append(aux)
        for posicion in self.posiciones:
            for x in range(len(self.tablero)):
                tablero_atacado[x][posicion[1]] = 1
                tablero_atacado[posicion[0]][x] = 1

        return self.sacar_covertura(tablero_atacado),tablero_atacado
    def sacar_covertura(self,tablero):
        counter = 0
        for x in tablero:
            for y in x:
                counter += y
        return (counter*100)/float(len(self.tablero)*len(self.tablero[0]))

class Caballo:
    def __init__(self,tablero):
        self.posiciones = []
        self.tablero = tablero
        self.coverage = 0
        self.atacar()
        self.sacar_covertura(self.tablero)
    def atacar(self):
        tablero_atacado=[]
        for x in range(8):
            aux =[]
            for y in range(8):
                try:
                    self.posiciones.index([x,y])
                    aux.append(1)
                except ValueError:
                    aux.append(0)
            tablero_atacado.append(aux)
        for posicion in self.posiciones:
            if posicion[0]>=2:
                if posicion[1]>0:
                    tablero_atacado[posicion[0]-2][posicion[1]-1] = 1
                if posicion[1] < len(tablero_atacado)-1:
                    tablero_atacado[posicion[0]-2][posicion[1]+1] = 1
            if posicion[1] < len(tablero_atacado)-2:
                if posicion[0]>0:
                    tablero_atacado[posicion[0]-1][posicion[1] + 2] = 1
                if posicion[0]< len(tablero_atacado)-1:
                    tablero_atacado[posicion[0]+1][posicion[1] + 2] = 1
            if posicion[0] < len(tablero_atacado)-2:
                if posicion[1] < len(tablero_atacado)-1:
                    tablero_atacado[posicion[0]+2][posicion[1]+1] = 1
                if posicion[1] > 0:
                    tablero_atacado[posicion[0]+2][posicion[1]-1] = 1
            if posicion[1] >= 2:
                if posicion[0]> 0:
                    tablero_atacado[posicion[0]-1][posicion[1]-2] = 1
                if posicion[0]< len(tablero_atacado)-1:
                    tablero_atacado[posicion[0]+1][posicion[1]-2] = 1
        return self.sacar_covertura(tablero_atacado),tablero_atacado
    def sacar_covertura(self,tablero):
        counter = 0
        for x in tablero:
            for y in x:
                counter += y
        return (counter*100)/float(len(self.tablero)*len(self.tablero[0]))

class Reina:
    def __init__(self,tablero):
        self.posiciones = []
        self.tablero = tablero
        self.coverage = 0
        self.atacar()
        self.sacar_covertura(self.tablero)
    def atacar(self):
        tablero_atacado=[]
        for x in range(8):
            aux =[]
            for y in range(8):
                try:
                    self.posiciones.index([x,y])
                    aux.append(1)
                except ValueError:
                    aux.append(0)
            tablero_atacado.append(aux)
        for i,posicion in enumerate(self.posiciones):
            for x in range(len(self.tablero)):
                tablero_atacado[x][posicion[1]] = 1
                tablero_atacado[posicion[0]][x] = 1
            for x in range(1,min(posicion)+1):
                # print(x),[posicion[0]-x, posicion[1]-x], len(tablero_atacado)
                tablero_atacado[posicion[0]-x][posicion[1]-x] = 1
            if max(posicion)>0:
                for x in range(0,7-max(posicion)):
                    tablero_atacado[posicion[0]+x][posicion[1]-x] = 1
            if max(posicion)>0:
                for x in range(0,7-max(posicion)+1):
                    tablero_atacado[posicion[0]-x][posicion[1]+x] = 1
            for x in range(1,7-max(posicion)+1):
                #print(x), [posicion[0]+x,posicion[1]+x]
                tablero_atacado[posicion[0]+x][posicion[1]+x] = 1
        return self.sacar_covertura(tablero_atacado),tablero_atacado
    def sacar_covertura(self,tablero):
        counter = 0
        for x in tablero:
            for y in x:
                counter += y
        return (counter*100)/float(len(self.tablero)*len(self.tablero[0]))

class Rey:
    def __init__(self,tablero):
        self.posiciones = []
        self.tablero = tablero
        self.coverage = 0
        self.atacar()
        self.sacar_covertura(self.tablero)
    def atacar(self):
        tablero_atacado=[]
        for x in range(8):
            aux =[]
            for y in range(8):
                try:
                    self.posiciones.index([x,y])
                    aux.append(1)
                except ValueError:
                    aux.append(0)
            tablero_atacado.append(aux)
        for posicion in self.posiciones:
            if posicion[0] > 0:
                if posicion[1] > 0:
                   tablero_atacado[posicion[0]-1][posicion[1]-1] = 1
                if posicion[1] < len(tablero_atacado)-1:
                    tablero_atacado[posicion[0]-1][posicion[1]+1] = 1
                tablero_atacado[posicion[0]-1][posicion[1]] = 1
            if posicion[1] < len(tablero_atacado)-1:
                tablero_atacado[posicion[0]][posicion[1]+1] = 1
                if posicion[0] < len(tablero_atacado)-1:
                    tablero_atacado[posicion[0]+1][posicion[1]+1] = 1
            if posicion[0] < len(tablero_atacado)-1:
                tablero_atacado[posicion[0]+1][posicion[1]] = 1
                if posicion[1] > 0:
                    tablero_atacado[posicion[0]+1][posicion[1]-1] = 1
            if posicion[1] > 0:
                tablero_atacado[posicion[0]][posicion[1]-1] = 1
        return self.sacar_covertura(tablero_atacado),tablero_atacado
    def sacar_covertura(self,tablero):
        counter = 0
        for x in tablero:
            for y in x:
                counter += y
        return (counter*100)/float(len(self.tablero)*len(self.tablero[0]))

def menu(opciones, texto):
    inteneto = 1
    os.system ("clear")
    opcion = -100
    while(opcion < 0 or opcion > len(opciones)):
        while True:
            print('\t Menu Selecione una opcion')    
            print(texto)
            for i, x in enumerate(opciones):
                print(str(i+1)+ "-. "+ str(x))
            try:
                opcion = int(input("ingrese una opcion valida: "))
                if opcion > 0 and opcion <= len(opciones):
                    return opcion
                os.system ("clear")
                print("ingrese una opcion valida")
            except:
                os.system ("clear")
                print("ingrese una opcion valida")

def algoritmo(objeto, tablero):
    while objeto.sacar_covertura(tablero)<100:
        mejor_coverage = 0
        mejor_pos = []
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                objeto.posiciones.append([i,j])
                prosp,tablero = objeto.atacar()
                objeto.posiciones.pop()
                if prosp > mejor_coverage:
                    mejor_pos= [i,j]
                    mejor_coverage = prosp
        objeto.posiciones.append(mejor_pos)
    # print objeto.sacar_covertura(tablero), objeto.posiciones
    print 'Cantidad de piezas: ', len(objeto.posiciones) 
    print 'posiciones: ', objeto.posiciones
    tablero_atacado=[]
    for x in range(8):
        aux =[]
        for y in range(8):
            try:
                objeto.posiciones.index([x,y])
                aux.append(1)
            except ValueError:
                aux.append(0)
        tablero_atacado.append(aux)
    for x in tablero_atacado:
        print x

def main():
    opcion = menu(['torre','caballo','alfil','reina','rey'], 'selecione cual pieza quiere usar')
    tablero = [[0 for y in range(8)] for x in range(8)]
    print ['torre','caballo','alfil','reina','rey'][opcion-1]
    objeto = {
        1: Torre(tablero),
        2: Caballo(tablero),
        3: Alfil(tablero),
        4: Reina(tablero),
        5: Rey(tablero)
    }.get(opcion, lambda: "Invalid")
    algoritmo(objeto,tablero)
main()
class Gen:
    def __init__(self,cromosoma):
        self.cromosoma = cromosoma
        self.valor = self.sacarValor()
    def sacarValor(self):
        suma = 0
        for x in range(len(self.cromosoma)):
            for y in range(len(self.cromosoma[x])-1):
                suma += 1 if(self.cromosoma[x][y] == '1') else -1
                suma += 1 if(self.cromosoma[x][y] == '1' and self.cromosoma[x][y+1] == '1') else 0
                suma += -1 if(self.cromosoma[x][y] == '0' and self.cromosoma[x][y+1] == '0') else 0
            suma+= 1 if( self.cromosoma[x][len(self.cromosoma[x])-1]== '1') else -1 
            if not(self.cromosoma[x].count('1') == self.cromosoma[x].count('0')):
                suma += 1 if(self.cromosoma[x].count('1')> self.cromosoma[x].count('0'))else -1
        return suma
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
                        aux.append(suma)
                        suma = ""
            if(len(aux)>0):
                i += 1
                datos.append(aux)
                aux = []
        return datos
    except ValueError:
        print('format error')
        return

datos = LeerDatos('./datos/geneticos.txt')
genes = []
print('datos',datos)
for x in datos:
    genes.append(Gen(x))
print genes[1].valor
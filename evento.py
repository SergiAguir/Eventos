import random

class Evento:
    def __init__(self,nEvento,fecha,localidad,provincia,precioI):
        self.nEvento = nEvento
        self.fecha = fecha
        self.localidad = localidad
        self.provincia = provincia
        self.precioI = precioI
        self.total = 0
        self.participantes = []
        self.finalizado = False
        self.podium = {"PRIMERO":0,
                       "SEGUNDO":0,
                       "TERCERO":0}

    def getNEvento(self):
        return self.nEvento

    def getFecha(self):
        return self.fecha

    def getLocalidad(self):
        return self.localidad

    def getProvincia(self):
        return self.provincia

    def getPrecioI(self):
        return self.precioI

    def getTotal(self):
        return self.total

    def getFinalizado(self):
        return self.finalizado


    def anyadirParticipante(self,dni,nombre,edad):
        self.participantes.append((dni,nombre,edad))
        self.total+= self.precioI
        return True

    def mostrarParticipantes(self):
        lista = ""
        for i in self.participantes:
            lista += "DNI: "+i[0]+" Nombre: "+ i[1]+" Edad: "+str(i[2])+"\n"
        return lista

    def finalizarEvento(self):
        for i in self.podium:
            self.podium[i] = random.choice(self.participantes)
        self.finalizado = True

    def mostrarPodium(self):
        lista = ""
        for clave,valor in self.podium.items():
            lista += str(clave)+"\n"+str(valor)+"\n"
        return lista
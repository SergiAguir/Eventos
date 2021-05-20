from evento import Evento

class Controlador:
    def __init__(self):
        self.listaEventos = {}

    def getNumEventos(self):
        return len(self.listaEventos)


    def anyadirEvento(self,evento):
        if evento.getNEvento() not in self.listaEventos:
            self.listaEventos[evento.getNEvento()] = evento
            return True
        else:
            return False
    
    def _check_dni(self,dni):
        letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        
        letraDNI = dni[-1].upper()
        numDNI = dni[:-1]

        if (letraDNI.isalpha() == False):
            return False
        if len(dni) != 9:
            return False
        else:
            letraCalculada = letras[int(numDNI)%23]
            if (letraDNI != letraCalculada):
                return False
        return True

    def comEvento(self,nEvento):
        if nEvento in self.listaEventos:
            return True
        return False

    def anyadirParticipante(self,nEvento,dni,nombre,edad):
        if self.listaEventos[nEvento].anyadirParticipante(dni,nombre,edad):
            return True
        else:
            return False

    def mostrarEventos(self):
        lista = []
        for clave,valor in self.listaEventos.items():
            if valor.getFinalizado() == False:
                lista.append("Nombre del Evento: "+str(clave)+"\n Fecha: "+str(valor.getFecha())+"\n Localidad: "+valor.getLocalidad()+"\n Provincia: "+valor.getProvincia()+"\n Precio Inscripcion: "+str(valor.getPrecioI())+"\n Total Recaudado: "+str(valor.getTotal()))
        return lista


    def mostrarEventosParticipantes(self):
        lista = []
        for clave,valor in self.listaEventos.items():
            if valor.getFinalizado() == False:
                lista.append("Nombre del Evento: "+str(clave)+"\n Fecha: "+str(valor.getFecha())+"\n Localidad: "+valor.getLocalidad()+"\n Provincia: "+valor.getProvincia()+"\n Precio Inscripcion: "+str(valor.getPrecioI())+"\n Total Recaudado: "+str(valor.getTotal())+"\n Participantes: "+valor.mostrarParticipantes())
        return lista


    def mostrarEventosPodium(self):
        lista = []
        for clave,valor in self.listaEventos.items():
            if valor.getFinalizado() == True:
                lista.append("Nombre del Evento: "+str(clave)+"\n Fecha: "+str(valor.getFecha())+"\n Localidad: "+valor.getLocalidad()+"\n Provincia: "+valor.getProvincia()+"\n Precio Inscripcion: "+str(valor.getPrecioI())+"\n Total Recaudado: "+str(valor.getTotal())+"\n Participantes: "+valor.mostrarParticipantes()+"\n Podium: "+valor.mostrarPodium()+"\n")
        return lista


    def finalizarEvento(self,nEvento):
        if nEvento in self.listaEventos:
            self.listaEventos[nEvento].finalizarEvento()
            return True
        return False
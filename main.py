from evento import Evento
from controlador import Controlador
from datetime import datetime

con = Controlador()

while True:
    print("El numero de eventos es ",con.getNumEventos())
    print("1.- Anyadir evento")
    print("2.- Anyadir participante a evento")
    print("3.- Listar eventos pendientes de realizar sin participantes")
    print("4.- Listar eventos pendientes de realizar con participantes")
    print("5.- Listar eventos acabados con podium")
    print("6.- Finalizar un evento")
    print("7.- Salir")


    op = int(input("Elige una opcion: "))

    if op == 1:
        while True:
            nombre = input("Cual es el nombre del evento: ")
            
            if nombre == "":
                print("El nombre no puede estar en blanco!!")
            else:
                break

        while True:
            fecha = datetime.now()
            fechaForm = fecha.strftime("%d/%m/%Y %H:%M")
            print("--------------")
            print("Fecha anyadida")
            print("--------------")
            break

        while True:
            localidad = input("Introduce la localidad: ")

            if localidad == "":
                print("La localidad no puede estar en blanco!!")
            else:
                break

        while True:
            provincia = input("Introduce la provincia: ")

            if provincia == "":
                print("La provincia no puede estar en blanco!!")
            else:
                break

        while True:
            try:
                precioI = int(input("Introduce el precio de la inscripcion: "))

                if precioI <= 0:
                    print("El precio de la inscripcion no puede ser 0 o menor que 0")
                else:
                    break
            except ValueError:
                print("El precio es un numero!!")

        evento = Evento(nombre,fecha,localidad,provincia,precioI)

        if con.anyadirEvento(evento):
            print("El evento se ha anyadido correctamente!!")
        else:
            print("Error al anyadir el evento!!")

    if op == 2:
        while True:
            nEvento = str(input("Introduce le nombre del evento: "))

            if con.comEvento(nEvento)== False:
                print("El evento introducido no existe!!")
            else:
                break


        while True:
            dni = str(input("Introduce el DNI del participante: "))

            if con._check_dni(dni) == False:
                print("Error el DNI introducido no es correcto!!")
            
            else:
                break

        while True:
            nombre = str(input("Introduce el nombre del participante: "))

            if nombre == "":
                print("Error el nombre no puede estar en blanco!!")
            else:
                break

        while True:
            edad = int(input("Introduce la edad del participante: "))

            if edad <18:
                print("El participante tiene que tener 18 anyos o mas para participar!!")
            else:
                break

        if con.anyadirParticipante(nEvento,dni,nombre,edad):
            print("Participante anyadido correctamente!!")
        else:
            print("Error al anyadir el paciente")

    if op == 3:
        for i in con.mostrarEventos():
            print(i)
            
    if op == 4:
        for i in con.mostrarEventosParticipantes():
            print(i)

    if op == 5:
        for i in con.mostrarEventosPodium():
            print(i)

    if op == 6:
        nEvento = str(input("Introduce el nombre del evento a finalizar: "))

        if con.finalizarEvento(nEvento):
            print("Evento finalizado correctamente")
        else:
            print("Error al finalizar el evento")

    if op == 7:
        print("Adios!!!")
        break
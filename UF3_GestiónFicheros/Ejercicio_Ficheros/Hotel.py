#En este módulo implemento las funciones que podrá realizar el Hotel

import fileManager as file

HAB_DISPONIBLE = "DISPONIBLE"
HAB_OCUPADA = "OCUPADA"
HAB_SUCIA = "SUCIA"

'''Esta función recibe como argumentos el número de la habitación, la capacidad y el precio
y, si no estaba registrada previamente la registra en la base de datos del hotel'''
def anyadirHabitacion(numHab, capacidad, precio):
    habitaciones = file.getDataHabitaciones()
    if numHab not in habitaciones:
        file.escribirHabitaciones(numHab, capacidad, precio, HAB_DISPONIBLE)
        print("Habitación registrada correctamente")
    else:
        print(f"El número de habitación '{numHab}' ya está registrado en la base de datos")

'''Esta función recibe como argumentos el número de la habitación y el nombre, apellido, dni y teléfono de
un cliente. Si la habitación está disponible y se encuentra en la base de datos del hotel, se ejecutará la reserva'''
def anyadirReserva(numHab, nombre, apellido, dni, tlf):
    habitaciones = file.getDataHabitaciones()
    if len(habitaciones) == 0:
        print("No hay ninguna habitación registrada")
    elif numHab not in habitaciones:
        print(f"La habitación con el número '{numHab}' no se encuentra en la base de datos")
    elif habEstado(numHab, HAB_DISPONIBLE):
        lineas = file.cambiarEstadoFile(numHab, HAB_OCUPADA)
        file.actualizarHabitacionesFile(lineas)
        file.escribirReservas(numHab, nombre, apellido, dni, tlf)
        print("Reserva registrada correctamente")

'''Esta función lista todas las reservas que se han realizado'''
def reservasList():
    reservas = file.getDataReservas()
    if len(reservas) == 0:
        print("No hay ninguna reserva hecha")
    else:
        print("===========      RESERVAS      ===========")
        for numhab, data in reservas.items():
            print(f"{numhab} : {data[file.DNI]} - {data[file.NOMBRE]} {data[file.APELLIDO]} - {data[file.TELEF]}")
        print(f"==========================================")

'''Esta función lista todas las habitaciones que se encuentra en la base de datos del hotel.
También muestra la cantidad total de habitaciones, las habitaciones disponibles, sucias y ocupadas'''
def habList():
    habitaciones = file.getDataHabitaciones()
    if len(habitaciones) == 0:
        print("No hay ninguna habitación registrada")
    else:
        contadorHab = 0
        habOcupadas = 0
        habDisponibles = 0
        print("===============        INFO HOTEL        ===============\n"
              "HAB\t\tCAP\t\tESTADO\n"
              "--------------------------------------------------------")
        for numhab, data in habitaciones.items():
            print(f"{numhab}\t\t{data[file.CAPACIDAD]}\t\t{data[file.ESTADO]}", end="\t")
            if data[file.ESTADO] == HAB_OCUPADA:
                reservas = file.getDataReservas()
                print(f"\t=> Cliente: {reservas[numhab][file.NOMBRE]} {reservas[numhab][file.APELLIDO]}")
                habOcupadas += 1
            else:
                print()
                if data[file.ESTADO] == HAB_DISPONIBLE:
                    habDisponibles += 1
            contadorHab += 1

        print("========================================================\n"
              f"Total habitaciones: {contadorHab}\n"
              f"Disponibles: {habDisponibles}\tOcupadas: {habOcupadas}\tSucias: {contadorHab - (habDisponibles+habOcupadas)}\n"
              f"-------------------------------------------------------")

'''Esta función recibe como argumento un DNI y mostrará todas las reservas que tenga el cliente del mismo'''
def infoCliente(dni):
    reservas = file.getDataReservas()
    clienteReservas = 0
    if len(reservas) == 0:
        print("No hay ninguna reserva registrada")
    else:
        for numhab, data in reservas.items():
            if data[file.DNI] == dni:
                clienteReservas += 1
                if clienteReservas == 1:
                    print(f"Datos del Cliente:\t{data[file.APELLIDO]} , {data[file.NOMBRE]} - Tfn: {data[file.TELEF]}")
                    print(f"Habitación:  {numhab}")

        if clienteReservas == 0:
            print(f"El cliente con dni '{dni}' no tiene ninguna reserva")

'''Esta función recibe un número de habitación y el número de días de estancia. Si hay habitaciones Ocupadas 
(y está en la base de datos del hotel) se finalizará la reserva y se mostrará el precio total a pagar. El precio será 0 si el cliento ha estado
menos de 1 día en el hotel (o por cancelarse)'''
def finalizar(numHab, numDias):
    habitaciones = file.getDataHabitaciones()
    if len(habitaciones) == 0:
        print("No hay habitaciones registradas")
    else:
        if numHab in habitaciones:
            if habEstado(numHab, HAB_OCUPADA):
                habitaciones = file.getDataHabitaciones()
                precioHab = habitaciones[numHab][file.PRECIO]
                precioEstancia = float(precioHab)*int(numDias)
                reservas = file.getDataReservas()
                if precioEstancia != 0:
                    print(f"Precio total: {precioEstancia:.2f} €. La habitación queda en espera del servicio de limpieza")
                    reservas.pop(numHab)
                    file.actualizarReservasFile(reservas)
                    lineas = file.cambiarEstadoFile(numHab, HAB_SUCIA)
                    file.actualizarHabitacionesFile(lineas)

                else:
                    print("Reserva anulada sin ningún coste. La habitación ahora esta disponible")
                    reservas.pop(numHab)
                    file.actualizarReservasFile(reservas)
                    lineas = file.cambiarEstadoFile(numHab, HAB_DISPONIBLE)
                    file.actualizarHabitacionesFile(lineas)

        else:
            print(f"La habitación con el número '{numHab}' no se encuentra en la base de datos")

'''Esta función recibe el número de una habitación como argumento. Si la habitación existe y está en estado
'SUCIA, el personal de limpizar procederá a limpiarla'''
def limpiar(numHab):
    habitaciones = file.getDataHabitaciones()
    if len(habitaciones) == 0:
        print("No hay habitaciones registradas")
    else:
        if numHab in habitaciones:
            if habEstado(numHab, HAB_SUCIA):
                lineas = file.cambiarEstadoFile(numHab, HAB_DISPONIBLE)
                file.actualizarHabitacionesFile(lineas)
                print(f"La habitación '{numHab}' se ha limpiado correctamente")
        else:
            print(f"La habitación {numHab} no está registrada")

'''Esta función recibe como argumento el número de habitación y el estado de la misma.
Si la habitación se encuentra en la base de datos del hotel comprueba si el estado de la habitación
coincide con el estado que se le envia por argumento. Si coincide devuelve True, si no, devuelve False'''
def habEstado(numHab, estado):
    coincideEstado = False
    habitaciones = file.getDataHabitaciones()
    if habitaciones[numHab][file.ESTADO] == estado:
        coincideEstado = True
    else:
        print(f"La habitación '{numHab}' no está {estado.lower()}")

    return coincideEstado





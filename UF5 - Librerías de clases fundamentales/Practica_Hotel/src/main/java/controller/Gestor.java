package controller;

import enums.EstadoHabitacion;
import exceptions.ComandaException;
import models.Cliente;
import models.Habitacion;
import models.Persona;
import models.Trabajador;
import utils.ColorTexto;

import java.util.*;

public class Gestor {

    private static int money = 1000;
    private HashMap<String, Habitacion> habitaciones = new HashMap<>();
    private HashMap<String, Persona> personas = new HashMap<>();


    public void addRoom(String num, int capacidad, HashSet<String> servicios) throws ComandaException {

        if(!habitaciones.containsKey(num)){
            Habitacion habitacion = new Habitacion(num, capacidad, servicios);
            habitaciones.put(num, habitacion);
            System.out.println(ColorTexto.BLUE + "--> Nueva habitación registrada " +num+ " <--" + ColorTexto.RESET);
        }else{
            throw new ComandaException(ComandaException.HABITACION_EXISTENTE_EXCEPTION);
        }
    }

    public void addWorker(String dni, String nombre, HashSet<String> habilidades) throws ComandaException{
        if(!buscarTrabajador(dni)){
            personas.put(dni, new Trabajador(dni, nombre, habilidades));
            System.out.println(ColorTexto.BLUE + "--> Nuevo trabajador registrado " + dni + " <--" + ColorTexto.RESET);
        }else{
            throw new ComandaException(ComandaException.TRABAJADOR_EXISTENTE_EXCEPTION);
        }
    }

    public void addReserva(String dni, int numPersonas, HashSet<String> requisitos) throws ComandaException {

        if (!(personas.get(dni) instanceof Trabajador)) {
            if(!habitaciones.isEmpty()){
                Cliente c;
                String info;
                Habitacion hab = buscarCapacidadAjustada(numPersonas, requisitos);

                if(hab!=null){
                    c = new Cliente(dni, numPersonas, requisitos);
                    info = "--> Cliente " + dni + " asignado a la habitacion " + hab.getNum() + " <--";
                    hab.cambiarEstado(EstadoHabitacion.RESERVED.name());
                    hab.asignarCliente(c);
                    System.out.println(ColorTexto.BLUE + info + ColorTexto.RESET);
                }else{
                    money -= 100;
                    throw new ComandaException(ComandaException.HABITACION_REQUISITOS_EXCEPTION);
                }

            }else{
                throw new ComandaException(ComandaException.NO_HABITACIONES_REGISTRADAS);
            }

        } else {
            throw new ComandaException(ComandaException.DNI_TRABAJADOR);
        }
    }

    public Habitacion buscarCapacidadAjustada(int capacidad, HashSet<String> requisitos){
        int auxCapacidad = -1;
        int contador = 0;
        Habitacion habitacionElegida = new Habitacion();
        int i = 0;
        for(Map.Entry<String, Habitacion> h: habitaciones.entrySet()){
            Habitacion habitacion = h.getValue();
            if(habitacion.getEstado().equalsIgnoreCase(EstadoHabitacion.CLEAN.name())){
                if(habitacion.getCapacidad() >= capacidad){
                    if(comprobarRequisitos(habitacion, requisitos)){
                        contador = 1;
                        if(i==0){
                            auxCapacidad = habitacion.getCapacidad();
                            habitacionElegida = habitacion;
                            i = 1;
                        }else{
                            if(habitacion.getCapacidad() < auxCapacidad){
                                auxCapacidad = habitacion.getCapacidad();
                                habitacionElegida = h.getValue();
                            }
                        }
                    }
                }
            }
        }
        if(contador == 0){
            habitacionElegida = null;
        }

        return habitacionElegida;
    }

    public boolean comprobarRequisitos(Habitacion habitacion, HashSet<String> requisitos){
        boolean serviciosValidos = true;
        for(String r: requisitos){
            if(!habitacion.getServicios().contains(r)){
                serviciosValidos = false;
            }
        }
        return serviciosValidos;

    }

    public void mostrarHotel(){
        System.out.println(ColorTexto.PURPLE + "==> ROOMS <==" );
        for(Map.Entry<String, Habitacion> h: habitaciones.entrySet()){
            System.out.println("== " + h.getValue() + " ==");
        }
        System.out.println("============================================");
        System.out.println(ColorTexto.PURPLE + "==> WORKERS <==");
        for(Map.Entry<String, Persona> p: personas.entrySet()){
            if(p.getValue() instanceof Trabajador trabajador){
                System.out.println("== " + trabajador + " ==");
            }
        }
        System.out.print(ColorTexto.RESET);
    }

    public void problemas(String habitacion) throws ComandaException{

        if(habitaciones.containsKey(habitacion)){
            Habitacion h = habitaciones.get(habitacion);
            System.out.println(ColorTexto.BLUE + "--> El estado de la habitación ha cambiado a BROKEN <--" + ColorTexto.RESET);
            if(h.getEstado().equalsIgnoreCase(EstadoHabitacion.RESERVED.name())) {
                Cliente cliente = h.getCliente();
                h.asignarCliente(new Cliente());
                h.cambiarEstado(EstadoHabitacion.BROKEN.name());
                addReserva(cliente.getDni(), cliente.getCapacidad(), cliente.getRequisitos());
            }
            h.cambiarEstado(EstadoHabitacion.BROKEN.name());
        }else{
            throw new ComandaException(ComandaException.HABITACION_NO_EXISTE_EXCEPTION);
        }
    }

    public void peticion(String numHab, HashSet<String> peticiones) throws ComandaException{
        if(habitaciones.containsKey(numHab)){
            int contador = 0;
            Habitacion hab = habitaciones.get(numHab);

                for (String p : peticiones) {
                    boolean peticionPendiente = true;
                    for (Map.Entry<String, Persona> per : personas.entrySet()) {
                        if (per.getValue() instanceof Trabajador) {
                            contador = 1;
                            Trabajador trabajador = (Trabajador) per.getValue();
                            if (trabajador.isEstaDisponible()) {
                                HashSet<String> habilidades = trabajador.getHabilidades();
                                if(peticionPendiente){
                                    for (String h : habilidades) {
                                        if (h.equalsIgnoreCase(p)) {
                                            peticionPendiente = false;
                                            trabajador.asignarHabitacion(hab);
                                            trabajador.cambiarDisponibilidad();
                                            hab.addPeticion(p, peticionPendiente);
                                            System.out.println(ColorTexto.BLUE + "--> Trabajador " + trabajador.getNombre() +" asignado a la habitacion " + hab.getNum() + ColorTexto.RESET);
                                        }
                                    }
                                }
                            }
                        }
                    }if (contador == 0){
                        throw new ComandaException(ComandaException.NO_TRABAJADORES_REGISTRADOS);
                    }
                    if (peticionPendiente) {
                        hab.addPeticion(p, peticionPendiente);
                        System.out.println(ColorTexto.BLUE + "--> Ningún trabajador disponible para este servicio. Servicio pendiente <--" + ColorTexto.RESET);
                    }
                }
            }
        else{
            throw new ComandaException(ComandaException.HABITACION_NO_EXISTE_EXCEPTION);
        }
    }

    public void finish(String numHab) throws ComandaException{
        if(habitaciones.containsKey(numHab)){
            Habitacion habitacion = habitaciones.get(numHab);
            boolean hayServicios = false;
            for(Map.Entry<String, Persona> persona: personas.entrySet()) {
                if (persona.getValue() instanceof Trabajador trabajador) {
                    if(trabajador.getHab()!= null){
                        if (trabajador.getHab().getNum().equalsIgnoreCase(habitacion.getNum())) {
                            hayServicios = true;
                            trabajador.cambiarDisponibilidad();
                            habitacion.eliminarPeticiones();
                            if (habitacion.getCliente().getDni() == null) {
                                habitacion.cambiarEstado(EstadoHabitacion.CLEAN.name());
                            } else {
                                habitacion.cambiarEstado(EstadoHabitacion.RESERVED.name());
                            }
                        }
                    }
                }

            } if (!hayServicios) {
                System.out.println(ColorTexto.BLUE + "--> Ningún trabajador asignado a esta habitación <--" + ColorTexto.RESET);
            }else{
                System.out.println(ColorTexto.BLUE + "--> Servicios completados en la habitación: " + habitacion.getNum() + " <--" + ColorTexto.RESET);
            }
        } else{
            throw new ComandaException(ComandaException.HABITACION_NO_EXISTE_EXCEPTION);
        }
    }

    public void leave(String numHab, int precio) throws ComandaException{
        if(habitaciones.containsKey(numHab)){
            Habitacion habitacion = habitaciones.get(numHab);
            String info;
            if(habitacion.getCliente().getDni() != null){
                boolean clienteSatisfecho = true;
                habitacion.cambiarEstado(EstadoHabitacion.UNCLEAN.name());
                for(Map.Entry<String, Persona> persona: personas.entrySet()){
                    if(persona.getValue() instanceof Trabajador trabajador){
                        if (trabajador.getHab() != null){
                            if(trabajador.getHab().getNum().equalsIgnoreCase(habitacion.getNum())){
                                trabajador.cambiarDisponibilidad();
                                for(Map.Entry<String, Boolean> p: habitacion.getRequests().entrySet()){
                                    if(p.getValue()){
                                        clienteSatisfecho = false;
                                    }
                                }
                            }
                        }
                    }
                }
                if(!clienteSatisfecho){
                    money -= precio/2;
                    info = "--> Habitación " + habitacion.getNum() + " libre y cambia a estado SUCIA <--\n" +
                            "--> Clientes insatisfechos. Pierdes " + precio/2 + "$ <--";
                }else{
                    money += precio;
                    info = "--> Habitación " + habitacion.getNum() + " libre y cambia a estado SUCIA <--\n" +
                            "--> Clientes satisfechos. Ganas " + precio + "$ <--";
                }
                System.out.println(ColorTexto.BLUE + info + ColorTexto.RESET);
            }else{
                throw new ComandaException(ComandaException.HABITACION_NO_RESERVADA);
            }
        }else{
            throw new ComandaException(ComandaException.HABITACION_NO_EXISTE_EXCEPTION);
        }
    }
    public void mostrarMoney(){
        System.out.println(ColorTexto.PURPLE + "==========================================\n" +
                "==>   Money: " + money + "$   <==\n" +
                "==========================================" + ColorTexto.RESET);
    }
    public int getMoney() {
        return this.money;
    }

    public void quiebra(){
        System.out.println(ColorTexto.PURPLE + "===========================================\n" +
                "===      HAS PERDIDO TOD EL DINERO      ===\n" +
                "===========================================" + ColorTexto.RESET);
    }

    private boolean buscarTrabajador(String dni){
        boolean trabajadorExiste = false;
        if(personas.containsKey(dni)){
            if(personas.get(dni) instanceof Trabajador){
                trabajadorExiste = true;
            }
        }
        return trabajadorExiste;

    }
}

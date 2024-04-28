package models;

import enums.EstadoHabitacion;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class Habitacion implements Comparable{

    private String num;
    private int capacidad;
    private String estado;
    private HashSet<String> servicios;
    private HashMap<String, Boolean> requests;
    //private Trabajador trabajador;
    private Cliente c;

    public Habitacion(){}
    public Habitacion(String num, int capacidad, HashSet<String> servicios) {
        this.num = num;
        this.capacidad = capacidad;
        this.servicios = servicios;
        this.estado = EstadoHabitacion.CLEAN.name();
        this.c = new Cliente();
        this.requests = new HashMap<>();
        //this.trabajador = new Trabajador();

    }

    public void addPeticion(String peticion, boolean estaPendiente){
        this.requests.put(peticion, estaPendiente);
    }

    public void cambiarEstado(String estado){
        this.estado = estado;
    }

    public void asignarCliente(Cliente c){
        this.c = c;
    }

    /*public void asignarTrabajador(Trabajador trabajador){
        this.trabajador = trabajador;
    }*/

    public void eliminarPeticiones(){
        this.requests.clear();
    }

    public String getNum() {
        return num;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public HashSet<String> getServicios() {
        return servicios;
    }

    public String getEstado() {
        return estado;
    }

    public Cliente getCliente() {
        return c;
    }

    public HashMap<String, Boolean> getRequests() {
        return requests;
    }

    /*public Trabajador getTrabajador() {
        return trabajador;
    }*/

    @Override
    public int compareTo(Object o) {
        Habitacion h = (Habitacion) o;
        return this.capacidad - h.getCapacidad();
    }

    @Override
    public String toString() {
        String info;
        if(this.estado.equalsIgnoreCase(EstadoHabitacion.RESERVED.name())){
            info = "ROOM " + this.num + " Cliente: " + this.c.getDni() + "("+this.capacidad+")";
        }else{
            info = "ROOM "+ this.num + " " + this.estado;
        }
        return info;
    }
}

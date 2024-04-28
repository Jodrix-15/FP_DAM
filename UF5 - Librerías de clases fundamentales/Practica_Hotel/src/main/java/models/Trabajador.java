package models;

import java.util.HashSet;

public class Trabajador extends Persona{
    private String nombre;
    private HashSet<String> habilidades;
    private boolean estaDisponible;

    private Habitacion hab;


    public Trabajador(String dni, String nombre, HashSet<String> habilidades) {
        super(dni);
        this.nombre = nombre;
        this.habilidades = habilidades;
        this.estaDisponible = true;
        this.hab =  null;
    }

    public Trabajador(){
        super();
    }

    public void cambiarDisponibilidad(){
        this.estaDisponible = !this.estaDisponible;
    }



    public String getNombre() {
        return nombre;
    }

    public HashSet<String> getHabilidades() {
        return habilidades;
    }



    public boolean isEstaDisponible() {
        return estaDisponible;
    }

    public void asignarHabitacion(Habitacion hab){
        this.hab = hab;
    }

    public Habitacion getHab() {
        return hab;
    }

    @Override
    public String toString() {
        String disponibilidad;
        if(this.estaDisponible){
            disponibilidad = "AVAILABLE";
        }else{
            disponibilidad = "ROOM: " + this.hab.getNum();
        }
        return "WORKER "+ super.toString() + " " + this.nombre + " " +disponibilidad;
    }
}

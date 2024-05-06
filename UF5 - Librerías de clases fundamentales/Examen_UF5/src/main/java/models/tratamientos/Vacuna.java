package models.tratamientos;

import enums.Tratamientos;
import models.Trabajador;

public class Vacuna extends Tratamiento{

    private String nombre;
    private double precio;
    private boolean primeraVez;


    public Vacuna(Trabajador trabajador, String nombre, boolean primeraVez) {
        super(trabajador);
        this.nombre = nombre;
        this.primeraVez = primeraVez;
    }


    @Override
    public double calcularPreu() {
        if(!primeraVez){
            this.precio = 29.95;
        }else{
            this.precio = 50;
        }
        return this.precio;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }


    @Override
    public String toString() {
        return super.toString() + " - Tipus: " + Tratamientos.VACUNA + " - Precio: " + this.precio + "€";
    }
}

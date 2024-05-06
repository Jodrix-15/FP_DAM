package models.tratamientos;

import enums.Tratamientos;
import models.Trabajador;

public class Revision extends Tratamiento{
    private boolean esPajaro;
    private String descripcionMascota;

    public Revision(Trabajador trabajador, boolean esPajaro, String descripcionMascota) {
        super(trabajador);
        this.esPajaro = esPajaro;
        this.descripcionMascota = descripcionMascota;
    }

    @Override
    public double calcularPreu() {
        if(esPajaro){
            this.precio = 25;
        }else{
            this.precio = 30;
        }
        return this.precio;
    }

    @Override
    public String toString() {
        return super.toString() + " - Tipus: " + Tratamientos.REVISIO + " - Precio: " + this.precio + "€";
    }
}

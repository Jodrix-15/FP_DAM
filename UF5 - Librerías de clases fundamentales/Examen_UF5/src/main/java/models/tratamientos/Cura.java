package models.tratamientos;

import enums.Tratamientos;
import models.Trabajador;

public class Cura extends Tratamiento{
    private boolean huesoRoto;

    public Cura(Trabajador trabajador, boolean huesoRoto) {
        super(trabajador);
        this.huesoRoto = huesoRoto;
    }

    @Override
    public double calcularPreu() {
        this.precio = 35.25;
        if(huesoRoto){
            this.precio += 51.50;
        }
        return this.precio;
    }

    @Override
    public String toString() {
        return super.toString() + " - Tipus: " + Tratamientos.CURA + " - Precio: " + this.precio + "€";
    }
}

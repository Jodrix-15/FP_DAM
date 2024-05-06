package models.tratamientos;

import models.Trabajador;

public abstract class Tratamiento {

    protected Trabajador trabajador;
    protected static int codigo = 0;
    protected int codTratamiento;
    protected double precio;


    public Tratamiento(Trabajador trabajador) {
        this.trabajador = trabajador;
        this.precio = 0;
        this.codTratamiento = codigo + 1;
        codigo++;
    }

    public abstract double calcularPreu();

    public int getCodTratamiento() {
        return codTratamiento;
    }

    @Override
    public String toString() {
        return "Código: " + this.codTratamiento + " - Trabjador: " + this.trabajador;
    }
}

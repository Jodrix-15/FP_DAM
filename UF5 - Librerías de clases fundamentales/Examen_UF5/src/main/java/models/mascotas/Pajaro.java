package models.mascotas;

import models.mascotas.Animal;
import models.tratamientos.Tratamiento;

import java.util.HashMap;

public abstract class Pajaro extends Animal {

    protected int horasLibresDia;

    public Pajaro(String nombre, boolean esMacho, int edad, int horasLibresDia) {
        super(nombre, edad, esMacho);
        this.horasLibresDia = horasLibresDia;
    }

    public int getHorasLibresDia() {
        return horasLibresDia;
    }
    public abstract String getExpedient();


}

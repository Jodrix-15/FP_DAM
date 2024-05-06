package models.mascotas;

import enums.TipoAnimal;
import models.tratamientos.*;

import java.util.ArrayList;

public abstract class Animal {

    protected String nombre;
    protected int edad;
    protected boolean esMacho;



    public Animal(String nombre, int edad, boolean esMacho) {
        this.nombre = nombre;
        this.edad = edad;

        this.esMacho = esMacho;
    }



    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public abstract String getExpedient();
}

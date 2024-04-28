package models;

import java.util.Objects;

public class Persona {

    protected String dni;

    public Persona(){
        dni = null;
    }
    public Persona(String dni) {
        this.dni = dni;
    }

    public String getDni() {
        return dni;
    }

    @Override
    public String toString() {
        return dni;
    }


}

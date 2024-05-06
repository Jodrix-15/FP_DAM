package models;

import enums.EspecialidadTrabajador;

import java.util.HashSet;

public class Trabajador {
    private String dni;
    private String nombre;
    private String apellidos;
    private String numTelef;
    private HashSet<EspecialidadTrabajador> especialidades;

    public Trabajador(String dni, String nombre, String apellidos, String numTelef, HashSet<EspecialidadTrabajador> especialidades) {
        this.dni = dni;
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.numTelef = numTelef;
        this.especialidades = especialidades;
    }

    public String getDni() {
        return dni;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public String getNumTelef() {
        return numTelef;
    }

    public HashSet<EspecialidadTrabajador> getEspecialidades() {
        return especialidades;
    }

    @Override
    public String toString() {
        return this.nombre + " " + this.apellidos;
    }
}

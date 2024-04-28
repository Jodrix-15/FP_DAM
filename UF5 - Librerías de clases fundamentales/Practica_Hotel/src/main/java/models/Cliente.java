package models;

import exceptions.ComandaException;

import java.util.HashSet;

public class Cliente extends Persona{


    private HashSet<String> requisitos;
    private int capacidad;

    public Cliente(){
        super();
    }

    public Cliente(String dni, int capacidad, HashSet<String> requisitos) {
        super(dni);
        this.capacidad = capacidad;
        this.requisitos = requisitos;

    }



    public int getCapacidad() {
        return capacidad;
    }

    public HashSet<String> getRequisitos() {
        return requisitos;
    }

    @Override
    public boolean equals(Object obj) {
        boolean esIgual = false;
        if (obj instanceof Cliente) {
            Cliente cliente = (Cliente) obj;
            if (this.dni.equalsIgnoreCase(cliente.dni)) {
                esIgual = true;
            }
        }
        return esIgual;
    }
}

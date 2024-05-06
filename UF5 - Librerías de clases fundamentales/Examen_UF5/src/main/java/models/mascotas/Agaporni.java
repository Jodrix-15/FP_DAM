package models.mascotas;

import enums.TipoAnimal;
import models.tratamientos.*;

import java.util.HashMap;

public class Agaporni extends Pajaro {

    private double altura;
    private HashMap<Integer, Tratamiento> tratamientos;

    public Agaporni(String nombre, boolean esMacho, int edad, int horasLibresDia, double altura) {
        super(nombre, esMacho, edad, horasLibresDia);
        this.altura = altura;
        this.tratamientos = new HashMap<>();

    }

    public double getAlturaMax() {
        return altura;
    }

    public HashMap<Integer, Tratamiento> getTratamientos() {
        return tratamientos;
    }

    public void addTratamiento(Tratamiento tratamiento){
        tratamientos.put(tratamiento.getCodTratamiento(), tratamiento);
    }

    public String getExpedient(){
        String genero;
        String info;
        if(this.esMacho){
            genero = "M";
        }else{
            genero = "F";
        }
        info = "Edad: " + this.edad + " Genero: " + genero +"\n"+
                "------------------------------------------------\n";
        if(tratamientos.isEmpty()){
            info += "* No hay ningún tratamiento * \n";
        }else{
            info += "Tratamientos: \n";
            for(Tratamiento t: tratamientos.values()){
                if(t instanceof Peluqueria peluqueria){
                    info += peluqueria + "\n";
                }else if( t instanceof Revision revision){
                    info += revision + "\n";
                }
                else if( t instanceof Cura cura){
                    info += cura + "\n";
                }
                else if( t instanceof Vacuna vacuna){
                    info += vacuna + "\n";
                }
            }
        }
        info += "------------------------------------------------\n";
        info = info + "Especie: " + TipoAnimal.AGAPORNI + " - Horas libres al dia: " + this.horasLibresDia + " - Altura: " + this.altura + "cm";
        return info;

    }
}

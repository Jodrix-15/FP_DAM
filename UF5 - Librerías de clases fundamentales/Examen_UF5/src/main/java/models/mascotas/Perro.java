package models.mascotas;

import enums.GrandariaPelo;
import enums.TipoAnimal;
import models.tratamientos.*;

import java.util.HashMap;

public class Perro extends Animal{

    private boolean peloLargo;
    private GrandariaPelo grandaria;
    private HashMap<Integer, Tratamiento> tratamientos;

    public Perro(String nombre, boolean esMacho, int edad, boolean peloLargo, GrandariaPelo grandaria) {
        super(nombre, edad, esMacho);
        this.peloLargo = peloLargo;
        this.grandaria = grandaria;
        this.tratamientos = new HashMap<>();
    }

    public boolean isPeloLargo() {
        return peloLargo;
    }

    public GrandariaPelo getGrandaria() {
        return grandaria;
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
        String pelo;
        if(this.esMacho){
            genero = "M";
        }else{
            genero = "F";
        }
        if(this.peloLargo){
            pelo = "SI";
        }else{
            pelo = "NO";
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

        info = info + "Especie: " + TipoAnimal.GOS + " - Grandaria: " + this.grandaria + " - Pelo Largo: " + pelo;
        return info;

    }
}

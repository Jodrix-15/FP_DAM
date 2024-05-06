package models.mascotas;

import enums.TipoAnimal;
import models.tratamientos.*;

import java.util.HashMap;

public class Loro extends Pajaro {

    private boolean habla;
    private boolean silva;
    private HashMap<Integer, Tratamiento> tratamientos;

    public Loro(String nombre, boolean esMacho, int edad, int horasLibresDia, boolean habla, boolean silva) {
        super(nombre, esMacho, edad, horasLibresDia);
        this.habla = habla;
        this.silva = silva;
        this.tratamientos = new HashMap<>();
    }

    public boolean isHabla() {
        return habla;
    }

    public boolean isSilva() {
        return silva;
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
        String habla;
        String silva;
        if(this.esMacho){
            genero = "M";
        }else{
            genero = "F";
        }
        if(this.habla){
            habla = "SI";
        }else{
            habla = "NO";
        }
        if(this.silva){
            silva = "SI";
        }else{
            silva = "NO";
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

        info = info + "Especie: " + TipoAnimal.LLORO + " - Horas libres al dia: " + this.horasLibresDia + " - Silva: " + silva + " - Habla: " + habla;
        return info;

    }
}

package view;

import controller.Gestor;
import enums.HabilidadTrabajador;
import enums.ServicioHabitacion;
import exceptions.ComandaException;
import utils.CastData;
import utils.ColorTexto;

import java.awt.*;
import java.util.HashSet;

public class Validator {

    private Gestor g = new Gestor();

    public void valRoom(String[] comandos) throws ComandaException {
        valNumArgumentos(comandos.length, 4);
        valDigits(comandos[1], false);
        g.addRoom(comandos[1],
                valNumPositivoEntero(comandos[2]),
                valServicios(comandos[3]));
    }

    public void valWorker(String[] comandos) throws ComandaException{
        valNumArgumentos(comandos.length, 4);
        valDigits(comandos[1], true);
        g.addWorker(comandos[1], comandos[2], valHabilidades(comandos[3]));
    }
    public void valReservation(String[] comandos) throws ComandaException{
        valNumArgumentos(comandos.length, 4);
        valDigits(comandos[1], true);
        g.addReserva(comandos[1], valNumPositivoEntero(comandos[2]), valRequisitos(comandos[3]));
    }
    public void valHotel(String[] comandos) throws ComandaException {
        valNumArgumentos(comandos.length, 1);
        g.mostrarHotel();

    }
    public void valProblem(String[] comandos) throws ComandaException{
        valNumArgumentos(comandos.length, 2);
        valDigits(comandos[1], false);
        g.problemas(comandos[1]);

    }
    public void valRequest(String[] comandos) throws ComandaException {
        valNumArgumentos(comandos.length, 3);
        valDigits(comandos[1], false);
        g.peticion(comandos[1], valHabilidades(comandos[2]));

    }
    public void valLeave(String[] comandos)  throws ComandaException{
        valNumArgumentos(comandos.length, 3);
        valDigits(comandos[1], false);
        g.leave(comandos[1], valNumPositivoEntero(comandos[2]));
    }

    public void valFinish(String[] comandos)  throws ComandaException{
        valNumArgumentos(comandos.length, 2);
        valDigits(comandos[1], false);
        g.finish(comandos[1]);

    }
    public void valMoney(String[] comandos) throws ComandaException {
        valNumArgumentos(comandos.length, 1);
        g.mostrarMoney();

    }
    public void valExit(String[] comandos) throws ComandaException {
        valNumArgumentos(comandos.length, 1);

    }

    private void valNumArgumentos(int longitud, int longitudEsperada) throws ComandaException{
        if(longitud != longitudEsperada){
            throw new ComandaException(ComandaException.NUM_ARGUMENTOS_EXCEPTION);
        }
    }

    private int valNumPositivoEntero(String num) throws ComandaException{
        int capacidad;
        try{
            capacidad = CastData.toInt(num);
            if(capacidad < 1){
                throw new ComandaException(ComandaException.NUM_MENOR_UNO_EXCEPTION);
            }
        }catch(NumberFormatException e){
            throw new ComandaException(ComandaException.DATO_EXCEPTION);
        }
        return capacidad;
    }


    private boolean valDigits(String num, boolean isDni) throws ComandaException{
        boolean isValid;

        valNumPositivoEntero(num);
        int numDigits;
        if(isDni){
            numDigits = num.length();
            if (numDigits != 8) {
                throw new ComandaException(ComandaException.NUM_DIGITOSDNI_EXCEPTION);
            }else{
                isValid = true;
            }
        }else{
            numDigits = num.length();
            if (numDigits != 3) {
                throw new ComandaException(ComandaException.NUM_DIGITOS_EXCEPTION);
            }else{
                isValid = true;
            }
        }

        return isValid;
    }

    private HashSet<String> valServicios(String servicios)throws ComandaException {
        String[] servs = servicios.split(",");
        HashSet<String> servis = new HashSet<>();
        for(String s: servs){
            try{
                ServicioHabitacion.valueOf(s);
                servis.add(s);
            }catch(IllegalArgumentException e){
                throw new ComandaException(ComandaException.SERVICIO_EXCEPTION);
            }
        }
        return servis;
    }

    private HashSet<String> valHabilidades(String habilidades) throws ComandaException{
        String[] habs = habilidades.split(",");
        HashSet<String> skills = new HashSet<>();
        for(String s: habs){
            try{
                HabilidadTrabajador.valueOf(s);
                skills.add(s);
            }catch(IllegalArgumentException e){
                throw new ComandaException(ComandaException.HABILIDAD_EXCEPTION);
            }
        }
        return skills;
    }

    private HashSet<String> valRequisitos(String requisitos) throws ComandaException{
        String[] reqs = requisitos.split(",");
        HashSet<String> skills = new HashSet<>();
        for(String s: reqs){
            try{
                ServicioHabitacion.valueOf(s);
                skills.add(s);
            }catch(IllegalArgumentException e){
                throw new ComandaException(ComandaException.SERVICIO_EXCEPTION);
            }
        }
        return skills;
    }

}

package view;

import controller.Gestor;
import enums.*;
import exception.ComandaException;
import utils.CastData;

public class Validator {

    private Gestor g = new Gestor();

    public void valRegistrarMascota(String[] comandos) throws ComandaException{
        if(comandos.length > 4 && comandos.length < 9){
            int edad = valEdatAnimal(comandos[2]);
            boolean esMacho = valGenero(comandos[3]);
            valTipoAnimal(comandos[4]);
            if(comandos[4].equalsIgnoreCase(TipoAnimal.GOS.name())){
                valNumArgumentos(comandos.length, 7);
                boolean peloLargo = valPelo(comandos[5]);
                GrandariaPelo p = valGrandariaPelo(comandos[6]);
                g.RegistrarPerro(comandos[1], esMacho, edad, peloLargo, p);

            }else if(comandos[4].equalsIgnoreCase(TipoAnimal.GAT.name())){
                valNumArgumentos(comandos.length, 6);
                int h = valHorasDias(comandos[5]);
                g.RegistrarGato(comandos[1], esMacho, edad, h);

            }else if(comandos[4].equalsIgnoreCase(TipoAnimal.LLORO.name())){
                valNumArgumentos(comandos.length, 8);
                int h = valHorasDias(comandos[5]);
                boolean silva = valSiNo(comandos[6]);
                boolean habla = valSiNo(comandos[7]);
                g.RegistrarLoro(comandos[1], esMacho, edad, h, silva, habla);

            }else if(comandos[4].equalsIgnoreCase(TipoAnimal.AGAPORNI.name())){
                valNumArgumentos(comandos.length, 7);
                int h = valHorasDias(comandos[5]);
                int altura  = valAlturaAgaporni(comandos[6]);
                g.RegistrarAgaporni(comandos[1], esMacho, edad, h, altura);

            }
        }else{
            throw new ComandaException(ComandaException.NUM_ARGUMENTOS_EXCEPTION);
        }

    }
    public void valRegistrarTratamiento(String[] comandos) throws ComandaException{
        if(comandos.length > 3 && comandos.length < 7){
            Tratamientos tratamiento = valTipoTratamiento(comandos[2]);
            if(tratamiento.equals(Tratamientos.PERRUQUERIA)){
                valNumArgumentos(comandos.length, 6);
                boolean tall = valSiNo(comandos[3]);
                boolean rentat = valSiNo(comandos[3]);
                boolean assecat = valSiNo(comandos[3]);
                g.RegistrarPeluqueria(comandos[1], tall, rentat, assecat);
            }else if(tratamiento.equals(Tratamientos.VACUNA)){
                valNumArgumentos(comandos.length, 5);
                boolean primeraVez = valSiNo(comandos[4]);
                g.RegistrarVacuna(comandos[1], comandos[3], primeraVez);
            }else if(tratamiento.equals(Tratamientos.REVISIO)){
                valNumArgumentos(comandos.length, 4);
                g.RegistrarRevision(comandos[1], comandos[3]);
            }else if(tratamiento.equals(Tratamientos.CURA)){
                valNumArgumentos(comandos.length, 4);
                boolean huesoRoto = valSiNo(comandos[3]);
                g.RegistrarCura(comandos[1], huesoRoto);
            }
        }else{
            throw new ComandaException(ComandaException.NUM_ARGUMENTOS_EXCEPTION);
        }
    }

    public void valVerFicha(String[] comandos) throws ComandaException{
        valNumArgumentos(comandos.length, 2);
        g.VerFicha(comandos[1]);
    }

    public void valExit(String[] comandos) throws ComandaException {
        valNumArgumentos(comandos.length, 1);
    }


    private void valNumArgumentos(int longitud, int longitudEsperada) throws ComandaException{
        if(longitud != longitudEsperada){
            throw new ComandaException(ComandaException.NUM_ARGUMENTOS_EXCEPTION);
        }
    }

    private double valNumDecimal(String num) throws ComandaException{
        double decimal;
        try{
            decimal = CastData.toDouble(num);
        }catch(NumberFormatException e){
            throw new ComandaException(ComandaException.DATO_EXCEPTION);
        }
        return decimal;
    }

    private int valNumEntero(String num) throws ComandaException{
        int entero;
        try{
            entero = CastData.toInt(num);
        }catch(NumberFormatException e){
            throw new ComandaException(ComandaException.DATO_EXCEPTION);
        }
        return entero;
    }

    private int valAlturaAgaporni(String altura) throws ComandaException{
        int a = valNumEntero(altura);
        valNumPositivo(altura, 1, false);
        if(a > 25){
            throw new ComandaException(ComandaException.ALTURA_AGAPORNI_EXCEPTION);
        }
        return a;
    }

    private void valNumPositivo(String num, int min, boolean esDecimal) throws ComandaException{

        if(esDecimal){
            if(valNumDecimal(num) < min){
                throw new ComandaException(ComandaException.NUM_MENOR_UNO_EXCEPTION);
            }
        }else{
            if(valNumEntero(num) < min){
                throw new ComandaException(ComandaException.NUM_MENOR_UNO_EXCEPTION);
            }
        }
    }

    public int valHorasDias(String horas) throws ComandaException{
        valNumPositivo(horas, 0,false);
        int cantidad =valNumEntero(horas);
        if(cantidad > 24){
            throw new ComandaException(ComandaException.NUM_HORAS_EXCEPTION);
        }
        return cantidad;
    }

    public int valEdatAnimal(String edadAnimal) throws ComandaException{
        int edad = valNumEntero(edadAnimal);
        if(edad < 0 || edad >50){
            throw new ComandaException(ComandaException.EDAD_NO_VALIDA_EXCEPTION);
        }
        return edad;
    }
    private GrandariaPelo valGrandariaPelo(String pelo)throws ComandaException {
        try{
            GrandariaPelo.valueOf(pelo);
        }catch(IllegalArgumentException e){
            throw new ComandaException(ComandaException.GRANDARIA_PELO_EXCEPTION);
        }
        return GrandariaPelo.valueOf(pelo);
    }

    private boolean valSiNo(String respuesta)throws ComandaException {
        boolean si = false;
        try{
            SiNo.valueOf(respuesta);
            if(respuesta.equalsIgnoreCase("SI")){
                si = true;
            }
        }catch(IllegalArgumentException e){
            throw new ComandaException(ComandaException.SINO_EXCEPTION);
        }
        return si;
    }

    private Tratamientos valTipoTratamiento(String tratamiento)throws ComandaException {
        Tratamientos tratamientos;
        try{
            tratamientos = Tratamientos.valueOf(tratamiento);
        }catch(IllegalArgumentException e){
            throw new ComandaException(ComandaException.SINO_EXCEPTION);
        }
        return tratamientos;
    }



    private boolean valPelo(String pelo)throws ComandaException {
        boolean peloLargo = false;
        try{
            PeloPerro.valueOf(pelo);
            if(pelo.equalsIgnoreCase("LLARG")){
                peloLargo = true;
            }
        }catch(IllegalArgumentException e){
            throw new ComandaException(ComandaException.PELO_EXCEPTION);
        }
        return peloLargo;
    }

    private boolean valDigits(String num, boolean isDni) throws ComandaException{
        boolean isValid;

        valNumPositivo(num, 1,false);
        int numDigits;
        if(isDni){
            numDigits = num.length();
            if (numDigits != 8) {
                throw new ComandaException(ComandaException.NUM_DIGITOS_EXCEPTION);
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

    private boolean valGenero(String genero)throws ComandaException {
        boolean esMacho = false;
        try{
            GeneroAnimal.valueOf(genero);
            if(genero.equalsIgnoreCase("M")){
                esMacho = true;
            }

        }catch(IllegalArgumentException e){
            throw new ComandaException(ComandaException.GENERO_EXCEPTION);
        }
        return esMacho;
    }

    private void valTipoAnimal(String animal)throws ComandaException {
        try{
            TipoAnimal.valueOf(animal);
        }catch(IllegalArgumentException e){
            throw new ComandaException(ComandaException.TIPO_ANIMAL_EXCEPTION);
        }
    }

    //Cambiar el tipo de HashSet y los nombres de las clases Enums
    /*private HashSet<Genero> val(String genero)throws ComandaException {
        String[] servs = servicios.split(",");
        HashSet<String> servis = new HashSet<>();
        for(String s: servs){
            try{
                servis.add(ServicioHabitacion.valueOf(s));
            }catch(IllegalArgumentException e){
                throw new ComandaException(ComandaException.ENUM_EXCEPTION);
            }
        }
        return servis;
    }*/
}

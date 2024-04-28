package exceptions;

import utils.ColorTexto;

import java.util.ArrayList;
import java.util.Arrays;

public class ComandaException extends Exception{

    public final static int NUM_ARGUMENTOS_EXCEPTION = 0;
    public final static int DATO_EXCEPTION= 1;
    public final static int NUM_DIGITOS_EXCEPTION = 2;
    public final static int SERVICIO_EXCEPTION = 3;
    public final static int NUM_MENOR_UNO_EXCEPTION = 4;
    public final static int HABITACION_EXISTENTE_EXCEPTION = 5;
    public final static int TRABAJADOR_EXISTENTE_EXCEPTION = 6;
    public final static int HABILIDAD_EXCEPTION = 7;
    public final static int HABITACION_NO_DISPONIBLE = 8;
    public final static int HABITACION_REQUISITOS_EXCEPTION = 9;
    public final static int HABITACION_NO_EXISTE_EXCEPTION = 10;
    public final static int DNI_TRABAJADOR = 11;
    public final static int HABITACION_NO_RESERVADA = 12;
    public final static int OPCION_NO_VALIDA = 13;
    public final static int NO_HABITACIONES_REGISTRADAS = 14;
    public final static int NO_TRABAJADORES_REGISTRADOS = 15;
    public final static int NUM_DIGITOSDNI_EXCEPTION = 16;


    private final ArrayList<String> errores = new ArrayList<>(Arrays.asList(
            "[ Número de argumentos incorrecto ]",
            "[ Dada incorrecta ]",
            "[ El número de habitación tiene que tener 3 dígitos ]",
            "[ Uno o más de los servicios introducidos no está(n) disponible(s) ]",
            "[ No puede haber un número de habitación o capacidad de la misma menor o igual a cero ]",
            "[ Ya existe una habitación con ese número ]",
            "[ Ya existe un trabajador con ese dni ]",
            "[ Una o más de las habilidades introducidas no está(n) disponible(s) ]",
            "[ La habitacion no está disponible ]",
            "[ No hay ninguna habitación que cumpla los requisitos. Pierdes 100$ ]",
            "[ La habitacion introducida no existe ]",
            "[ El dni del introducido es de un trabajador ]",
            "[ No hay ningún cliente en esta habitación ]",
            "[ Opción no válida ]",
            "[ No hay ninguna habitación registrada ]",
            "[ No hay ningún trabajador registrado ]",
            "[ El número de dni tiene que tener 8 dígitos ]"));

    private int code;


    public ComandaException(int code){
        this.code = code;
    }

    @Override
    public String toString() {
        return ColorTexto.RED + errores.get(code) + ColorTexto.RESET;
    }
}

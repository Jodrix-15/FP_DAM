package exception;

import java.util.ArrayList;
import java.util.Arrays;

public class ComandaException extends Exception{

    public final static int NUM_ARGUMENTOS_EXCEPTION = 0;
    public final static int DATO_EXCEPTION= 1;
    public final static int NUM_MENOR_UNO_EXCEPTION = 2;
    public final static int NUM_DIGITOS_EXCEPTION = 3;

    public final static int CLAVE_EXISTE_EXCEPTION = 4;
    public final static int CLAVE_NO_EXISTE_EXCEPTION = 5;

    public final static int ENUM_EXCEPTION = 6;
    public final static int EDAD_NO_VALIDA_EXCEPTION = 7;

    public final static int GENERO_EXCEPTION = 8;
    public final static int TIPO_ANIMAL_EXCEPTION = 9;
    public final static int GRANDARIA_PELO_EXCEPTION = 10;
    public final static int PELO_EXCEPTION = 11;
    public final static int NUM_HORAS_EXCEPTION = 12;
    public final static int SINO_EXCEPTION = 13;
    public final static int ALTURA_AGAPORNI_EXCEPTION = 14;
    public final static int TRABAJADOR_EXCEPTION = 15;
    public final static int ESPECIALIDAD_TRABAJADOR_EXCEPTION = 16;



    private final ArrayList<String> errores = new ArrayList<>(Arrays.asList(
            "[ El número de argumentos es incorrecto ]",
            "[ Dada incorrecta ]",
            "[ El número no puede ser menor que uno ]",
            "[ Cantidad de dígitos incorrecto ]",
            "[ La clave introducida ya está registrada ]",
            "[ La clave introducida no existe ]",
            "[ Enum no válido ]",
            "[ La edad introducidad no es válida ]",
            "[ El género introducido no es válido ]",
            "[ Tipo animal no válido ]",
            "[ La grandaria del pelo introducida no es válida ]",
            "[ El largo del pelo introducido no es válido ]",
            "[ La cantidad de horas al dia no puede ser menor que cero o mayor que 24 ]",
            "[ Solo se permite como respuesta Si o No ]",
            "[ La altura del agaporni no es válida ]",
            "[ El trabajador no existe ]",
            "[ Ningún trabajador cumple con los requisitos ]"
            ));

    private int code;

    public ComandaException(int code){
        this.code = code;
    }

    @Override
    public String toString() {
        return errores.get(code);
    }
}

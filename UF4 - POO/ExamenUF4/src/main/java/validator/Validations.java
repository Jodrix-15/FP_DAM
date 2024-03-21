package validator;

import controller.Gestor;
import utils.CastData;

public class Validations {

    private Gestor gestor = new Gestor();

    public boolean valLength(int argsLength, int lengthEsperada) {
        boolean Validacion = false;
        if (argsLength == lengthEsperada) {
            Validacion = true;
        } else {
            System.out.println("ERROR. El número de argumentos es incorrecto.");
        }
        return Validacion;
    }

    public boolean valPhone(String tel) {
        //TODO Valentinalinda
        boolean esCorrecto = true;
        if (tel.length() == 9) {
            for (int i = 0; i < tel.length(); i++) {
                if (!Character.isDigit(tel.charAt(i))) {
                    System.out.println("El número de teléfono introducido no es válido.");
                    esCorrecto = false;
                }
            }
        } else {
            System.out.println("El numero de telefono introducido no es valido.");
            esCorrecto = false;
        }

        return esCorrecto;
    }

    public boolean valDni(String dni) {
        //TODO Jordi
        dni = dni.strip().toUpperCase();
        boolean isValid = false;
        int resto = 0;
        String dniNum = getNumDni(dni);
        int numDni = 0;
        String validLetters = "TRWAGMYFPDXBNJZSQVHLCKE";

        if (dniNum.length() == 8 && dni.length() == 9) {
            numDni = CastData.toInt(dniNum);
            char letter = dni.charAt(dni.length() - 1);

            resto = numDni % 23;
            if (letter == validLetters.charAt(resto)) {
                isValid = true;
            } else {
                System.out.println("El último carácter solo puede ser una letra y tiene que ser válida");
            }
        } else {
            System.out.println("El formato del DNi debe ser '12345678X'");
        }

        return isValid;
    }

    public String getNumDni(String dni) {
        String validNumbers = "0123456789";
        String numDni = "";
        for (int i = 0; i < dni.length() - 1; i++) {
            for (int j = 0; j < validNumbers.length(); j++) {
                if (dni.charAt(i) == validNumbers.charAt(j)) {
                    numDni += dni.charAt(i);
                }
            }
        }
        return numDni;
    }
}
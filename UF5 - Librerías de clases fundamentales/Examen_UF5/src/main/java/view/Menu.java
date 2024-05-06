package view;

import enums.EspecialidadTrabajador;
import exception.ComandaException;
import models.Trabajador;
import utils.InputData;

import java.util.ArrayList;
import java.util.HashSet;

public class Menu {

    private Validator val = new Validator();
    private InputData inp = new InputData();
    private Comandos c = new Comandos();


    public void start() {
        boolean finalizar = false;

        ArrayList<String> errores = c.getPruebaErrores();
        ArrayList<String> funcionalidad = c.getPruebaFuncionalidad();



        do {
            for (String co : funcionalidad) {
                System.out.println("> " + co);
                String[] comandos = co.toUpperCase().split("-");
                String opcion = comandos[0];

               //String[] comandos = inp.inputString("> ").toUpperCase().split("-");
                //String opcion = comandos[0];

                try {
                    switch (opcion) {

                        case "P":
                            val.valRegistrarMascota(comandos);
                            break;

                        case "R":
                            val.valRegistrarTratamiento(comandos);
                            break;

                        case "V":
                            val.valVerFicha(comandos);
                            break;

                        case "E":
                            val.valExit(comandos);
                            finalizar = true;
                            break;

                        default:
                            System.out.println("Opción no válida");
                    }
                } catch (ComandaException e) {
                    System.out.println(e);
                }
            }
        } while (!finalizar);
    }



}

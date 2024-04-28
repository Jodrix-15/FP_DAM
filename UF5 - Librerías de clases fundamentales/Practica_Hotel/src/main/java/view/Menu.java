package view;

import controller.Gestor;
import exceptions.ComandaException;
import utils.InputData;

import java.util.ArrayList;

public class Menu {

    private Validator val = new Validator();
    private InputData inp = new InputData();
    private Comandos c = new Comandos();
    public void start(){
        boolean finalizar = false;
        Gestor g = new Gestor();
        ArrayList<String> coms = c.getComs();
        ArrayList<String> pruebas = c.getPrueba();

        do {
            int money;
            String[] comandos;
            String opcion;

            for (String co : pruebas) {
                if(finalizar){
                    co = "EXIT";
                    comandos = co.toUpperCase().split(" ");
                    opcion = comandos[0];
                }else {
                    System.out.println("> " + co);
                    comandos = co.toUpperCase().split(" ");
                    opcion = comandos[0];
                }

                //String[] comandos = inp.inputString("> ").toUpperCase().split(" ");
                //String opcion = comandos[0];



                try {
                    switch (opcion) {

                        case "ROOM":
                            val.valRoom(comandos);
                            break;

                        case "WORKER":
                            val.valWorker(comandos);
                            break;

                        case "RESERVATION":
                            val.valReservation(comandos);
                            break;

                        case "HOTEL":
                            val.valHotel(comandos);
                            break;

                        case "PROBLEM":
                            val.valProblem(comandos);
                            break;

                        case "REQUEST":
                            val.valRequest(comandos);
                            break;

                        case "FINISH":
                            val.valFinish(comandos);
                            break;

                       case "LEAVE":
                            val.valLeave(comandos);
                            money = g.getMoney();
                            if(money<=0){
                                g.quiebra();
                                finalizar = true;
                            }
                            break;

                        case "MONEY":
                            val.valMoney(comandos);
                            break;

                        case "EXIT":
                            val.valExit(comandos);
                            finalizar = true;
                            break;
                        default:
                            System.out.println(new ComandaException(ComandaException.OPCION_NO_VALIDA));
                    }
                } catch (ComandaException e) {
                    System.out.println(e);
                    money = g.getMoney();
                    if(money<=0){
                        g.quiebra();
                        finalizar = true;
                    }
                }
            }
        }while (!finalizar);
    }
}
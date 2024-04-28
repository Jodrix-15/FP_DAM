package view;

import java.util.ArrayList;
import java.util.Arrays;

public class Comandos {
    private ArrayList<String> coms = new ArrayList<>(Arrays.asList(
            "HOLA",
            "ROOM",
            "ROoM 00a hola mec",
            "ROoM 0001 hola mec",
            "ROoM 001 a mec",
            "ROoM 001 -1 mec",
            "ROoM 001 2 mec",
            "ROOM 001 3 tv,jacuzzi,balcon",
            "ROoM 001 2 jacuzzi",
            "WorkEr",
            "Worker 1 2 3 4",
            "WORKER 12345678 Pepe piscina,hola",
            "WORKER 12345678 Pepe piscina,mantenimiento",
            "WORKER 12345678 Pepe piscina,mantenimiento",
            "WORKER 1234s679 Pepe piscina,mantenimiento,piscina",
            "Money a",
            "money",
            "hotel a",
            "hotel",
            "RESERVAtion",
            "REservation 2 3 4 5",
            "reservation 111a2233 1 tv",
            "reservation 11122233 -1 tv",
            "reservation 11122233 1 mec",
            "reservation 11122233 4 tv",
            "reservation 11122233 1 tv",
            "exit"
    ));

    private ArrayList<String> prueba = new ArrayList<>(Arrays.asList(
            "ROOM 001 2 tv,jacuzzi,balcon",
            "Room 002 2 tv,llitdoble",
            "room 003 1 telefono,satelite,tv",
            "room 004 2 suite,jacuzzi,tv,balcon,llitdoble,minibar,telefono,satelite",
            "room 005 4 tv,telefono,llitdoble",
            "room 006 1 tv",
            "worker 12345678 Pepe piscina,mantenimiento",
            "worker 88888888 Maria mantenimiento,spa",
            "worker 11111111 Juan limpieza,bar,comida,bogaderia",
            "worker 22222222 Clara comida,bar",
            "Room 007 2 llitdoble,tv,llitdoble",
            "room 008 1 satelite,telefono,tv",
            "room 001 1 tv",
            "room 009 2 sauna,tv,satelite",
            "Worker 33333333 Antonio limpieza,mantenimiento",
            "worker 44444444 Paco piscina,bar",
            "worker 33333333 Pepe piscina,mantenimiento",
            "worker 55555555 Sandra piscina,mantenimiento,sauna",
            "Reservation 11223344 1 tv",
            "reservation 33445566 2 llitdoble,tv,telefono",
            "reservation 55667788 1 tv",
            "reservation 88888848 4 jacuzzi,tv,balcon",
            "money",
            "hotel",
            "problem 001",
            "problem 888",
            "problem 003",
            "problem 004",
            "problem 005",
            "hotel",
            "request 001 mantenimiento,limpieza",
            "request 003 piscina,mantenimiento,limpieza",
            "request 006 comida,bar",
            "request 888 bar",
            "request 001 informatica,limpieza",
            "hotel",
            "finish 003",
            "finish 004",
            "finish 888",
            "finish",
            "hotel",
            "leave 888",
            "leave 888 500",
            "leave 006 400",
            "leave 008 200",
            "EXIT"));

    public ArrayList<String> getComs() {
        return coms;
    }

    public ArrayList<String> getPrueba() {
        return prueba;
    }
}

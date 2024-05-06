package view;

import java.util.ArrayList;
import java.util.Arrays;

public class Comandos {
    private ArrayList<String> pruebaErrores = new ArrayList<>(Arrays.asList(
            "p-hola",
            "p hola",
            "p-hola-hola-2-3-4-5",
            "p-Barley-60-T-Rata",
            "p-Barley-49-T-Rata",
            "p-Barley-35-M-Rata",
            "p-Barley-29-F-Gos",
            "p-Barley-29-F-Gos-mitad-hombre",
            "p-Barley-29-F-Gos-llarg-homobre",
            "p-Barley-29-F-Gos-llarg-petit",
            "E"
    ));

    private ArrayList<String> pruebaFuncionalidad = new ArrayList<>(Arrays.asList(
            "p-Barley-29-F-Gos-llarg-petit",
            "p-sakura-4-f-gat-14",
            "p-pepe-8-m-lloro-12-si-SI",
            "p-paca-6-f-agaporni-5-15",
            "p-Barley-29-F-Gos-llarg-petit",
            "v-jodrix",
            "R-Barley-perruqueria-si-si-si",
            "r-pepe-vacuna-rabia-si",
            "r-Barley-REVISIO-tot be",
            "r-lola-vacuna-rubeola-no",
            "r-paca-vacuna-rubeola-no",
            "r-sakura-cura-si",
            "v-paca",
            "v-sakura",
            "v-pepe",
            "v-barley",
            "E"));

    public ArrayList<String> getPruebaErrores() {
        return pruebaErrores;
    }

    public ArrayList<String> getPruebaFuncionalidad() {
        return pruebaFuncionalidad;
    }
}
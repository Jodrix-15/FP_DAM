package models.tratamientos;

import enums.Tratamientos;
import models.Trabajador;

public class Peluqueria extends Tratamiento{

    private boolean peloLargo;
    private boolean tall;
    private boolean rentat;
    private boolean assecat;

    public Peluqueria(Trabajador trabajador, boolean peloLargo, boolean tall, boolean rentat, boolean assecat) {
        super(trabajador);
        this.peloLargo = peloLargo;
        this.tall = tall;
        this.rentat = rentat;
        this.assecat = assecat;
    }

    @Override
    public double calcularPreu() {
        if(tall){
            this.precio += 10;
        }
        if(rentat){
            this.precio += 9.99;
        }
        if(assecat){
            this.precio += 5.15;
        }
        if(peloLargo){
            this.precio += 8.75;
        }
        return this.precio;
    }

    @Override
    public String toString() {
        return super.toString() + " - Tipus: " + Tratamientos.PERRUQUERIA + " - Precio: " + this.precio + "€";
    }
}

package controller;

import enums.EspecialidadTrabajador;
import enums.GrandariaPelo;
import exception.ComandaException;
import models.*;
import models.mascotas.*;
import models.tratamientos.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Gestor {
    
    private HashMap<String, Animal> animales = new HashMap<>(); //Uso hashmap porque los nommbres de los animales no se repiten, y puedo acceder a ellos con facilidad
    private ArrayList<Trabajador> trabajadores = afegirTreballadors();
    private HashMap<Integer, Tratamiento> tratamientos = new HashMap<>();



    public ArrayList<Trabajador> afegirTreballadors(){
        this.trabajadores = new ArrayList<>();
        HashSet<EspecialidadTrabajador> mireia = new HashSet<>();
        mireia.add(EspecialidadTrabajador.VETERINARIA);
        mireia.add(EspecialidadTrabajador.PERRUQUERIA);
        HashSet<EspecialidadTrabajador> aitor = new HashSet<>();
        aitor.add(EspecialidadTrabajador.VETERINARIA);
        HashSet<EspecialidadTrabajador> leo = new HashSet<>();
        leo.add(EspecialidadTrabajador.PERRUQUERIA);
        HashSet<EspecialidadTrabajador> paloma = new HashSet<>();
        paloma.add(EspecialidadTrabajador.INFERMERIA);
        trabajadores.add(new Trabajador("12345678A", "Mireia", "Montana Mares", "666112233", mireia));
        trabajadores.add(new Trabajador("55555555Z", "Aitor", "Menta Rayos", "656565656", aitor));
        trabajadores.add(new Trabajador("11111111X", "Leo", "Palomo Sanchez", "6466444444", leo));
        trabajadores.add(new Trabajador("22222222F", "Paloma", "Posada Alamo", "619999999", paloma));

        return trabajadores;
    }

    public void RegistrarPerro(String nombre, boolean esMacho, int edad, boolean pelo, GrandariaPelo grandaria) throws ComandaException{
        if(!mapClaveExiste(nombre)){
            Perro perro = new Perro(nombre, esMacho, edad, pelo, grandaria);
            animales.put(nombre, perro);
            System.out.println("Perro registrado correctamente");
        }else{
            throw new ComandaException(ComandaException.CLAVE_EXISTE_EXCEPTION);
        }
    }

    public void RegistrarGato(String nombre, boolean esMacho, int edad, int horasDuerme) throws ComandaException{
        if(!mapClaveExiste(nombre)){
            Gato gato = new Gato(nombre, esMacho, edad, horasDuerme);
            animales.put(nombre, gato);
            System.out.println("Gato registrado correctamente");

        }else{
            throw new ComandaException(ComandaException.CLAVE_EXISTE_EXCEPTION);
        }

    }
    public void RegistrarLoro(String nombre, boolean esMacho, int edad, int horasLibertad, boolean silva, boolean hablan) throws ComandaException{
        if(!mapClaveExiste(nombre)){
            Loro loro = new Loro(nombre, esMacho, edad, horasLibertad, silva, hablan);
            animales.put(nombre, loro);
            System.out.println("Loro registrado correctamente");

        }else{
            throw new ComandaException(ComandaException.CLAVE_EXISTE_EXCEPTION);
        }

    }
    public void RegistrarAgaporni(String nombre, boolean esMacho, int edad, int horasLibertad, int altura) throws ComandaException{
        if(!mapClaveExiste(nombre)){
            Agaporni agaporni = new Agaporni(nombre, esMacho, edad, horasLibertad, altura);
            animales.put(nombre, agaporni);
            System.out.println("Agaporni registrado correctamente");

        }else{
            throw new ComandaException(ComandaException.CLAVE_EXISTE_EXCEPTION);
        }

    }

    public void RegistrarPeluqueria(String nombreMascota, boolean tall, boolean rentat, boolean assecat) throws ComandaException{
        if(!trabajadores.isEmpty()){
            Animal animal = getMapValueByKey(nombreMascota);
            Trabajador trabajador = asignarTrabajador(EspecialidadTrabajador.PERRUQUERIA);

            boolean peloLargo = false;
            Peluqueria peluqueria;
            if(animal instanceof Perro perro){
                if(perro.isPeloLargo()){
                    peloLargo = true;
                }
                peluqueria = new Peluqueria(trabajador, peloLargo, tall, rentat, assecat);
                perro.addTratamiento(peluqueria);
                tratamientos.put(peluqueria.getCodTratamiento(), peluqueria);
                info(trabajador, peluqueria.calcularPreu(), peluqueria.getCodTratamiento());


            }else if(animal instanceof Loro loro){
                peluqueria = new Peluqueria(trabajador, peloLargo, tall, rentat, assecat);
                loro.addTratamiento(peluqueria);
                tratamientos.put(peluqueria.getCodTratamiento(), peluqueria);
                info(trabajador, peluqueria.calcularPreu(), peluqueria.getCodTratamiento());


            }else if(animal instanceof Gato gato){
                peluqueria = new Peluqueria(trabajador, peloLargo, tall, rentat, assecat);
                gato.addTratamiento(peluqueria);
                tratamientos.put(peluqueria.getCodTratamiento(), peluqueria);
                info(trabajador, peluqueria.calcularPreu(), peluqueria.getCodTratamiento());


            }else if(animal instanceof Agaporni agaporni){
                peluqueria = new Peluqueria(trabajador, peloLargo, tall, rentat, assecat);
                agaporni.addTratamiento(peluqueria);
                tratamientos.put(peluqueria.getCodTratamiento(), peluqueria);
                info(trabajador, peluqueria.calcularPreu(), peluqueria.getCodTratamiento());
            }

        }else{
            throw new ComandaException(ComandaException.TRABAJADOR_EXCEPTION);
        }

    }

    public void info(Trabajador trabajador, double precio, int codigo){
        System.out.println("Tratamiento registrado. Código: " + codigo+
                "\nTrabajador que ha realizado el tratamiento: " + trabajador +
                "\nPrecio del tratamiento: " + precio + "€");
    }
    public void RegistrarVacuna(String nombreMascota, String nombreVacuna, boolean primeraVez) throws ComandaException{
        if(!trabajadores.isEmpty()){
            Animal animal = getMapValueByKey(nombreMascota);
            Trabajador trabajador = asignarTrabajador(EspecialidadTrabajador.INFERMERIA);

            if(animal instanceof Perro perro){
                Vacuna vacuna = new Vacuna(trabajador, nombreVacuna, primeraVez);
                perro.addTratamiento(vacuna);
                tratamientos.put(vacuna.getCodTratamiento(), vacuna);
                info(trabajador, vacuna.calcularPreu(), vacuna.getCodTratamiento());

            }else if(animal instanceof Loro loro){
                Vacuna vacuna = new Vacuna(trabajador, nombreVacuna, primeraVez);
                loro.addTratamiento(vacuna);
                tratamientos.put(vacuna.getCodTratamiento(), vacuna);
                info(trabajador, vacuna.calcularPreu(), vacuna.getCodTratamiento());

            }else if(animal instanceof Gato gato){
                Vacuna vacuna = new Vacuna(trabajador, nombreVacuna, primeraVez);
                gato.addTratamiento(vacuna);
                tratamientos.put(vacuna.getCodTratamiento(), vacuna);
                info(trabajador, vacuna.calcularPreu(), vacuna.getCodTratamiento());


            }else if(animal instanceof Agaporni agaporni){
                Vacuna vacuna = new Vacuna(trabajador, nombreVacuna, primeraVez);
                agaporni.addTratamiento(vacuna);
                tratamientos.put(vacuna.getCodTratamiento(), vacuna);
                info(trabajador, vacuna.calcularPreu(), vacuna.getCodTratamiento());
            }
        }else{
            throw new ComandaException(ComandaException.TRABAJADOR_EXCEPTION);
        }

    }
    public void RegistrarRevision(String nombreMascota, String descripcion) throws ComandaException{
        if(!trabajadores.isEmpty()){
            Animal animal = getMapValueByKey(nombreMascota);
            Trabajador trabajador = asignarTrabajador(EspecialidadTrabajador.VETERINARIA);

            boolean esPajaro = false;
            if(animal instanceof Pajaro){
                esPajaro = true;
            }
            if(animal instanceof Perro perro){
                Revision revision = new Revision(trabajador, esPajaro, descripcion);
                perro.addTratamiento(revision);
                tratamientos.put(revision.getCodTratamiento(), revision);
                info(trabajador, revision.calcularPreu(), revision.getCodTratamiento());

            }else if(animal instanceof Loro loro){
                Revision revision = new Revision(trabajador, esPajaro, descripcion);
                loro.addTratamiento(revision);
                tratamientos.put(revision.getCodTratamiento(), revision);
                info(trabajador, revision.calcularPreu(), revision.getCodTratamiento());

            }else if(animal instanceof Gato gato){
                Revision revision = new Revision(trabajador, esPajaro, descripcion);
                gato.addTratamiento(revision);
                tratamientos.put(revision.getCodTratamiento(), revision);
                info(trabajador, revision.calcularPreu(), revision.getCodTratamiento());


            }else if(animal instanceof Agaporni agaporni){
                Revision revision = new Revision(trabajador, esPajaro, descripcion);
                agaporni.addTratamiento(revision);
                tratamientos.put(revision.getCodTratamiento(), revision);
                info(trabajador, revision.calcularPreu(), revision.getCodTratamiento());            }

        }else{
            throw new ComandaException(ComandaException.TRABAJADOR_EXCEPTION);
        }
    }
    public void RegistrarCura(String nombreMascota, boolean huesoRoto) throws ComandaException{
        if(!trabajadores.isEmpty()){
            Animal animal = getMapValueByKey(nombreMascota);
            Trabajador trabajador = asignarTrabajador(EspecialidadTrabajador.INFERMERIA);

            if(animal instanceof Perro perro){
                Cura cura = new Cura(trabajador, huesoRoto);
                perro.addTratamiento(cura);
                tratamientos.put(cura.getCodTratamiento(), cura);
                info(trabajador, cura.calcularPreu(), cura.getCodTratamiento());

            }else if(animal instanceof Loro loro){
                Cura cura = new Cura(trabajador, huesoRoto);
                loro.addTratamiento(cura);
                tratamientos.put(cura.getCodTratamiento(), cura);
                info(trabajador, cura.calcularPreu(), cura.getCodTratamiento());

            }else if(animal instanceof Gato gato){
                Cura cura = new Cura(trabajador, huesoRoto);
                gato.addTratamiento(cura);
                tratamientos.put(cura.getCodTratamiento(), cura);
                info(trabajador, cura.calcularPreu(), cura.getCodTratamiento());

            }else if(animal instanceof Agaporni agaporni){
                Cura cura = new Cura(trabajador, huesoRoto);
                agaporni.addTratamiento(cura);
                tratamientos.put(cura.getCodTratamiento(), cura);
                info(trabajador, cura.calcularPreu(), cura.getCodTratamiento());            }

        }else{
            throw new ComandaException(ComandaException.TRABAJADOR_EXCEPTION);
        }

    }
    public void VerFicha(String nombre) throws ComandaException{
        Animal animal = getMapValueByKey(nombre);
        System.out.println("-------   EXPEDIENTE DE " + nombre + "   --------");
        if(animal instanceof Gato gato){
            System.out.println(gato.getExpedient());
        }else if(animal instanceof Perro perro){
            System.out.println(perro.getExpedient());
        }else if(animal instanceof Loro loro){
            System.out.println(loro.getExpedient());
        }else if(animal instanceof Agaporni agaporni){
            System.out.println(agaporni.getExpedient());
        }
    }


    private boolean mapClaveExiste(String clave){
        return animales.containsKey(clave);
    }

    private Animal getMapValueByKey(String clave) throws ComandaException{
        if(!mapClaveExiste(clave)){
            throw new ComandaException(ComandaException.CLAVE_NO_EXISTE_EXCEPTION);
        }
        return animales.get(clave);
    }

    private Trabajador asignarTrabajador(EspecialidadTrabajador especialidad) throws ComandaException{
        for(Trabajador t: trabajadores){
                if(t.getEspecialidades().contains(especialidad) || t.getEspecialidades().contains(EspecialidadTrabajador.VETERINARIA)){
                    moverTrabajadorAlFinal(t);
                    return t;
                }
        }
        throw new ComandaException(ComandaException.ESPECIALIDAD_TRABAJADOR_EXCEPTION);
    }

    private void moverTrabajadorAlFinal(Trabajador trabajador){
        trabajadores.remove(trabajador);
        trabajadores.add(trabajador);
    }
}

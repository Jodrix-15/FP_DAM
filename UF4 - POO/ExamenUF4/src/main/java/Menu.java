import utils.InputData;
import validator.Validations;

public class Menu {
    private Validations val = new Validations();
    public void start(){
        boolean finalizar = false;

        do{
            menu();
            int opcion = escogerOpcion();

            switch(opcion){
                case 1:

                    break;

                case 2:

                    break;

                case 3:

                    break;

                case 4:

                    break;

                case 5:

                    break;

                case 6:

                    break;

                case 0:
                    finalizar = true;
                    break;
            }

        }while(!finalizar);
    }

    public void menu(){
        System.out.println("Aquí va el menú");
    }

    public int escogerOpcion(){
        int opcion;
        int MAX_OPCIONES = 6;

        do{
            opcion = InputData.inputInt("Qué opción escoges?: ");
            if(opcion < 0 || opcion > MAX_OPCIONES){
                System.out.println("ERROR. Debe ser un numero entero entre 0 y " + MAX_OPCIONES);
            }
        }while(opcion < 0 || opcion > MAX_OPCIONES);

        return opcion;
    }
}

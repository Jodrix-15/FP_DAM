package controller;

import java.util.ArrayList;

public class Gestor {

    public int buscarCliente(ArrayList<Object> clientes, String phoneNumber){
        int posCliente = -1;
        int i = 0;
        if(!clientes.isEmpty()){
            while(posCliente == -1 && i<clientes.size()){
                Cliente cliente = (Cliente) clientes.get(i);
                if(cliente.getPhoneNumber().equalsIgnoreCase(phoneNumber)){
                    posCliente = i;
                }
                i++;
            }
        }
        return posCliente;
}

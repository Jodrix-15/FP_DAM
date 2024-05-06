package utils;

import java.util.Scanner;

public class InputData {

    private Scanner sc = new Scanner(System.in);

    public String inputString(String msj){
        System.out.print(msj);
        return sc.nextLine();
    }
}

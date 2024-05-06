package utils;

public class CastData {
    public static int toInt(String num) throws NumberFormatException{
        return Integer.parseInt(num);
    }

    public static double toDouble(String num) throws NumberFormatException{
        return Double.parseDouble(num);
    }
}

import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        NumberFormat usr = NumberFormat.getCurrencyInstance(Locale.US);
        String us = usr.format(payment);
        NumberFormat inr = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        String india = inr.format(payment);
        NumberFormat chy = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = chy.format(payment);
        NumberFormat Fre = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = Fre.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
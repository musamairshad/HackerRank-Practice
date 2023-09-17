/*
 * Author: Muhammad Daniyal Khan
 * Difficulty Level: Easy
 */.


 import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();//The reasone of this line is that after nextInt() it register nextLine() as a integer token so the string will be empty by adding that this become empty and our string has a value that we inputed
        String s = scan.nextLine();

        // Write your code here.

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
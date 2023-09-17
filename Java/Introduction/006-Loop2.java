/*
 * Author: Muhammad Daniyal Khan
 * Difficulty Level: Easy
 */


import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int sum = a;
            int k = 1;
            for (int j = 1 ; j <= n ; j ++){
                sum = sum + (k * b);
                k = k * 2;
                System.out.print(sum+" ");
            }
            System.out.println();
        }
        in.close();
    }
}
/*
 * Author: Muhammad Daniyal Khan
 * Difficulty Level: Easy
 */

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String temp = "";
        for(int i = A.length() - 1 ; i >= 0 ; i--){
            temp = temp + A.charAt(i);
        }
        System.out.println((A.equals(temp)? "Yes": "No"));
        
    }
}

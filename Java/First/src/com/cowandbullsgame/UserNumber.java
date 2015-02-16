package com.cowandbullsgame;

import java.util.Arrays;
import java.util.Scanner;


public class UserNumber extends Number {

    private static int value = 0;

    public void setValue() {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the number of " + DEFAULT_AMOUNT + " digits:");
        value = in.nextInt();
        for (int i = DEFAULT_AMOUNT - 1; i >= 0; i--) {
            bufComp[i] = value % 10;
            value = value / 10;
        }
    }

    public void getValue() {
        System.out.println(Arrays.toString(bufComp));
    }
}

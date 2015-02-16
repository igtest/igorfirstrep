package com.cowandbullsgame;

import java.util.Arrays;
import java.util.Random;

public class CompNumber extends Number {


    Random newValue = new Random();

    public void setValue() {
        for (int i = 0; i < bufComp.length; i++) {
            bufComp[i] = newValue.nextInt(10);
            int max = i;
            while (max > 0) {
                if (bufComp[--max] == bufComp[i]) {
                    bufComp[i] = newValue.nextInt(bufComp[i]);
                }
            }
        }
    }

    public void getValue() {
        System.out.println(Arrays.toString(bufComp));
    }
}

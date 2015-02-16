package com.cowandbullsgame;


public class Main {

    public static void main(String[] args) {


        Play play1 = new Play();
        play1.compNumber.setValue();
        play1.userNumber.setValue();
        while (play1.CountBulls() < play1.userNumber.DEFAULT_AMOUNT || play1.CountCows() != 0) {
            play1.play();
        }

        System.out.println("You won!!!");
        System.out.println("Computer set up following number: ");
        play1.compNumber.getValue();


    }


}


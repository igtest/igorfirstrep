package com.cowandbullsgame;

public class Play {

    public CompNumber compNumber = new CompNumber();
    public UserNumber userNumber = new UserNumber();

    public void play() {

        System.out.println("The number of bulls: " + CountBulls());
        System.out.println("The number of cows: " + CountCows());
        System.out.println("Try again!");
        userNumber.setValue();

    }

    public int CountBulls() {
        int bull = 0;

        for (int i = 0; i < userNumber.DEFAULT_AMOUNT; i++) {
            if (userNumber.bufComp[i] == compNumber.bufComp[i]) {
                bull++;
            }
            if (bull == userNumber.DEFAULT_AMOUNT) {
                return userNumber.DEFAULT_AMOUNT;
            }
        }
        return bull;
    }

    public int CountCows() {
        int cows = 0;

        for (int i = 0; i < compNumber.bufComp.length; i++) {
            for (int j = 0; j < userNumber.bufComp.length; j++) {
                if (compNumber.bufComp[j] == userNumber.bufComp[i]) {
                    cows++;
                    break;
                }
            }
        }

        int totalCows = cows - CountBulls();
        return totalCows;
    }

}

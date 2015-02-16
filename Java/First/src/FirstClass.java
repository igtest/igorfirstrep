import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/**
 * Created by User on 13.02.2015.
 */
public class FirstClass {

    public void GuessNumber() {
        Random random = new Random();
        int randomInt = random.nextInt(100);
        int flag = 0;
        int count = 0;
        while (flag == 0) {
            System.out.println("Input your value: ");
            count++;
            int value = 0;
            Scanner sc = new Scanner(System.in);
            if (sc.hasNextInt()) {
                value = sc.nextInt();
                if (value > randomInt) {
                    System.out.println("Your value is bigger");
                    continue;
                }
                if (value < randomInt) {
                    System.out.println("Your value is less");
                    continue;
                }
                if (value == randomInt) {
                    System.out.println("You are guess!!!");
                    flag = 1;
                }
            } else {
                System.out.println("It isn't number");
            }

        }
        System.out.println("I think of a number " + randomInt);
        System.out.printf("You made " + count + " attempts");
    }

    public void GuessNumberPythonWay() {
        Random random = new Random();
        int randomInt = random.nextInt(100);
        int flag = 0;
        int count = 0;
        while (flag == 0) {
            System.out.println("Input your value: ");
            count++;
            int value = InputInt();
            if (value > randomInt) {
                System.out.println("Your value is bigger");
                continue;
            }
            if (value < randomInt) {
                System.out.println("Your value is less");
                continue;
            }
            if (value == randomInt) {
                System.out.println("You are guess!!!");
                flag = 1;
            }
        }
        System.out.println("I think of a number " + randomInt);
        System.out.printf("You made " + count + " attempts");
    }

    private int InputInt() {
        int value = 0;
        while (true) {
            Scanner sc = new Scanner(System.in);
            if (sc.hasNextInt()) {
                value = sc.nextInt();
                return value;
            } else {
                System.out.println("You should input a number!");
            }
        }
    }

    private ArrayList<Integer> PrimeNumbers(int n) {

        ArrayList<Integer> array = new ArrayList<Integer>(0);
        ArrayList<Integer> array_temp = new ArrayList<Integer>(0);
        for (int i = 2; i <= n; i++) {
            array.add(i);
        }
        int firstCount = 0;
        while (true) {
            int num = array.get(firstCount);
            firstCount++;
            if (firstCount >= array.size()) {
                break;
            }
            int secondCount = 1;
            while (secondCount <= array.size()) {
                secondCount++;
                int key = secondCount * num;
                if (key > max(array)) {
                    break;
                }
                if (array_temp.indexOf(key) != -1) {
                    continue;
                }
                array_temp.add(key);
                int pos = array.indexOf(key);
                array.remove(pos);
            }
        }
        return array;
    }

    public void PrintPrimeNumber(int n) {
        ArrayList<Integer> array = new ArrayList<Integer>();
        array = PrimeNumbers(n);
        for (int i = 0; i < array.size(); i++) {
            System.out.println("" + array.get(i));
        }
    }

    private int max(ArrayList<Integer> array) {
        int max = array.get(0);
        for (int i = 0; i < array.size(); i++) {
            if (array.get(i) > max) {
                max = array.get(i);
            }
        }
        return max;
    }

    private int MaxPrimeNumber(int n) {
        ArrayList<Integer> array = new ArrayList<Integer>();
        array = PrimeNumbers(n);
        int maxNum = 0;
        for (int i = 0; i < array.size(); i++) {
            if (n % array.get(i) == 0) {
                maxNum = array.get(i);
            }
        }
        return maxNum;
    }

    public void PrintMaxNumber(int n) {
        System.out.println("" + MaxPrimeNumber(n));
    }

    private int fibo(int n) {
        int result = 0;
        if (n == 0) {
            result = 0;
        } else if (n == 1) {
            result = 1;
        } else {
            result = fibo(n - 1) + fibo(n - 2);
        }
        return result;
    }

    public void PrintFibo(int n) {
        System.out.println("Fibonacci number is " + fibo(n));
    }

    public static void main(String[] args) {
        FirstClass a = new FirstClass();
        a.PrintFibo(10);

    }
}

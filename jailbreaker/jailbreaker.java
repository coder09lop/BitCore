package jailbreaker;
import java.util.Scanner;



public class jailbreaker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("jailbraker 1 update 1.090.8");
        System.out.println("1. avvia jailbreaker");
        System.out.println("2. avvia jailbreaker con root");
        System.out.println("3. exit");
        String sc = scanner.nextLine();
        scanner.close();
        switch(sc) {
            case "1":
                System.out.println("avviando jailbreaker");
                System.out.println("avviando jailbreaker");
                simulateStartup();
                break;
            case "2":
                System.out.println("avviando jailbreaker con root");
                simulateStartupWithRoot();
                simulateLoadingWithRoot();
                break;
            case "3":
                System.out.println("ciao");
                break;
            default:
                System.out.println("non è un opzione valida!");
           
        }
        
    }
    private static void simulateStartup() {
        System.out.println("avviando jailbreaker...");
        simulateLoading();
        System.out.println("jailbreaker avviato");
    }
    private static void simulateStartupWithRoot() {
        System.out.println("avviando jailbreaker con root...");
        simulateLoading();
        System.out.println("jailbreaker avviato con root");
    }
    private static void simulateLoading() {
        for (int i = 0; i < 10; i++) {
            System.out.println(".");
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        System.out.println();
    }
    private static void simulateLoadingWithRoot() {
        for (int i = 0; i < 10; i++) {
            System.out.println(".");
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println();

    }

    } }

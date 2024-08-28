package engine;
import java.util.Scanner;
public class engine {

    public static void main(String[] args) {
        // Create a new instance of the Scanner class
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.println("Engine started wit");
        simulateLoading();
        System.out.println("Engine ver 1.90.8");
        System.out.println("Engine started with 1.90.8");
        System.out.println("write hello");
        scanner.nextLine();
        scanner.close();
    }
    @SuppressWarnings("unused")
    private static void simulateLoading() {
        for (int i = 0; i < 10; i++) {
        System.out.println("Loading...");
        try {
            Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                }
                }
           System.out.println();     } 
                
    }
                

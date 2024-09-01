package scripts;
import java.util.Scanner;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;




public class ScriptInstaller {

    public static void main(String[] args) {
        //scanner
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.println("scripts installing");
        SimulateLoading();
        System.out.println("scripts installed");
        System.out.println("continue installing scripts!");
        System.out.println("Y/n");
        String input = scanner.nextLine();
        switch (input) {
            case "y":
                System.out.println("installing scripts");
                SimulateLoading();
                System.out.println("scripts installed");
                break;
            case "n":
                System.out.println("installation cancelled");
            default:
                System.out.println("invalid input");
        }
        
        
    }
    
    private static void SimulateLoading() {
        ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();
        @SuppressWarnings("unused")
        Runnable loadingTask = () -> System.out.println("Loading...");
        executor.scheduleAtFixedRate(loadingTask, 0, 1, TimeUnit.SECONDS);
        try {
            
                Thread.sleep(1000);
                } catch (InterruptedException e) {
                    }
                executor.shutdown();
            

        }    


    }

    



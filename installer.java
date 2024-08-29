import java.util.Scanner;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;








public class installer {
    public static void main(String[] args) {
        // Create a new instance of the installer
        System.out.println("welcome to the BitCore installer");
        System.out.println("Please select an option:");
        System.out.println("1. Install BitCore");
        System.out.println("2. Uninstall BitCore");
        System.out.println("3. Update BitCore");
        System.out.println("4. Exit");
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        int choice = scanner.nextInt();
            switch (choice) {
                case 1 -> {
                    System.out.println("Installing BitCore...");
                    System.out.println("Please wait...");
                    SimulateLoading();
                    System.out.println("Installation complete!");
                    break;
            }
                case 2 -> {
                    System.out.println("Uninstalling BitCore...");
                    System.out.println("Please wait...");
                    SimulateLoading();
                    break;
                }
                case 3 -> {
                    System.out.println("Updating BitCore...");
                    System.out.println("Please wait...");
                    SimulateLoading();
                    break;
                }
                case 4 -> {
                    System.out.println("Exiting...");
                    System.exit(0);
                    break;
                }
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

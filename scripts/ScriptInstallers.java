package scripts;
import java.util.Scanner;
public class ScriptInstallers {
    public static void main(String[] args) {
        new ScriptInstaller();
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of scripts you want to install:");
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.println("Enter the name of the script:");
            String name = scanner.next();
            System.out.println("Enter the version of the script:");
            String version = scanner.next();
            System.out.println("Enter the location of the script:");
            String location = scanner.next();
            // Create a new ScriptInstaller object and call the installScript method
            ScriptInstaller installer = new ScriptInstaller();
            installer.installScript(name, version, location);
            }
            
    }
}

import java.util.Scanner;
import java.util.regex.Matcher;
@SuppressWarnings("unused")

//inizio programma

public class installer {
   public static void ma6in(String[] args) {
    // Create a new Scanner object
    Scanner scanner = new Scanner(System.in);
    System.out.println("benvenuto nella hacker box ");
    System.out.println("inserisci il tuo nome");
    String nome = scanner.nextLine();
    scanner.close();
    switch(nome) {
        case "hacker":
        System.out.println("benvenuto hacker");
        break;
        case "oms":
        System.out.println("benvenuto oms");
        System.out.println("inserisci password");
        String oms = scanner.nextLine();
        scanner.close();
        if (oms == "password"); {
            System.out.println("acesso consentito");
            System.out.println("benvenuto nell pannello di controllo");
            System.out.println("inserisci comando");
        }
        break;
        default:
        System.out.println("benvenuto");
        System.out.println(nome);
        System.out.println("scegli una password");
        String password = scanner.nextLine();
        scanner.close();
        switch(password) {
            case "password":
            System.out.println("password molto prevedibile");
            break;
            case "1234":
            System.out.println("password molto debole");
            break;
            default:
            System.out.println("password accettabile");
            System.out.println("ok possiamo continuare");
            System.out.println("ok user creato premi invio per usire");
            scanner.nextLine();
            scanner.close();
            break;
        }
        

    }
   }
}
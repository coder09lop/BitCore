package crash;

import java.io.File;

public class crash {
    public static void main(String[] args) {
      
        //create crash file
        File file = new File("crash.txt");
        try{
            file.createNewFile();
            }catch(Exception e){
                System.out.println("Error creating file");
                }
        }
    }


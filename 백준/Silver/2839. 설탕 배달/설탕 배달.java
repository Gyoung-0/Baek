import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sugar = Integer.parseInt(br.readLine());
        int count = 0;
        while (sugar > 0) {

            while(!((sugar%5) == 0)){
                sugar -= 3;
                count++;
                if(sugar == 0){ break;}
                else if(sugar < 0){
                    System.out.println(-1);
                    break;}
            }
            if(0 == sugar){
                System.out.println(count);
                break;
            }
            if(sugar > 0){
                count += sugar / 5;
                System.out.println(count);
                break;
            }
        }
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        for(int i = 0 ; i < T ; i++){
            int n = Integer.parseInt(br.readLine());
            if(n != 0) stack.push(n);
            else stack.pop();
        }
        int sum = 0;
        for(int i : stack){
            sum += i;
        }
        System.out.println(sum);
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for(int i = 0; i < T; i++) {
            String PS = br.readLine();
            Queue<String> queue = new LinkedList<>();
            boolean found = false;
            for (int j = 0; j < PS.length(); j++) {
                char current = PS.charAt(j);
                if (current == '(') {
                    queue.offer(String.valueOf(current));
                } else if (current == ')') {
                    if (queue.isEmpty()) {
                        found = true;
                        break;
                    } else queue.poll();
                }
            }
            if (queue.isEmpty() && !found ) {
                System.out.println("YES");
            }else System.out.println("NO");
        }

    }
}
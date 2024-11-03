import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack();

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            if(s.equals("push")){
                stack.push(Integer.parseInt(st.nextToken()));
            }
            else if(s.equals("pop")){
                if(stack.isEmpty()){
                    System.out.println("-1");
                    continue;
                }
                System.out.println(stack.pop());
            }
            else if(s.equals("top")){
                if(stack.isEmpty()){
                    System.out.println("-1");
                    continue;
                }
                System.out.println(stack.peek());
            }
            else if(s.equals("empty")){
                if(stack.isEmpty()){
                    System.out.println("1");
                    continue;
                }
                System.out.println("0");
            }
            else if(s.equals("size")){
                System.out.println(stack.size());
            }
        }
    }
}
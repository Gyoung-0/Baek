import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            if(s.equals("push")){
                queue.offer(Integer.parseInt(st.nextToken()));
            }
            else if(s.equals("pop")){
                if(queue.isEmpty()){
                    System.out.println("-1");
                    continue;
                }
                System.out.println(queue.poll());
            }
            else if(s.equals("front")){
                if(queue.isEmpty()){
                    System.out.println("-1");
                    continue;
                }
                System.out.println(queue.peekFirst());
            }
            else if(s.equals("back")){
                if(queue.isEmpty()){
                    System.out.println("-1");
                    continue;
                }
                System.out.println(queue.peekLast());
            }
            else if(s.equals("empty")){
                if(queue.isEmpty()){
                    System.out.println("1");
                    continue;
                }
                System.out.println("0");
            }
            else if(s.equals("size")){
                System.out.println(queue.size());
            }
        }
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<>();
        Deque<Integer> deque = new ArrayDeque<>();

        for(int i = 0; i < N; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }
        double T = N;
        int round = (int)Math.round(T*0.3/2);
        Collections.sort(list);

        for(int i = 0; i < list.size(); i++){
            deque.offer(list.get(i));
        }

        for(int i = 0; i < round; i++) {
            deque.removeFirst();
            deque.removeLast();
        }
        double sum=0;
        for(int i : deque){
            sum+=i;
        }

        System.out.println( (int)Math.round(sum/deque.size()));
    }
}


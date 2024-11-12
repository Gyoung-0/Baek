import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());


        for(int i=0; i < T; i++){
            Queue<Print> queue = new LinkedList<>();
            StringTokenizer st =new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++){
                queue.offer(new Print(j, Integer.parseInt(st.nextToken())));
            }
            int count = 0;
            while(!queue.isEmpty()){
                Print current = queue.poll();
                boolean hasHighPriority = false;

                for(Print P : queue){
                    if(P.priority > current.priority){
                        hasHighPriority = true;
                        break;
                    }
                }
                if(hasHighPriority){
                    queue.offer(current);
                } else{
                    count++;
                    if(M == current.index){
                        System.out.println(count);
                        break;
                    }
                }

            }
        }

    }
    static class Print{
        int index;
        int priority;
        public Print(int index, int priority){
            this.index = index;
            this.priority = priority;
        }
    }
}
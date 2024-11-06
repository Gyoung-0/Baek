import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<Integer> list = new ArrayList<>();

        for(int i=0; i<N; i++){
            list.add(i+1);
        }
        int count = 0;
        sb.append("<");
        while(!list.isEmpty()){
            count = (count+K-1)%list.size();
            if(list.size() == 1) {
                sb.append(list.remove(count)).append(">");
                break;
            }
            sb.append(list.remove(count)).append(", ");
        }

        System.out.println(sb);
    }
}
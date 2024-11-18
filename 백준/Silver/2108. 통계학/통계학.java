import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int[] N = new int[T];
        for(int i = 0 ; i < T; i++){
            N[i] = Integer.parseInt(br.readLine());
        }

        Statistics st = new Statistics(N);

        System.out.println(st.arithmeticMean);
        System.out.println(st.median);
        System.out.println(st.mode);
        System.out.println(st.range);

    }
    static class Statistics{

        int arithmeticMean;
        int median;
        int mode = 0;
        int range;

        Map<Integer, Integer> map = new HashMap<>();

        Statistics(int[] list){

            Arrays.sort(list);

            for(int i : list){
                this.arithmeticMean += i;

                map.put(i, map.getOrDefault(i, 0) + 1);
            }

            arithmeticMean = (int)Math.round((double) arithmeticMean / (double) list.length);
            this.median = list[list.length/2];


            // 최빈값 계산
            int maxFrequency = 0;
            List<Integer> modes = new ArrayList<>();

            for (int key : map.keySet()) {
                int frequency = map.get(key);
                if (frequency > maxFrequency) {
                    maxFrequency = frequency;
                    modes.clear();
                    modes.add(key);
                } else if (frequency == maxFrequency) {
                    modes.add(key);
                }
            }
            
            if (modes.size() > 1) {
                Collections.sort(modes);
                this.mode = modes.get(1);
            } else {
                this.mode = modes.get(0);
            }

            this.range = Math.abs(list[0] - list[list.length-1]);

        }
    }
}
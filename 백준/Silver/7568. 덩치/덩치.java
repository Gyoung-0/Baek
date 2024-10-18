import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int people = Integer.parseInt(br.readLine());

        List<Body> bodyList = new ArrayList<>();

        for (int i = 0; i < people; i++) {
            String[] input = br.readLine().split(" ");
            int height = Integer.parseInt(input[0]);
            int weight = Integer.parseInt(input[1]);

            bodyList.add(new Body(height, weight));
        }

        // 각 사람의 등수를 저장할 배열
        int[] rank = new int[people];
        Arrays.fill(rank, 1);  // 기본 등수는 1등으로 설정

        // 몸무게와 키를 비교하여 등수 매기기
        for (int i = 0; i < people; i++) {
            Body current = bodyList.get(i);
            for (int j = 0; j < people; j++) {
                if (i != j) {
                    Body compare = bodyList.get(j);
                    // 키와 몸무게가 둘 다 큰 경우에만 등수를 증가
                    if (compare.height > current.height && compare.weight > current.weight) {
                        rank[i]++;
                    }
                }
            }
        }

        // 결과 출력
        for (int r : rank) {
            System.out.print(r + " ");
        }
    }
}

class Body {
    int height;
    int weight;

    Body(int h, int w) {
        this.height = h;
        this.weight = w;
    }
}
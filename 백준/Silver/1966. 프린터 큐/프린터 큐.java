import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken()); // 문서의 개수
            int M = Integer.parseInt(st.nextToken()); // 추적할 문서의 인덱스

            Queue<Print> queue = new LinkedList<>();
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                queue.offer(new Print(j, Integer.parseInt(st.nextToken()))); // 문서 추가
            }

            int count = 0;

            while (!queue.isEmpty()) {
                Print current = queue.poll();
                boolean hasHigherPriority = false;

                // 현재 문서보다 우선순위가 높은 문서가 있는지 확인
                for (Print p : queue) {
                    if (p.priority > current.priority) {
                        hasHigherPriority = true;
                        break;
                    }
                }

                if (hasHigherPriority) {
                    // 우선순위가 높은 문서가 있으면 현재 문서를 다시 큐에 넣음
                    queue.offer(current);
                } else {
                    // 현재 문서를 출력
                    count++;
                    if (current.index == M) {
                        System.out.println(count);
                        break;
                    }
                }
            }
        }
    }

    // Print 클래스 정의
    static class Print {
        int index;
        int priority;

        public Print(int index, int priority) {
            this.index = index;
            this.priority = priority;
        }
    }
}
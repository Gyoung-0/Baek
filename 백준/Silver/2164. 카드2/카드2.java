import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Queue<Integer> queue = new LinkedList<>();
        int N = Integer.parseInt(br.readLine());

        // 1~N까지 차례대로 삽입
        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }

        // 차례대로 한장 버리고 그 뒷장 맨 뒤로
        while (queue.size() > 1) {
            queue.poll(); // 맨 앞 숫자 버리기
            int back = queue.poll(); // 그 다음 숫자 꺼내기
            queue.offer(back); // 꺼낸 숫자를 큐의 뒤로 다시 넣기
        }

        // 마지막 남은 숫자 출력
        System.out.println(queue.poll());
    }
}
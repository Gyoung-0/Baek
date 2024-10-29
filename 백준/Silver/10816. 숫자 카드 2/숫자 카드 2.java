import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 카드 개수 읽기
        int T = Integer.parseInt(br.readLine());

        // 카드 입력받고 개수 저장
        Map<Integer, Integer> cardCount = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < T; i++) {
            int card = Integer.parseInt(st.nextToken());
            cardCount.put(card, cardCount.getOrDefault(card, 0) + 1);
        }

        // 확인할 카드 개수
        T = Integer.parseInt(br.readLine());
        
        // 확인할 카드 리스트를 순회하며 개수 출력
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            int haveCard = Integer.parseInt(st.nextToken());
            sb.append(cardCount.getOrDefault(haveCard, 0)).append(" ");
        }
        
        System.out.println(sb.toString().trim());
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sugar = Integer.parseInt(br.readLine());
        Delievery delievery = new Delievery();

        delievery.calculate(sugar, 0); // 재귀 호출로 나눌 수 있는지 확인

        if (delievery.flag) {
            System.out.println(delievery.count); // 최소 봉지 수 출력
        } else {
            System.out.println(-1); // 나눌 수 없는 경우
        }
    }

    static class Delievery {
        final int FIVE = 5;
        final int THREE = 3;
        int count = Integer.MAX_VALUE; // 최소 봉지 수를 구하기 위해 초기값을 매우 크게 설정
        boolean flag = false; // 나눌 수 있는지 여부를 확인하는 플래그

        // 재귀적으로 설탕 나누기 계산
        public void calculate(int x, int currentCount) {
            if (flag) return;  // 이미 가능한 경우를 찾았으면 종료

            if (x == 0) { // 정확하게 나눌 수 있는 경우
                flag = true; // 나눌 수 있음을 표시
                count = Math.min(count, currentCount); // 최소 봉지 수 갱신
                return;
            }
            if (x < 0) return; // 설탕이 음수가 되면 더 이상 나눌 수 없음

            // 5kg 봉지를 하나 사용하는 경우
            calculate(x - FIVE, currentCount + 1);
            // 3kg 봉지를 하나 사용하는 경우
            calculate(x - THREE, currentCount + 1);
        }
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String s = br.readLine();
            if (s.equals(".")) return;  // 입력 종료 조건
            
            Stack<Character> stack = new Stack<>();
            boolean valid = true;

            for (int i = 0; i < s.length(); i++) {
                char ch = s.charAt(i);

                // 여는 괄호는 스택에 추가
                if (ch == '(' || ch == '[') {
                    stack.push(ch);
                }
                // 닫는 괄호는 짝이 맞는지 확인하고 스택에서 제거
                else if (ch == ')') {
                    if (stack.isEmpty() || stack.pop() != '(') {
                        valid = false;
                        break;
                    }
                } else if (ch == ']') {
                    if (stack.isEmpty() || stack.pop() != '[') {
                        valid = false;
                        break;
                    }
                }
            }

            // 스택이 비어 있지 않다면 짝이 맞지 않음
            if (!stack.isEmpty()) valid = false;

            // 결과 출력
            if (valid) System.out.println("yes");
            else System.out.println("no");
        }
    }
}
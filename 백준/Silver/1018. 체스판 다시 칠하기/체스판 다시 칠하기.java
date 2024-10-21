import java.io.*;
import java.util.*;
public class Main {
    static char[][] board;
    public static void main(String[] args) throws IOException {
        //시작이 B면 홀수번째 시작은 B 짝수번째 시작은 W , 시작이 W면 반대
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        board = new char[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            board[i] = line.toCharArray();
        }

        int minPaint = Integer.MAX_VALUE;

        for (int i = 0; i < n-7; i++) {
            for (int j = 0; j < m-7; j++) {
                minPaint = Math.min(minPaint, findMinPaint(i,j));
            }
        }
        System.out.println(minPaint);
    }
    static int findMinPaint(int startX, int startY) {
        int countB = 0; // 시작이 B
        int countW = 0; // 시작이 W
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if( (i+j) % 2 == 0){
                    if(board[startX+i][startY+j] != 'B') countB++;
                    if(board[startX+i][startY+j] != 'W') countW++;
                }else{
                    if(board[startX+i][startY+j] != 'B') countW++;
                    if(board[startX+i][startY+j] != 'W') countB++;
                }
            }
        }
        return Math.min(countW, countB);
    }
}






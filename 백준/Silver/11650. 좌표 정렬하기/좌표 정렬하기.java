import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Coordinate> list = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            list.add(new Coordinate(x, y));
        }
        list.sort((a,b)->{
            if(a.x==b.x) return a.y - b.y;
            else return a.x - b.x;
        });
        for(Coordinate c : list) {
            System.out.println(c.x + " " + c.y);
        }

    }
    static class Coordinate{
        int x;
        int y;
        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}



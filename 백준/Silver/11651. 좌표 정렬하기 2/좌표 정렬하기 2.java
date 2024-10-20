import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Coordinate> coordinates = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            coordinates.add(new Coordinate(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        coordinates.sort((a,b)->{
           if(a.y == b.y) return a.x - b.x;
           return a.y - b.y;
        });

        for(Coordinate c : coordinates){
            System.out.println(c.x + " " + c.y);
        }
    }
}

class Coordinate {
    int x;
    int y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}



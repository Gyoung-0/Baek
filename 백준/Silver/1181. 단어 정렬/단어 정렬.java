import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<String> tokens = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] lineTokens = br.readLine().split(" ");
            Collections.addAll(tokens, lineTokens);
        }

        Collections.sort(tokens, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.length() == s2.length()) {
                    return s1.compareTo(s2);
                }
                return s1.length() - s2.length();
            }
        });
        String d = "";

        for (String token : tokens) {

            if(token.equals(d)){
                continue;
            }
            System.out.println(token);
            d = token;
        }
    }
}
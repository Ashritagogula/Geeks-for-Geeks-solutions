import java.util.*;

class Solution {

    public static void pb(ArrayDeque<Integer> dq, int x) {
        dq.addLast(x);
    }

    public static void ppb(ArrayDeque<Integer> dq) {
        if (!dq.isEmpty()) dq.removeLast();
    }

    public static int front_dq(ArrayDeque<Integer> dq) {
        if (!dq.isEmpty()) return dq.peekFirst();
        return -1;
    }

    public static void pf(ArrayDeque<Integer> dq, int x) {
        dq.addFirst(x);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        int q = sc.nextInt(); // number of queries
        sc.nextLine(); // consume newline

        for (int i = 0; i < q; i++) {
            String line = sc.nextLine();
            String[] parts = line.split(" ");

            switch (parts[0]) {
                case "pb":
                    pb(dq, Integer.parseInt(parts[1]));
                    break;
                case "pf":
                    pf(dq, Integer.parseInt(parts[1]));
                    break;
                case "pp_b":
                    ppb(dq);
                    break;
                case "f":
                    System.out.println(front_dq(dq));
                    break;
            }
        }
        sc.close();
    }
}

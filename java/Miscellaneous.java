import java.util.HashMap;
import java.util.HashSet;

public class Miscellaneous {

    public static int locate_fibonacci_diff(final int n) {
        if (n < 1)
            return -1;
        if (n == 1)
            return 0;

        int i = 1;
        int j = 1;
        while (j < n) {
            int temp = i;
            i = j;
            j = temp + i;
        }
        if (j == n)
            return 0;
        return j - n < n - i ? j - n : n - i;
    }

    public static int get_prime(final int n) {
        if (n <= 1)
            return -1;

        HashSet<Integer> primes = new HashSet<Integer>();

        for (int i = 2; i <= n; i++) {
            boolean prime = true;

            for (int key : primes) {
                if (i % key == 0) {
                    prime = false;
                    break;
                }
            }
            if (!prime)
                continue;
            primes.add(i);
        }
        int max = 0;
        for (Integer integer : primes) {
            if (max < integer)
                max = integer;
        }
        return max;
    }

    public static void main(String[] args) {
        int n = get_prime(10000);
        System.out.println(n);
    }
}
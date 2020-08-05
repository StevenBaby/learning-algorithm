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

    public static void main(String[] args) {
        int n = locate_fibonacci_diff(100);
        System.out.println(n);
    }
}
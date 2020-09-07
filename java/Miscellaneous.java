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

    public static void counter_print() {
        int[][] array = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 }, { 13, 14, 15, 16 } };
        int top = 0;
        int bottom = array.length - 1;
        int left = 0;
        int right = array[0].length - 1;
        int counter = 0;
        int total = array.length * array[0].length;

        int i = 0;
        int j = 0;
        while (counter < total) {
            j = left;
            i = top;

            while (j <= right) {
                System.out.print(array[i][j++] + ", ");
                counter++;
            }
            top++;

            i = top;
            j = right;

            while (i <= bottom) {
                System.out.print(array[i++][j] + ", ");
                counter++;
            }
            right--;

            j = right;
            i = bottom;

            while (j >= left) {
                System.out.print(array[i][j--] + ", ");
                counter++;
            }
            bottom--;

            i = bottom;
            j = left;
            while (i >= top) {
                System.out.print(array[i--][j] + ", ");
                counter++;
            }
            left++;
        }
    }

    public static void pick_numbers(int[] array) {
        int even = -1;
        int odd = -1;
        for (int i = 0; i < array.length; i++) {
            if (even < 0 && array[i] % 2 == 1)
                continue;
            if (even < 0 && array[i] % 2 == 0) {
                even = i;
                continue;
            }

            assert (even >= 0);

            if (odd < 0 && array[i] % 2 == 0)
                continue;
            if (odd < 0 && array[i] % 2 == 1) {
                odd = i;
            }
            assert (odd >= 0);

            int temp = array[odd];
            while (odd - 1 >= even) {
                array[odd] = array[odd - 1];
                odd--;
            }
            array[even] = temp;
            odd = -1;
            even = i;
        }
    }

    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 4, 5 };
        Sort.print(array);
        pick_numbers(array);
        Sort.print(array);

    }
}
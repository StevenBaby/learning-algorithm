import java.util.Random;
import java.util.Stack;

public class Sort {

    public static void shuffle(final int[] array) {
        Random rand = new Random();
        int index = 0;
        for (int i : array) {
            int rand_index = rand.nextInt(array.length);
            int temp = array[rand_index];
            array[rand_index] = array[index];
            array[index] = temp;
            index++;
        }
    }

    public static void print(final int[] array) {
        int index = 1;
        for (int i : array) {
            if (index++ < array.length)
                System.out.print(i + ", ");
            else
                System.out.print(i);
        }
        System.out.println();
    }

    public static int[] create(int length) {
        int[] array = new int[length];
        int index = 0;
        for (int i : array) {
            array[index++] = index;
        }
        Sort.shuffle(array);
        return array;
    }

    public static void shift(final int[] array, int count) {
        if (array == null || array.length == 0)
            return;
        int length = array.length;
        count %= length;
        if (count <= 0)
            return;

        int pivot = 0;
        int save = 0;
        int move = 0;
        int counter = 0;
        int loop = 1;

        for (int i = length - 1; counter < length; i--) {
            pivot = array[i];
            save = i;
            loop = 1;
            while (counter < length && loop != 0) {
                move = save - count;
                if (move < 0)
                    move += array.length;

                array[save] = array[move];
                save = move;

                counter++;
                loop = (counter * count + count) % length;
            }
            counter++;
            array[save] = pivot;
        }
    }

    public static void bubble(final int[] array, boolean reverse) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 1; j < array.length - i; j++) {
                int diff = array[j] - array[j - 1];
                if ((!reverse && diff < 0) || (reverse && diff > 0)) {
                    int temp = array[j];
                    array[j] = array[j - 1];
                    array[j - 1] = temp;
                }
            }
        }
    }

    public static void select(final int[] array, boolean reverse) {
        if (array == null || array.length == 0)
            return;

        int index = 0;
        int swap = 0;

        for (int i = 0; i < array.length; i++) {
            index = 0;
            swap = array.length - i - 1;
            for (int j = 1; j < array.length - i; j++) {
                int diff = array[index] - array[j];
                if ((!reverse && diff < 0) || (reverse && diff > 0)) {
                    index = j;
                }
            }

            if (index != swap) {
                final int temp = array[index];
                array[index] = array[swap];
                array[swap] = temp;
            }
        }
    }

    public static void insert(final int[] array, boolean reverse) {
        if (array == null || array.length == 0)
            return;
        for (int i = 1; i < array.length; i++) {
            int pivot = array[i];
            int j = i;
            for (; j > 0; j--) {
                int diff = pivot - array[j - 1];
                if ((!reverse && diff > 0) || (reverse && diff < 0)) {
                    break;
                }
                array[j] = array[j - 1];
            }
            array[j] = pivot;
        }
    }

    public static void shell(final int[] array, boolean reverse) {
        if (array == null || array.length == 0)
            return;
        int step = array.length / 2;
        while (step >= 1) {
            for (int i = step; i < array.length; i++) {
                int pivot = array[i];
                int j = i;
                for (; j - step >= 0; j -= step) {
                    int diff = pivot - array[j - step];
                    if ((!reverse && diff > 0) || (reverse && diff < 0)) {
                        break;
                    }
                    array[j] = array[j - step];
                }
                array[j] = pivot;
            }
            step /= 2;
        }
    }

    private static void _quick_sort(final int[] array, int start, int end, boolean reverse) {
        if (start >= end)
            return;
        int pivot = array[start];

        int high = end - 1;
        int low = start;
        int diff = 0;

        while (low < high) {
            diff = array[high] - pivot;
            while (low < high && ((!reverse && diff > 0) || (reverse && diff < 0))) {
                high--;
                diff = array[high] - pivot;
            }

            array[low] = array[high];

            diff = pivot - array[low];
            while (low < high && ((!reverse && diff > 0) || (reverse && diff < 0))) {
                low++;
                diff = pivot - array[low];
            }

            array[high] = array[low];
        }
        array[low] = pivot;
        Sort._quick_sort(array, start, low, reverse);
        Sort._quick_sort(array, low + 1, end, reverse);
    }

    public static void quick(final int[] array, boolean reverse) {
        if (array == null || array.length == 0)
            return;
        Sort._quick_sort(array, 0, array.length, reverse);
    }

    private static void _merge_array(final int[] array, int low, int mid, int high, boolean reverse) {
        int[] clone = array.clone();
        int i = low;
        int j = mid;
        int index = low;

        while (i < mid && j < high) {
            int diff = clone[i] - clone[j];
            if ((!reverse && diff < 0) || (reverse && diff >= 0)) {
                array[index++] = clone[i++];
            } else {
                array[index++] = clone[j++];
            }
        }
        while (i < mid) {
            array[index++] = clone[i++];
        }
        while (j < high) {
            array[index++] = clone[j++];
        }
    }

    private static void _merge_sort(final int[] array, int low, int high, boolean reverse) {
        if (high - low <= 1)
            return;
        int mid = (low + high) / 2;
        Sort._merge_sort(array, low, mid, reverse);
        Sort._merge_sort(array, mid, high, reverse);
        Sort._merge_array(array, low, mid, high, reverse);
    }

    public static void merge(final int[] array, boolean reverse) {
        // merge sort recursive
        if (array == null || array.length <= 1)
            return;
        Sort._merge_sort(array, 0, array.length, reverse);
    }

    public static void merge_stack(final int[] array, boolean reverse) {
        if (array == null || array.length <= 1)
            return;

        final class MergeItem {
            public int low = 0;
            public int high = 0;
            public int mid = 0;
            public boolean pushed = false;

            MergeItem(int low, int high) {
                this.low = low;
                this.high = high;
                this.mid = (low + high) / 2;
            }
        }

        Stack<MergeItem> stack = new Stack<MergeItem>();
        stack.push(new MergeItem(0, array.length));

        while (!stack.empty()) {
            MergeItem item = stack.peek();
            if (item.high - item.low <= 1) {
                stack.pop();
                continue;
            }
            if (!item.pushed) {
                stack.push(new MergeItem(item.low, item.mid));
                stack.push(new MergeItem(item.mid, item.high));
                item.pushed = true;
                continue;
            }
            Sort._merge_array(array, item.low, item.mid, item.high, reverse);
            stack.pop();
        }
    }

    public static void merge_iterate(final int[] array, boolean reverse) {
        if (array == null || array.length == 0)
            return;
        for (int segment = 1; segment < array.length; segment *= 2) {
            for (int low = 0; low < array.length; low += segment * 2) {
                int mid = low + segment;
                int high = mid + segment;
                Sort._merge_array(array, low, mid, high, reverse);
            }
        }
    }

    private static void adjust_heap(final int[] array, int low, int high, boolean reverse) {
        int dad = low;
        int son = dad * 2 + 1;

        while (son < high) {
            if (son + 1 < high) {
                int diff = array[son] - array[son + 1];
                if ((!reverse && diff < 0) || (reverse && diff > 0))
                    son++;
            }
            int diff = array[son] - array[dad];
            if ((!reverse && diff < 0) || (reverse && diff > 0))
                return;

            int temp = array[son];
            array[son] = array[dad];
            array[dad] = temp;
            dad = son;
            son = dad * 2 + 1;
        }
    }

    public static void heap(final int[] array, boolean reverse) {
        for (int i = array.length / 2 - 1; i >= 0; i--) {
            Sort.adjust_heap(array, i, array.length, reverse);
        }

        for (int i = array.length - 1; i >= 0; i--) {
            int temp = array[0];
            array[0] = array[i];
            array[i] = temp;
            Sort.adjust_heap(array, 0, i, reverse);
        }
    }

    public static void main(String[] args) {
        int length = 32;
        int[] array = Sort.create(length);
        Sort.print(array);
        Sort.merge_stack(array, true);
        Sort.print(array);
    }
}
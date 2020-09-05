
public class BinaryTree {

    static public void build_tree(int[] tree, int index, int[] first, int findex, int[] middle, int mindex,
            int length) {
        tree[index] = first[findex];
        int root = tree[index];
        int delta = 0;
        for (int i = mindex; i < length; i++) {
            if (middle[i] == root) {
                delta = i - mindex;
                break;
            }
        }

        if (delta != 0) { // left not empty
            build_tree(tree, (index * 2) + 1, first, findex + 1, middle, mindex, mindex + delta);
        }
        if (mindex + delta + 1 < length) { // right not empty
            build_tree(tree, (index * 2) + 2, first, findex + delta + 1, middle, mindex + delta + 1, length);
        }
    }

    public static void main(String[] args) {
        int[] tree = new int[15];
        int[] first = { 1, 2, 4, 7, 3, 5, 6, 8 };
        int[] middle = { 4, 7, 2, 1, 5, 3, 8, 6 };

        Sort.print(tree);
        Sort.print(first);
        Sort.print(middle);
        BinaryTree.build_tree(tree, 0, first, 0, middle, 0, 8);
        Sort.print(tree);
    }
}
class Node {
    char type;              // 'L' = Leaf, 'H' = Horizontal, 'V' = Vertical
    String name;

    int minWidth;
    int minHeight;

    Node left;
    Node right;
    Node parent;

    Node(char type, String name) {
        this.type = type;
        this.name = name;
    }
}

public class SlicingFloorPlan {

    // Create a basic rectangle
    public static Node createRectangle(String name, int width, int height) {
        Node node = new Node('L', name);
        node.minWidth = width;
        node.minHeight = height;
        return node;
    }

    // Horizontal Cut
    public static Node horizontalCut(Node top, Node bottom) {
        Node node = new Node('H', "H");

        node.left = top;
        node.right = bottom;

        top.parent = node;
        bottom.parent = node;

        return node;
    }

    // Vertical Cut
    public static Node verticalCut(Node leftRect, Node rightRect) {
        Node node = new Node('V', "V");

        node.left = leftRect;
        node.right = rightRect;

        leftRect.parent = node;
        rightRect.parent = node;

        return node;
    }

    // Assign dimensions
    public static void assignDimensions(Node node, int width, int height) {
        if (node != null && node.type == 'L') {
            node.minWidth = width;
            node.minHeight = height;
        }
    }

    // Compact Floor Plan (Postorder Traversal)
    public static void compact(Node root) {

        if (root == null)
            return;

        if (root.type == 'L')
            return;

        compact(root.left);
        compact(root.right);

        if (root.type == 'H') {
            root.minWidth = Math.max(root.left.minWidth, root.right.minWidth);
            root.minHeight = root.left.minHeight + root.right.minHeight;
        } else { // Vertical
            root.minWidth = root.left.minWidth + root.right.minWidth;
            root.minHeight = Math.max(root.left.minHeight, root.right.minHeight);
        }
    }

    // Display Slicing Tree (Preorder)
    public static void displayTree(Node root) {

        if (root == null)
            return;

        if (root.type == 'L')
            System.out.print(root.name + " ");
        else
            System.out.print(root.type + " ");

        displayTree(root.left);
        displayTree(root.right);
    }

    public static void main(String[] args) {

        // Create Rectangles
        Node A = createRectangle("A", 3, 2);
        Node B = createRectangle("B", 4, 1);
        Node C = createRectangle("C", 2, 3);

        // Vertical Cut between A and B
        Node V1 = verticalCut(A, B);

        // Horizontal Cut with C
        Node root = horizontalCut(V1, C);

        // Compute minimum dimensions
        compact(root);

        // Display Tree
        System.out.print("Slicing Tree (Preorder): ");
        displayTree(root);

        // Display Final Dimensions
        System.out.println("\n\nCompacted Floor Plan:");
        System.out.println("Minimum Width  = " + root.minWidth);
        System.out.println("Minimum Height = " + root.minHeight);
    }
}
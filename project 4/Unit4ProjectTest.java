import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class Unit4ProjectTest {
    @Test
    void findRoot() {
        Unit4Project app = new Unit4Project();
        assertNotNull(app.getRoot());
        assertEquals("Budget", app.getRoot().name);
        assertTrue(app.getRoot().children.isEmpty());
        System.out.println("PASS: Root node created successfully.");
    }

    @Test
    void treeContainsOnlyRootNode() {
        Unit4Project app = new Unit4Project();
        assertEquals(0, app.getRoot().children.size());
        assertTrue(app.contains(app.getRoot(), "Budget"));
        assertFalse(app.contains(app.getRoot(), "Food"));
    }

    @Test
    void addChildNodeToTree() {
        Unit4Project app = new Unit4Project();
        Unit4Project.TreeNode root = app.getRoot();
        app.addChild(root, "Food");
        assertTrue(app.contains(root, "Food"));
    }

    @Test
    void findNestedChild() {
        Unit4Project app = new Unit4Project();
        Unit4Project.TreeNode root = app.getRoot();
        app.addChild(root, "Housing");
        assertFalse(root.children.isEmpty());
        app.addChild(root.children.get(0), "Rent");
        assertTrue(app.contains(root, "Rent"));
    }

    @Test
    void returnFalseForMissingNode() {
        Unit4Project app = new Unit4Project();
        Unit4Project.TreeNode root = app.getRoot();
        app.addChild(root, "Housing");
        app.addChild(root, "Food");
        app.addChild(root.children.get(0), "Rent");
        app.addChild(root.children.get(0), "Utilities");
        assertFalse(app.contains(root, "Travel"));
    }

    @Test
    void addMultipleChildrenAndValidateStructure() {
        Unit4Project app = new Unit4Project();
        Unit4Project.TreeNode root = app.getRoot();
        app.addChild(root, "Housing");
        app.addChild(root, "Food");
        app.addChild(root, "Transportation");
        assertEquals(3, root.children.size());
        assertTrue(app.contains(root, "Transportation"));
    }

    @Test
    void printPreOrderWithoutException() {
        Unit4Project app = new Unit4Project();
        Unit4Project.TreeNode root = app.getRoot();
        app.addChild(root, "Housing");
        app.addChild(root, "Food");
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        try {
            System.setOut(new PrintStream(output));
            assertDoesNotThrow(() -> app.printPreOrder(root));
        } finally {
            System.setOut(originalOut);
        }
        String result = output.toString();
        assertTrue(result.contains("Budget"));
        assertTrue(result.contains("Housing"));
        assertTrue(result.contains("Food"));
    }

    @Test
    void handlesNullAndRootOnlyEdgeCases() {
        Unit4Project app = new Unit4Project();
        Unit4Project.TreeNode root = app.getRoot();
        assertFalse(app.contains(null, "Budget"));
        assertTrue(app.contains(root, "Budget"));
        assertFalse(app.contains(root, "Travel"));
        System.out.println("PASS: Null and root-only edge cases handled correctly.");
    }
}

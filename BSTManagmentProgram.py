import os  # O(1) - Import statement execution.
import random  # O(1) - Import statement execution.

class BST:
    def __init__(self):
        self.root = None  # O(1) - Initialize the root of the BST to None.
        self.size = 0  # O(1) - Initialize the size of the tree to 0.

    def search(self, e):
        current = self.root  # O(1) - Start the search from the root.
        while current != None:  # O(h) - Traverse the tree until reaching a leaf (h is the height of the tree).
            if e < current.element:  # O(1) - Check if the element is less than the current node's element.
                current = current.left  # O(1) - Move to the left child.
            elif e > current.element:  # O(1) - Check if the element is greater than the current node's element.
                current = current.right  # O(1) - Move to the right child.
            else:  # O(1) - The element matches the current node's element.
                return True  # O(1) - Element is found, return True.
        return False  # O(1) - Element not found, return False.

    def countSearch(self, e):
        current = self.root  # O(1) - Start from the root.
        Count = 0  # O(1) - Initialize count of steps taken.
        while current != None:  # O(h) - Traverse until a leaf node is reached.
            if e < current.element:  # O(1) - If the search element is less, go left.
                current = current.left  # O(1) - Move to the left child.
                Count += 1  # O(1) - Increment the count.
            elif e > current.element:  # O(1) - If the search element is greater, go right.
                current = current.right  # O(1) - Move to the right child.
                Count += 1  # O(1) - Increment the count.
            else:  # O(1) - Element matches the current element.
                print(Count)  # O(1) - Output the count of steps taken.
                return Count  # O(1) - Return the count.
        print(Count)  # O(1) - Print the count when element is not found.

    def insert(self, e):
        if self.root == None:  # O(1) - Check if the tree is empty.
            self.root = self.createNewNode(e)  # O(1) - Create a new root node.
        else:
            parent = None  # O(1) - Initialize parent node.
            current = self.root  # O(1) - Start from the root.
            while current != None:  # O(h) - Find the correct insertion point.
                if e < current.element:  # O(1) - Go left if the element is less.
                    parent = current
                    current = current.left
                elif e > current.element:  # O(1) - Go right if the element is greater.
                    parent = current
                    current = current.right
                else:
                    return False  # O(1) - Element is a duplicate and not inserted.
            if e < parent.element:  # O(1) - Attach the new node to the left of the parent.
                parent.left = self.createNewNode(e)
            else:  # O(1) - Attach the new node to the right of the parent.
                parent.right = self.createNewNode(e)
        self.size += 1  # O(1) - Increment the size of the tree.
        return True  # O(1) - Return True as the element is successfully inserted.

    def createNewNode(self, e):
        return TreeNode(e)  # O(1) - Return a new TreeNode with the element e.

    def leaf_inorder(self):
        self.leaf_inorderHelper(self.root)  # O(n) - Start inorder traversal from the root to find leaf nodes.

    def leaf_inorderHelper(self, r):
        if r:  # O(1) - Check if the current node is not None.
            self.leaf_inorderHelper(r.left)  # O(n/2) - Recursively traverse the left subtree.
            if r.left is None and r.right is None:  # O(1) - Check if the node is a leaf node.
                print(r.element, end=" ")  # O(1) - Print the leaf node element.
            self.leaf_inorderHelper(r.right)  # O(n/2) - Recursively traverse the right subtree.

    def non_leaf_inorder(self):
        self.non_leaf_inorderHelper(self.root)  # O(n) - Start inorder traversal from the root to find non-leaf nodes.

    def non_leaf_inorderHelper(self, r):
        if r:  # O(1) - Check if the current node is not None.
            self.non_leaf_inorderHelper(r.left)  # O(n/2) - Recursively traverse the left subtree.
            if r.left is not None or r.right is not None:  # O(1) - Check if the node is not a leaf node.
                print(r.element, end=" ")  # O(1) - Print the non-leaf node element.
            self.non_leaf_inorderHelper(r.right)  # O(n/2) - Recursively traverse the right subtree.

    def inorder(self):
        self.inorderHelper(self.root)  # O(n) - Start inorder traversal from the root.

    def inorderHelper(self, r):
        if r:  # O(1) - Check if the current node is not None.
            self.inorderHelper(r.left)  # O(n/2) - Recursively traverse the left subtree.
            print(r.element, end=" ")  # O(1) - Print the element of the current node.
            self.inorderHelper(r.right)  # O(n/2) - Recursively traverse the right subtree.

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
        if r != None:  # O(1) - Check if current node is not None.
            self.inorderHelper(r.left)  # O(n/2) - Recursively traverse left subtree.
            print(r.element, end=" ")  # O(1) - Print the element of the current node.
            self.inorderHelper(r.right)  # O(n/2) - Recursively traverse right subtree.

    # Inorder traversal from a subtree that returns a list of elements
    def inorderHelperReturner(self, r):
        ReturnList = []  # O(1) - Initialize an empty list to collect elements.
        if r != None:  # O(1) - Check if current node is not None.
            self.inorderHelper(r.left)  # O(n/2) - Recursively collect elements from left subtree.
            ReturnList.append(r.element)  # O(1) - Append the current element.
            self.inorderHelper(r.right)  # O(n/2) - Recursively collect elements from right subtree.
        return ReturnList  # O(1) - Return the list of collected elements.

    # Inorder traversal from the root
    def inverse_inorder(self):
        self.inverse_inorderHelper(self.root)  # O(n) - Start inverse inorder traversal from the root.

    # Inverse Inorder traversal from a subtree
    def inverse_inorderHelper(self, r):
        if r != None:  # O(1) - Check if current node is not None.
            self.inverse_inorderHelper(r.right)  # O(n/2) - Recursively traverse right subtree.
            print(r.element, end=" ")  # O(1) - Print the element of the current node.
            self.inverse_inorderHelper(r.left)  # O(n/2) - Recursively traverse left subtree.

    # Postorder traversal from the root
    def postorder(self):
        self.postorderHelper(self.root)  # O(n) - Start postorder traversal from the root.

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
        if root != None:  # O(1) - Check if the subtree root is not None.
            self.postorderHelper(root.left)  # O(n/2) - Recursively traverse the left subtree.
            self.postorderHelper(root.right)  # O(n/2) - Recursively traverse the right subtree.
            print(root.element, end=" ")  # O(1) - Print the element after its children.

    # Preorder traversal from the root
    def preorder(self):
        self.preorderHelper(self.root)  # O(n) - Start preorder traversal from the root.

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
        if root != None:  # O(1) - Check if the current node is not None.
            print(root.element, end=" ")  # O(1) - Print the element of the current node.
            self.preorderHelper(root.left)  # O(n/2) - Recursively traverse the left subtree.
            self.preorderHelper(root.right)  # O(n/2) - Recursively traverse the right subtree.

    # Method to initiate the total preorder traversal from the root
    def total_preorder(self):
        if self.root is None:  # O(1) - Check if the tree is empty.
            print("The tree is empty.")  # O(1) - Notify that the tree is empty.
            return
        count = self.total_nodes_preorderHelper(self.root)  # O(n) - Calculate the total number of nodes using preorder traversal.
        print("\n\nTotal nodes in the subtree:", count)  # O(1) - Print the total count of nodes.

    # Helper function for total preorder traversal from a subtree
    def total_nodes_preorderHelper(self, root):
        if root is None:  # O(1) - Check if the current node is None.
            return 0  # O(1) - Return 0 if the subtree is empty.
        left_count = self.total_nodes_preorderHelper(root.left)  # O(n/2) - Recursively count nodes in the left subtree.
        right_count = self.total_nodes_preorderHelper(root.right)  # O(n/2) - Recursively count nodes in the right subtree.
        return 1 + left_count + right_count  # O(1) - Return the count of nodes including the current node.

        # Method to initiate depth calculation of the subtree rooted at a given node
    def depthSubtreeBST(self, e):
        # First, find the node containing the element
        current = self.root
        while current:
            if e < current.element:
                current = current.left  # O(log n) - Traverse left
            elif e > current.element:
                current = current.right  # O(log n) - Traverse right
            else:
                # Element is found, calculate depth
                depth = self.depthSubtreeBSTHelper(current)  # O(n) - Calculate depth
                print(depth)  # O(1) - Print depth
                return
        print("ERROR: Subtree rooted at node <N> not found!")  # O(1) - Error message if node not found

    # Helper method to calculate the depth of the subtree in a post-order style traversal
    def depthSubtreeBSTHelper(self, root):
        if root is None:
            return -1  # O(1) - Return -1 if subtree is empty
        left_depth = self.depthSubtreeBSTHelper(root.left)  # O(n/2) - Recursively get left depth
        right_depth = self.depthSubtreeBSTHelper(root.right)  # O(n/2) - Recursively get right depth
        return 1 + max(left_depth, right_depth)  # O(1) - Return depth of the subtree

    def deleteRec(self, root, key):
        if root is None:
            return root  # O(1) - Return None if tree is empty
        
        if key < root.element:
            root.left = self.deleteRec(root.left, key)  # O(log n) - Recur left
        elif key > root.element:
            root.right = self.deleteRec(root.right, key)  # O(log n) - Recur right
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right  # O(1) - Temp store right child
                root = None  # O(1) - Delete node
                return temp  # O(1) - Return the right child
            elif root.right is None:
                temp = root.left  # O(1) - Temp store left child
                root = None  # O(1) - Delete node
                return temp  # O(1) - Return the left child
            
            # Node with two children, get the inorder successor (smallest in the right subtree)
            temp = self.min_value_node(root.right)  # O(log n) - Find min value node in right subtree
            root.element = temp.element  # O(1) - Replace element with inorder successor
            root.right = self.deleteRec(root.right, temp.element)  # O(log n) - Delete inorder successor
        
        return root  # O(1) - Return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left  # O(log n) - Move to the leftmost node
        return current  # O(1) - Return the leftmost node

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0  # O(1) - Return true if size is zero

    # Remove all elements from the tree
    def clear(self):
        self.root = None  # O(1) - Reset the root to None
        self.size = 0  # O(1) - Reset size to zero

    # Return the root of the tree
    def getRoot(self):
        return self.root  # O(1) - Return the root of the tree
    
    # Method to find the depth of a node in the tree
    def findNodeDepth(self, e):
        current = self.root
        depth = 0
        while current is not None:
            if e < current.element:
                current = current.left  # O(log n) - Move left
                depth += 1  # O(1) - Increment depth
            elif e > current.element:
                current = current.right  # O(log n) - Move right
                depth += 1  # O(1) - Increment depth
            else:
                print(depth)  # O(1) - Print depth
                return
        print("ERROR: Node <N> not found!")  # O(1) - Print error if not found

    def insert(self, e):
        if self.root is None:
            self.root = TreeNode(e)  # O(1) - Insert the root node if tree is empty.
        else:
            parent = None
            current = self.root
            while current:
                parent = current  # O(1) - Update the parent node.
                if e < current.element:
                    current = current.left  # O(log n) - Traverse left if element is smaller.
                elif e > current.element:
                    current = current.right  # O(log n) - Traverse right if element is larger.
                else:
                    return False  # O(1) - Element is a duplicate, do not insert.
            if e < parent.element:
                parent.left = TreeNode(e)  # O(1) - Insert new node to the left.
            else:
                parent.right = TreeNode(e)  # O(1) - Insert new node to the right.
        self.size += 1  # O(1) - Increase the size of the tree.
        return True  # O(1) - Insertion was successful.

    def searchNode(self, e):
        current = self.root
        while current:
            if e < current.element:
                current = current.left  # O(log n) - Move left.
            elif e > current.element:
                current = current.right  # O(log n) - Move right.
            else:
                return current  # O(1) - Node found, return it.
        return None  # O(1) - Node not found.

    def createSubtreeBST(self, e):
        node = self.searchNode(e)  # O(log n) - Find the node.
        if node is None:
            print("Element not found in the tree.")  # O(1) - Element not found.
            return None
        new_bst = BST()  # O(1) - Create a new BST instance.
        queue = [node]  # O(1) - Start with the found node.
        while queue:
            current = queue.pop(0)  # O(n) - Remove from the front, less efficient than deque.
            new_bst.insert(current.element)  # O(log n) - Insert element into the new BST.
            if current.left:
                queue.append(current.left)  # O(1) - Add left child to the queue.
            if current.right:
                queue.append(current.right)  # O(1) - Add right child to the queue.
        return new_bst  # O(1) - Return the newly created subtree.

    def DisplayBST(self):
        if self.root:
            lines, _, _, _ = self.display_rec(self.root)  # O(n) - Generate lines to display the tree.
            print("\n")
            print("\t== Binary Tree: shape ==")
            print("\n")
            for line in lines:
                print('\t', line)  # O(n) - Print each line.
        else:
            print("\t== The tree is empty ==")  # O(1) - Print if tree is empty.

    def display_rec(self, node):
        if node is None:
            return [], 0, 0, 0  # O(1) - Handle the base case where the node is None.

        line = str(node.element)
        width = len(line)

        # Base case: the node is a leaf
        if node.left is None and node.right is None:
            return [line], width, 1, width // 2  # O(1) - Directly return the line for a leaf node.

        # Recursively call on the left child if the right child is absent
        if node.right is None:
            lines, n, p, x = self.display_rec(node.left)  # O(n/2) - Recursively process the left child.
            s = '%s' % node.element
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2  # Combine and return formatted lines.

        # Recursively call on the right child if the left child is absent
        if node.left is None:
            lines, n, p, x = self.display_rec(node.right)  # O(n/2) - Recursively process the right child.
            s = '%s' % node.element
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2  # Combine and return formatted lines.

        # Node has both children
        left, n, p, x = self.display_rec(node.left)  # O(n/2) - Recursively process the left child.
        right, m, q, y = self.display_rec(node.right)  # O(n/2) - Recursively process the right child.
        s = '%s' % node.element
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)  # Pad the shorter side if necessary.
        elif q < p:
            right += [m * ' '] * (p - q)  # Pad the shorter side if necessary.
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2  # Combine and format all parts into the final structure.


class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None

def Preload():
    Data = []  # O(1) - Initialize an empty list to store data.
    RequestLoopCount = input("Please enter the number of elements you would like generated in the array: ")  # O(1) - Prompt user for the number of elements.
    while int(RequestLoopCount) > 0:  # O(n) - Iterate n times based on user input, where n is the number of elements.
        NewItemToAddToArray = random.randint(0, 100)  # O(1) - Generate a random integer between 0 and 100.
        Data.append(NewItemToAddToArray)  # O(1) - Append the new item to the list (more efficient than insert at index).
        RequestLoopCount = int(RequestLoopCount) - 1  # O(1) - Decrement the loop counter.
    print("Your data is: ", Data)  # O(1) - Output the generated data list.
    return Data  # O(1) - Return the populated data list.

def ManuallyLoad():
    Data = []  # O(1) - Initialize an empty list to store data.
    RequestLoopCount = input("Please enter the number of elements you would like to enter manually: ")  # O(1) - Prompt user for the number of elements.
    while int(RequestLoopCount) > 0:  # O(n) - Iterate n times based on user input.
        NewItemToAddToArray = input("Please enter a number to add to the data: ")  # O(1) - Prompt user for a number.
        Data.append(int(NewItemToAddToArray))  # O(1) - Append the entered number to the list (more efficient than insert at index).
        RequestLoopCount = int(RequestLoopCount) - 1  # O(1) - Decrement the loop counter.
    print("Your data is: ", Data)  # O(1) - Output the manually entered data list.
    return Data  # O(1) - Return the populated data list.

def ExitMenu():
    return False  # O(1) - Simply returns False to indicate exiting or ending an action.

def DataLoader(Data):
    intTree = BST()  # O(1) - Instantiate a new binary search tree.
    for e in Data:  # O(n * log m) - Iterate through each data element where m is the number of elements already in the BST.
        intTree.insert(e)  # O(log m) - Insert an element into the BST assuming a balanced tree.
    return intTree  # O(1) - Return the populated BST.

def CountingSort(Data):
    UnsortedArray = Data  # O(1) - Assigns the input array to UnsortedArray.
    FinalArray = [0] * len(UnsortedArray)  # O(n) - Creates an array of zeros with the same length as UnsortedArray.
    max_element = max(UnsortedArray)  # O(n) - Finds the maximum element in UnsortedArray.
    min_element = min(UnsortedArray)  # O(n) - Finds the minimum element in UnsortedArray.
    range_of_numbers = max_element - min_element + 1  # O(1) - Calculates the range of numbers in UnsortedArray.
    count = [0] * range_of_numbers  # O(k) - Creates a count array initialized with zeros, where k is the range.
    for num in UnsortedArray:  # O(n) - Iterates through each number in the UnsortedArray.
        count[num - min_element] += 1  # O(1) - Increments the count for the number.
    for i in range(1, len(count)):  # O(k) - Iterates through the count array to accumulate counts.
        count[i] += count[i - 1]  # O(1) - Accumulates count values.
    for num in reversed(UnsortedArray):  # O(n) - Iterates through the array in reverse to place elements.
        FinalArray[count[num - min_element] - 1] = num  # O(1) - Places elements into the final array based on count.
        count[num - min_element] -= 1  # O(1) - Decreases the count by one.
    return FinalArray  # O(1) - Returns the sorted array.

def CreateTopDownBSTInput(sorted_input, L, R):
    if L > R:  # O(1) - Checks if there are no elements to process.
        return None  # O(1) - Returns None for no subtree.
    mid = (L + R) // 2  # O(1) - Finds the middle index of the sorted array.
    root = TreeNode(sorted_input[mid])  # O(1) - Creates a new TreeNode with the middle element.
    root.left = CreateTopDownBSTInput(sorted_input, L, mid - 1)  # Recursion to create left subtree.
    root.right = CreateTopDownBSTInput(sorted_input, mid + 1, R)  # Recursion to create right subtree.
    return root  # O(1) - Returns the root of the BST.

def GetBSTData(root):
    data = []  # O(1) - Initialize an empty list to store data from BST.
    if root:  # O(1) - Checks if root is not None.
        data.append(root.element)  # O(1) - Adds root's element to data list.
        data.extend(GetBSTData(root.left))  # Recursively gets data from left subtree.
        data.extend(GetBSTData(root.right))  # Recursively gets data from right subtree.
    return data  # O(1) - Returns the list of data collected from the BST.


def SecondMenu(SecondMenuActive, Data):
    sorted_input = CountingSort(Data)  # O(n + k) - Sort the data using Counting Sort.
    Root = CreateTopDownBSTInput(sorted_input, 0, len(sorted_input) - 1)  # O(n) - Create a BST from the sorted data.
    intTree = DataLoader(GetBSTData(Root))  # O(n log n) - Load the sorted data into an AVL tree.

    while SecondMenuActive:  # O(1) - Continue displaying the menu as long as it is active.
        os.system('clear')  # O(1) - Clear the console for a clean display of the menu.

        # Print the main menu options
        print("Please Pick One Of The Following Options: ")
        print("    - Option 1 : Display the tree shape of current BST, and then display the pre-order, in-order, post-order and inverse-in-order traversal sequences of the BST.")
        print("    - Option 2 : Display all leaf nodes of the BST, and all non-leaf nodes (separately).")
        print("    - Option 3 : Display a subtree of the BST and count the number of nodes of the subtree.")
        print("    - Option 4 : Display the depth of a given node in the BST.")
        print("    - Option 5 : Display the depth of a subtree of the BST.")
        print("    - Option 6 : Insert a new integer key into the BST.")
        print("    - Option 7 : Delete an integer key from the BST.")
        print("    - Option 8 : Return to the level-1 menu.")
        print("------------------------------------------")
        
        SecondMenuInput = input("Please enter a menu option number: ")  # O(1) - Get user input for selecting a menu option.

        if SecondMenuInput == "1":
            intTree.DisplayBST()  # O(n) - Display the current BST structure visually.
            print("\nPre order:")
            intTree.preorder()  # O(n) - Display pre-order traversal.
            print("\n")
            print("\nIn order:")
            intTree.inorder()  # O(n) - Display in-order traversal.
            print("\n")
            print("\nPost order:")
            intTree.postorder()  # O(n) - Display post-order traversal.
            print("\n")
            print("\nInverse in order:")
            intTree.inverse_inorder()  # O(n) - Display inverse in-order traversal.
            print("\n")
            input("Press Any Key To Return To The Main Menu")  # O(1) - Wait for user input to continue.

        elif SecondMenuInput == "2":
            print("\nLeaf nodes in order:")
            intTree.leaf_inorder()  # O(n) - Display all leaf nodes in the BST.
            print("\n")
            print("\nNon leaf nodes in order:")
            intTree.non_leaf_inorder()  # O(n) - Display all non-leaf nodes in the BST.
            print("\n")
            input("Press Any Key To Return To The Main Menu")  # O(1) - Wait for user input to continue.

        elif SecondMenuInput == "3":
            UserInput = input("Please enter the root of the subtree: ")  # O(1) - Get the root element for the subtree.
            try:
                subTree = intTree.createSubtreeBST(int(UserInput))  # O(n) - Create and display a subtree based on user input.
                subTree.DisplayBST()  # O(n) - Display the subtree
                print("\nSub tree nodes count:", subTree.total_nodes_preorderHelper(subTree.root))  # O(n) - Count and display the number of nodes in the subtree.
                print("\n")
            except Exception as e:
                print("ERROR: Node not found!")  # O(1) - Handle case where the node is not found.
            input("Press Any Key To Return To The Main Menu")  # O(1) - Wait for user input to continue.

        elif SecondMenuInput == "4":
            UserInput = input("Please enter the node for which depth is required: ")  # O(1) - Get the specific node for depth calculation.
            print("Node depth:")  # O(1)
            intTree.findNodeDepth(int(UserInput)) # O(log n) - Calculate and display the depth of the specified node.
            input("Press Any Key To Return To The Main Menu")  # O(1) - Wait for user input to continue.

        elif SecondMenuInput == "5":
            UserInput = input("Please enter the root of the subtree for depth calculation: ")  # O(1) - Get the root of the subtree for depth calculation.
            print("Subtree depth:")  # O(1)
            intTree.depthSubtreeBST(int(UserInput)) # O(n) - Calculate and display the depth of the subtree.
            input("Press Any Key To Return To The Main Menu")  # O(1) - Wait for user input to continue.

        elif SecondMenuInput == "6":
            UserInput = input("Please enter a new integer key to insert into the BST: ")  # O(1) - Get a new integer key for insertion.
            intTree.insert(int(UserInput))  # O(log n) - Insert a new key into the BST.
            intTree.DisplayBST()  # O(n) - Display the BST after insertion.
            input("Press Any Key To Return To The Main Menu")  # O(1) - Wait for user input to continue.

        elif SecondMenuInput == "7":
            UserInput = input("Please enter an integer key to delete from the BST: ")  # O(1) - Get an integer key for deletion.
            try:
                intTree.deleteRec(intTree.root, int(UserInput))  # O(log n) - Delete node and update root
                print("Node deleted successfully.")  # O(1) - Confirm deletion to the user.
            except:
                print("ERROR: Node not found!")  # O(1) - Node not found message.
            intTree.DisplayBST()  # O(n) - Display the BST after deletion.
            print("\n")
            input("Press Any Key To Return To The Main Menu")  # O(1) - Wait for user input to continue.

        elif SecondMenuInput == "8":
            SecondMenuActive = ExitMenu()  # O(1) - Call the function to exit the menu and return to the main level-1 menu.
        
        else:
            print("\nError Not An Option") # O(1) - Return to the current menu.


def FirstMenu(Active):
    while Active:  # O(1) - Loop continues as long as Active is True.
        os.system('clear')  # O(1) - Clears the console for a clean display of options.
        Data = []  # O(1) - Initializes an empty list to store data.
        
        # Print the main menu options
        print("Please Pick One Of The Following Options: ")  # O(1) - Displays static text.
        print("    - Option 1 : Pre-load a sequence of integers to build a BST.")  # O(1) - Displays option 1.
        print("    - Option 2 : Manually enter integer keys one by one to build a BST.")  # O(1) - Displays option 2.
        print("    - Option 3 : Exit Program.")  # O(1) - Displays option 3.
        print("------------------------------------------")  # O(1) - Displays a separator line.

        FirstMenuInput = input("Please enter a menu option number: ")  # O(1) - Prompts for and reads the menu option number from the user.

        if FirstMenuInput == "1":  # O(1) - Checks if the user chose option 1.
            Data = Preload()  # O(n) - Calls Preload to generate and load data; complexity depends on user input and size of data generated.
            SecondMenu(True, Data)  # O(m) - Calls SecondMenu with the preloaded data; m depends on the operations within SecondMenu.
            FirstMenuInput = None  # O(1) - Resets FirstMenuInput to prepare for the next iteration if needed.

        elif FirstMenuInput == "2":  # O(1) - Checks if the user chose option 2.
            Data = ManuallyLoad()  # O(n) - Calls ManuallyLoad to collect data manually; complexity depends on user input and number of inputs provided.
            SecondMenu(True, Data)  # O(m) - Calls SecondMenu with the manually loaded data; m depends on the operations within SecondMenu.
            FirstMenuInput = None  # O(1) - Resets FirstMenuInput for the next iteration.

        elif FirstMenuInput == "3":  # O(1) - Checks if the user chose option 3 to exit.
            Active = ExitMenu()  # O(1) - Calls ExitMenu to potentially update the Active flag to false and terminate the loop.

        else:
            print("\nError Not An Option") # O(1) - Return to the current menu.

if __name__ == "__main__":
    FirstMenu(True)  # O(1) - Initiates the FirstMenu function with Active set to True, starting the menu interaction.
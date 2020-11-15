import queue as queue
import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
''' BUILD FUNCTIONS '''
def buildTree(arr): # Doesn't sort the array, so not valid BST

    if not arr:
        return None

    mid = (len(arr)) // 2 
    
    root = TreeNode(arr[mid]) 
    
    root.left = buildTree(arr[:mid]) 
    root.right  = buildTree(arr[mid+1:]) 

    return root

def buildBST(arr):
    if not arr:
        return None

    sort = sorted(arr)

    def helper(arr):
        if not arr:
            return None

        mid = (len(arr)) // 2 # If you want a balanced array, use the mid item as root
       
        root = TreeNode(arr[mid]) 
        
        root.left = helper(arr[:mid]) #splits the array for elements to the left
        root.right  = helper(arr[mid+1:]) #splits the array for elements to the right

        return root

    return helper(sort)

def validateBST(root): #In-order traversal of tree. Prev must always be smaller
    if root == None:
        return True

    stack = queue.LifoQueue()
    prev = None

    while(root != None or stack.qsize() > 0):
        while(root != None): #Traverses left
            stack.put(root)
            root = root.left
        
        root = stack.get() #Traverses root
        if(prev != None and prev.val >= root.val):
            return False
        prev = root
        root = root.right #Traverses right 

    return True

''' TRAVERSALS '''
def inOrderIterative(root): # Using a stack
    print('--- In-Order Iteratively ---')
    
    stack = queue.LifoQueue()
    ret = []
    while(root != None or stack.qsize() > 0):
        while(root != None): #Traverse left first
            stack.put(root)
            root = root.left
        
        root = stack.get() # If no more left, pop out of stack and evaluate
        ret.append(root.val)

        root = root.right # Check right. If right is None it wont be put in the stack and will continue to the next node in the stack

    return ret

def inOrderRecursive(root):
    print('--- In-Order Recursively ---')

    ret = []

    def helper(root, ret):
        if root == None:
            return
        helper(root.left, ret) # Traverse left
        ret.append(root.val) # Do something 
        helper(root.right, ret) #Traverse right

    helper(root, ret)
    return ret

def preOrderRecursive(root):
    print('--- Pre-Order Recursively ---')

    ret = []

    def helper(root, ret):
        if root == None:
            return
        
        ret.append(root.val)
        helper(root.left, ret)
        helper(root.right, ret)

    helper(root, ret)
    return ret
def preOrderIterative(root): # Use a stack
    print('--- Pre-Order Iterative ---') 
    if root is None: 
        return 
  
    stack = queue.LifoQueue()
    stack.put(root) 
  
    ret = []
    while(stack.qsize() > 0): 
          
        cur = stack.get() 
        ret.append(cur.val)
          
        if cur.right is not None: # Put right in first because LIFO, you want left to come out first
            stack.put(cur.right) 
        if cur.left is not None: 
            stack.put(cur.left) 

    return ret
def postOrderRecursive(root):
    print('--- Post-Order Recursively ---')

    ret = []

    def helper(root, ret):
        if root == None:
            return
        
        helper(root.left, ret)
        helper(root.right, ret)
        ret.append(root.val)

    helper(root, ret)
    return ret

def levelOrderIterative(root): 
    ret = []

    if root == None:
        return ret
    
    q = queue.Queue() #Creates a FIFO queue
    q.put(root)

    while(q.empty() == False):

        node = q.get()
        ret.append(node.val)

        if node.left != None:
            q.put(node.left)
        if node.right != None:
            q.put(node.right)
    
    return ret
            

def isBalanced(root) -> bool:
    # Bottom up recursion
    # Each node returns its max depth of its right and left subtrees
    def check(root):
        if root is None:
            return 0
        left  = check(root.left)
        right = check(root.right)
        # If left or right is -1, the tree is unbalanced, keep returning -1
        # Check the difference in depth between left and right
        if left == -1 or right == -1 or abs(left - right) > 1: 
            return -1
        return 1 + max(left, right) # The depth of a ndoe is equal to the max depth
                                    # of its children nodes plus one
        
    return check(root) != -1

def main():
    arr = [7,4,9,3,5,1,8,2,6]
    root = buildBST(arr)

    print(levelOrderIterative(root))
    

    

if __name__ == "__main__":
    main()

class Node:
    def __init__(self, val):
        self.val = val
        self.height = 1
        self.left: Node = None
        self.right: Node = None
def getHeight(root: Node) -> int:
    if not root:
        return 0
    return root.height
def getBalance(root: Node) -> int:
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)
def leftRotate(root: Node) -> Node:
    y = root.right
    T2 = y.left
    y.left = root
    root.right = T2
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y
def rightRotate(x: Node) -> Node:
    y = x.left
    T2 = y.right
    y.right = x
    x.left = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y
def insert( root: Node, val: int) -> Node:
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    else:
        return root
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)
    if balance > 1 and val < root.left.val:
        return rightRotate(root)
    if balance < -1 and val > root.right.val:
        return rightRotate(root)
    if balance > 1 and val > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and val < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root
def getMinValueNode( root: Node) -> Node:
    if not root or not root.left:
        return root
    return getMinValueNode(root.left)
def delete( root: Node, val: int) -> Node:
    if not root:
        return root
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if not root.left:
            t = root.right
            root = None
            return t
        elif not root.right:
            t = root.left
            root = None
            return t
        t = getMinValueNode(root.right)
        root.val = t.val
        root.right = delete(root.right, t.val)
    if not root:
        return root
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root
def inorder( root: Node) -> None:
    if not root:
        return
    inorder(root.left)
    print(root.val, end = ' ')
    inorder(root.right)
if __name__ == "__main__":
    root = None
    root = insert(root, 10)
    root = insert(root, 20)
    print("Inorder Traversal :", end = ' ')
    inorder(root)
    print()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def convert_to_min_heap(root):
        if not root:
           return
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            elements.append(node.val)
            inorder_traversal(node.right)
    elements = []
    inorder_traversal(root)
    elements.sort()
    def fill_heap(node, index):
        if node:
            node.val = elements[index[0]]
            index[0] += 1
            fill_heap(node.left, index)
            fill_heap(node.right, index)
    fill_heap(root, [0])

    root = TreeNode(3, TreeNode(1), TreeNode(2))
    convert_to_min_heap(root)
# class TreeNode:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

# root=TreeNode(10)
# left_child=TreeNode(5)
# right_child=TreeNode(15)

# root.left=left_child
# root.right=right_child

# print(f"Root Data{root.data}")
# print(f"Left Child{root.left.data}")
# print(f"Right Child{root.right.data}")

# root.left=left_child
# root.right=right_child
# root.left.left=TreeNode(2)
# root.left.right=TreeNode(8)
# root.left.left=TreeNode(12)
# root.left.right=TreeNode(20)



# print(f"Root Data{root.data}")
# print(f"Left Child{root.left.data}")
# print(f"Right Child{root.right.data}")


# def print_in_order(node):
#     if node is None:
#         return
#     print_in_order(node.left)
#     print(node.data,end=" ")
#     print_in_order(node.right)


# def print_pre_order(node):
#     if node is None:
#         return
#     print(node)

class BSTree:
    def __init__(self.key):
        self.val=Key
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return BSTree(key)
    

    if key<root.val:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)

    return root



def search(root,key):
    if root is None:
        return False
    if root.val==key:
        return True
    

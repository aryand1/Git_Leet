# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: 
            return True
        if p is None or q is None:
            return False
        if p.val!=q.val: 
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)  


# a solution or a tree-related utility. In Python, when you define a method within a class, you need to use self to refer to the instance of the class.



# Instance Method: When you define a method inside a class, it becomes an instance method. To call this method, you need an instance of the class. The self parameter in the method definition refers to the instance that calls the method.
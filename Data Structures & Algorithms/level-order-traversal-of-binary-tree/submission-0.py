# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        li=[]
        if root is None:
            return li
        return self.lvt(root,li,0)
    def lvt(self,root,li,i):
        if root is None:
            return li
        if len(li)-1<i:
            li.append([])
        li[i].append(root.val)
        if root.left:
            li=self.lvt(root.left,li,i+1)
        if root.right:
            li=self.lvt(root.right,li,i+1)
        return li
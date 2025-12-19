# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def findMax(l, r):
            max_index = l
            for i in range(l, r):
                if nums[i] > nums[max_index]:
                    max_index = i
            return max_index

        def build(l, r):
            if l >= r:
                return None

            max_index = findMax(l, r)
            print(max_index)
            root = TreeNode(nums[max_index])

            root.left = build(l, max_index)
            root.right = build(max_index + 1, r)

            return root


        return build(0, len(nums))
        

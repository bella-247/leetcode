# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def findMax(arr):
            max_index = 0
            for i in range(len(arr)):
                if arr[i] > arr[max_index]:
                    max_index = i
            return max_index

        def build(arr):
            if not arr:
                return None

            max_index = findMax(arr)
            root = TreeNode(arr[max_index])

            left = arr[ : max_index]
            right = arr[ max_index + 1 : ]

            root.left = build(left)
            root.right = build(right)

            return root


        return build(nums)
        

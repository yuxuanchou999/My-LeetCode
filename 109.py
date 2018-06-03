# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(nums):
            if not nums: return None
            root = TreeNode(nums[len(nums) // 2])
            root.left = helper(nums[:len(nums) // 2])
            root.right = helper(nums[len(nums) // 2 + 1:])
            return root
        
        nums  = []
        while head:
            nums.append(head.val)
            head = head.next
        
        return helper(nums)

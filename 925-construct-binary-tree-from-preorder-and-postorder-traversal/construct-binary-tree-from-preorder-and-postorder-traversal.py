# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_index = {val: idx for idx, val in enumerate(postorder)}
        pre_index = 0

        def buildTree(left, right):
            nonlocal pre_index
            if pre_index >= len(preorder) or left > right:
                return None

            root = TreeNode(preorder[pre_index])
            pre_index += 1

            if pre_index < len(preorder) and left <= right:
                left_child_idx = postorder_index[preorder[pre_index]]

                if left_child_idx < right:
                    root.left = buildTree(left, left_child_idx)
                    root.right = buildTree(left_child_idx + 1, right - 1)

            return root
        return buildTree(0, len(postorder) - 1)

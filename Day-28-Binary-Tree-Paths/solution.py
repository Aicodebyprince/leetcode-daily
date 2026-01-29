class Solution(object):
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            # If leaf node, add path to result
            if not node.left and not node.right:
                result.append(path)
                return

            # Continue DFS
            dfs(node.left, path + "->")
            dfs(node.right, path + "->")

        dfs(root, "")
        return result

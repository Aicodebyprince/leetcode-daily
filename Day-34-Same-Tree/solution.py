class Solution(object):
    def isSameTree(self, p, q):
        # If both nodes are None, trees match here
        if not p and not q:
            return True

        # If one is None and the other is not, trees differ
        if not p or not q:
            return False

        # If values differ, trees differ
        if p.val != q.val:
            return False

        # Check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


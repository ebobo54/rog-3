class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solution(root) -> bool:
    def check_balance(node):
        if node is None:
            return 0, True
        lh, lb = check_balance(node.left)
        rh, rb = check_balance(node.right)
        balanced = lb and rb and abs(lh - rh) <= 1
        return 1 + max(lh, rh), balanced
    _, is_bal = check_balance(root)
    return is_bal

def test():
    node1 = Node(1)
    node2 = Node(0)
    root1 = Node(-1, node1, node2)
    print(solution(root1))

    node3 = Node(3)
    node4 = Node(6)
    node5 = Node(0, node3, node4)
    root2 = Node(1, Node(2), node5)
    print(solution(root2))

    node7 = Node(7)
    node8 = Node(8)
    node4_2 = Node(4, node7, node8)
    node12 = Node(12, node4_2, None)
    root3 = Node(0, Node(2), node12)
    print(solution(root3))

if __name__ == '__main__':
    test()

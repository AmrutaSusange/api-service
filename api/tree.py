class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"value: {self.value}, left: {self.left}, right: {self.right}"

def insert(node, value):
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node


if __name__ == "__main__":
    l = [10, 5, 15, 2, 7, 12, 20]
    root = None
    for ele in l:
        root = insert(root, ele)










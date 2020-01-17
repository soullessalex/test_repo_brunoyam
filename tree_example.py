class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = TreeNode(100000000000)


def add_value(new_value, current_node):
    if current_node.value > new_value:  # left
        if current_node.left is not None:
            add_value(new_value, current_node.left)  # go to left child
        else:
            current_node.left = TreeNode(new_value)  # add new node
    else:  # right
        if current_node.right is not None:
            add_value(new_value, current_node.right)  # go to right child
        else:
            current_node.right = TreeNode(new_value)  # add new child


def print_tree(current_node):
    print(current_node.value)
    if current_node.left is not None:
        print_tree(current_node.left)
    if current_node.right is not None:
        print_tree(current_node.right)


add_value(10, root)
add_value(5, root)
add_value(3, root)
add_value(7, root)
add_value(6, root)
add_value(9, root)

add_value(11, root)
add_value(14, root)
print_tree(root)


def find(value, current_node):
    if current_node.value == value:
        return True
    if current_node.value > value:
        if current_node.left is not None:
            return find(value, current_node.left)
        else:
            return False
    if current_node.value < value:
        if current_node.left is not None:
            return find(value, current_node.right)
        else:
            return False


print(find(17, root))
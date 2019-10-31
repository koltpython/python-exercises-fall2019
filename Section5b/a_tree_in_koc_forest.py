# Functions
def draw_tree_top(height):
    tree_layer = ''
    for layer_index in range(height):
        for index in range(2 * height - 1):
            if index == height - 1 - layer_index or index == height - 1 + layer_index:
                tree_layer += '*'
            else:
                tree_layer += ' '
        if layer_index != height - 1:
            tree_layer += '\n'

    print(tree_layer)
    # Modifying and printing the tree_layer string, create the top part of the tree


def draw_tree_bottom(height):
    tree_bottom = ""
    # Modifying the tree_bottom string, create the bottom part of the tree
    for index in range(2 * height - 1):
        if index == height or index == height - 2:
            tree_bottom += '|'
        else:
            tree_bottom += ' '
    print(tree_bottom)


# Main
height = 10
draw_tree_top(height)
draw_tree_bottom(height)

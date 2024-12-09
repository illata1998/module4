from node import Node


# BEGIN
def reverse(linked_list):
    reversed_list = None
    current = linked_list

    while current:
        reversed_list = Node(current.get_value(), reversed_list)
        current = current.get_next()

    return reversed_list
# END

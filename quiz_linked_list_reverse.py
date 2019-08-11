#разаернуть готовый связный список(ссылки на следующий объект)
from linked_list import LinkedListNode

def reverse(node):
    if node == None:
        return None
    if node.next == None:
        return node
    prev_node = None
    current = node
    while current:
        temp = current.next
        current.next = prev_node
        prev_node = current
        current = temp
    return(prev_node)


def display_all_values(node):
    while True:
        print(node.value)
        if node.next == None:
            break
        node = node.next



a = LinkedListNode(1)
a.next = LinkedListNode(2)
a.next.next = LinkedListNode(3)
a.next.next.next = LinkedListNode(4)
display_all_values(a)
display_all_values(reverse(a))
# singly linked list is a linear data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the next node.
# The first node is called the head, and the last node is called the tail. The tail node points to None, indicating the end of the list.
# Singly linked lists are used to implement stacks, queues, and other abstract data types.
# The main advantage of singly linked lists is that they are dynamic, meaning that they can grow or shrink as needed.
# The main disadvantage of singly linked lists is that they are not as efficient as arrays for random access to elements.

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value)
            current = current.next

if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(1)
    singly_linked_list.append(3)
    singly_linked_list.append(2)
    singly_linked_list.prepend(0)
    singly_linked_list.prepend(4)
    singly_linked_list.print_list()

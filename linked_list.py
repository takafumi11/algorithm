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

    def remove(self, value: int) -> None:
        current_node = self.head
        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return
        
        previous_node = None
        while current_node and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next

        # if the value is not found
        if current_node is None:
            return
        
        # if the value is found
        if current_node and current_node.value == value:
            previous_node.next = current_node.next
            current_node = None
            return
        self.length -= 1
    
    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value)
            current = current.next


    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        self.tail = self.head
        
        while current_node:
            next_node = current_node.next

            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

    def reverse_recursive(self) -> None:
        previous_node = None
        current_node = self.head
        self.tail = self.head

        def _reverse_recursive(current_node: Node, previous_node: Node) -> Node:
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(current_node, previous_node)


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.prepend(0)
    singly_linked_list.remove(3)
    singly_linked_list.print_list()
    print("####### Reverse Iterative")
    singly_linked_list.reverse_recursive()
    singly_linked_list.print_list()
    print("####### Rverse Recursive")
    singly_linked_list.reverse_iterative()
    singly_linked_list.print_list()
    
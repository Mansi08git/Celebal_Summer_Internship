# Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Adds a node with the given data to the end of the list.
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #  Prints the elements in the linked list.
    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Deletes the nth node (1-based index) from the list.

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise Exception("Index must be a positive integer.")

        # Deleting the head node
        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        # Traverse to the (n-1)th node
        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1

        # Check if the next node exists
        if not current or not current.next:
            raise Exception("Index out of range.")

        print(f"Deleting node at position {n} with value {current.next.data}")
        current.next = current.next.next

# Testing the LinkedList
if __name__ == "__main__":
    ll = LinkedList()

    # Adding nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial List:")
    ll.print_list()
    print()

    # Deleting 2nd node
    try:
        ll.delete_nth_node(2)
        print("List after deleting 2nd node:")
        ll.print_list()
    except Exception as e:
        print(f"Error: {e}")

    # Deleting head node
    try:
        print()
        ll.delete_nth_node(1)
        print("List after deleting 1st node:")
        ll.print_list()
    except Exception as e:
        print(f"Error: {e}")

    # delete with an out-of-range index
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print(f"\nError: {e}")

    # delete from an empty list
    try:
        ll = LinkedList() 
        ll.delete_nth_node(1)
    except Exception as e:
        print(f"\nError: {e}")

class LinkedList:
    # Inner class representing a single node (element) in the linked list
    class Node:
        def __init__(self, element):
            self.element = element  # Stores the actual data/value of the node
            self.next = None        # Pointer/reference to the next node in the list (defaults to None)
            
    # Initializes a new, empty LinkedList
    def __init__(self):
        self.length = 0   # Counter tracking how many nodes are currently in the list[cite: 1]
        self.head = None  # Points to the first node in the list (None when empty)

    # Checks whether the linked list has any nodes[cite: 2]
    def is_empty(self):
        return self.length == 0  # Returns True if length is 0, otherwise False[cite: 2]
    
    # Appends a new element to the end of the linked list
    def add(self, element):
        node = self.Node(element)  # Wraps the raw element inside a new Node object
        if self.is_empty():
            self.head = node       # If the list is empty, the new node becomes the head
        else:
            current_node = self.head
            # Traverse through the list until reaching the last node (whose .next is None)[cite: 4]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node  # Link the last node to the newly created node
        self.length += 1              # Increment the node count by 1

    # Searches for and removes the first node matching the given element
    def remove(self, element):
        previous_node = None
        current_node = self.head
        
        # Traverse the list while nodes remain and the target element hasn't been found[cite: 6]
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
            
        if current_node is None:
            return  # Element was not found in the list; exit without changing anything
        elif previous_node is not None:
            # Target is in the middle or end: bypass current_node by linking previous_node to the next node
            previous_node.next = current_node.next
        else:
            # Target is the head node: move the head pointer to the second node
            self.head = current_node.next
            
        self.length -= 1  # Decrement the node count by 1


# --- Testing the LinkedList ---

my_list = LinkedList()        # Create a new, empty LinkedList instance[cite: 3]
print(my_list.is_empty())     # Prints True because no nodes have been added yet[cite: 2, 3]

my_list.add(1)                # Adds node with value 1 as the head
my_list.add(2)                # Traverses past 1 and links node with value 2 at the end
print(my_list.is_empty())     # Prints False because the list now contains 2 nodes[cite: 2, 5]
print(my_list.length)         # Prints 2 (the current number of nodes in the list)[cite: 5]

class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


# class LL:
#     def __init__(self):
#         self.head = None

#     def append(self, val):
#         new_node = Node(val)
#         if not self.head:  # If the list is empty
#             self.head = new_node
#             return self.display()
#         current = self.head
#         while current.next:  # Traverse to the last node
#             current = current.next
#         current.next = new_node  # Add the new node at the end
#         return self.display()

#     def display(self):
#         elem = []
#         current = self.head
#         while current:  # Traverse the list and collect values
#             elem.append(current.val)
#             current = current.next
#         return elem


# if __name__ == "__main__":
#     # Create an instance of the LL class
#     ll = LL()
    
#     # Append elements to the linked list
#     print(ll.append("10"))  # Output: ['10']
#     print(ll.append("20"))  # Output: ['10', '20']
#     print("success")

class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next


# class LL(Node):
class LL:
    def __init__(self):
        self.head = None
    
    def append (self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return self.display() #thiws one is for first elem
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node
        return self.display()
    

    def add_begin(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return self.display()
    
    def add_after_val(self,val,to_add):
        new__node = Node(to_add)
        current = self.head 
        while current.val != val:
            current = current.next
        new__node.next = current.next
        current.next = new__node
        return self.display()
        

    def del_begin(self):

        self.head = self.head.next
        return self.head.val

    def del_after_val(self,val):
        current = self.head
        while current.val !=val:
            current = current.next
        current = current.next
        return self.display()

    def display(self):
        elem = []
        current = self.head
        while current:
            elem.append(current.val)
            current = current.next 
        return elem
    
    
if __name__ == "__main__":
    ll = LL()
    print(ll.append(10))
    print(ll.append(20))
    ll.append(30)
    ll.append(40)
    print(ll.del_begin())
    print(ll.append(333))
    ll.append(666)
    ll.append(999)
    print(ll.add_after_val(333,444))
    print(ll.del_after_val(333))







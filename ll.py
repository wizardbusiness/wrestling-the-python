class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

  def __repr__(self):
    return "ListNode()"
  
  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)
  

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __repr__(self):
    return "LinkedList()"

  def __str__(self):
    return str(self.__class__) + ":" + str(self.__dict__)

  def add(self, val): 
    if not self.head:
      self.head = ListNode(val)
      self.tail = self.head
    else:
      self.tail.next = ListNode(val)
      self.tail = self.tail.next
  # inserts a node after the target position in the linked list
  def insert(self, val, target_posit):
    curr_posit = 0
    curr_node = self.head
    #find 
    while curr_posit < target_posit and curr_node:
      curr_posit += 1
      curr_node = curr_node.next
    
    # insert
    new_node = ListNode(val)
    new_node.next = curr_node.next
    curr_node.next = new_node

  def delete(self, val):
    curr_node = self.head
    if curr_node.val == val:
      curr_node = curr_node.next
      self.head = curr_node
      print(f"Node with val {val} deleted from list")
      return val
      
    while curr_node.next:
      if curr_node.next.val == val and not curr_node.next.next:  
        curr_node.next = None
        print(f"Node with val {val} deleted from list")
        return val
      elif curr_node.next.val == val and curr_node.next.next:
        curr_node.next = curr_node.next.next
        print(f"Node with val {val} deleted from list")
        return val
      curr_node = curr_node.next
    print(f"No node with val {val} found, returning -1")
    return -1
    
  




  def print(self):
    curr_node = self.head
    str_repr = ""
    while (curr_node):
      if (not curr_node.next): 
        str_repr += str(curr_node.val)
      else:
        str_repr += str(curr_node.val) + " -> "     
      curr_node = curr_node.next
    print(str_repr)
    return str_repr

ll = LinkedList()
ll.add(1)
ll.add(32)
ll.add(3)
ll.insert(4, 0)
ll.print()
ll.delete(33)
ll.print()
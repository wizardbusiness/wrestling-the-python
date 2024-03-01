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

  def print(self):
    curr_node = self.head
    str_repr = ""
    while (curr_node):
      if (not curr_node.next): 
        str_repr += str(curr_node.val)
      else:
        str_repr += str(curr_node.val) + " -> "     
      curr_node = curr_node.next
    print (str_repr)

ll = LinkedList()
ll.add(1)
ll.add(32)
ll.print()
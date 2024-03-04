class bstNode:
  def __init__(self, value):
    self.value = value
    self.count = 0
    self.left = None
    self.right = None


class Bst: 
  def __init__(self):
    self.root = None
  

  def add(self, value):
    if not self.root:
      self.root = bstNode(value)

    curr_node = self.root
    while curr_node:
      if value < curr_node.value:
        if curr_node.left:
          curr_node = curr_node.left
        else:
          curr_node.left = bstNode(value)
          curr_node.left.count +=1
          return
      elif value > curr_node.value:
        if curr_node.right:
          curr_node = curr_node.right
        else: 
          curr_node.right = bstNode(value)
          curr_node.right.count += 1
          return
      elif value == curr_node.value:
        curr_node.count += 1
        return


bst = Bst()

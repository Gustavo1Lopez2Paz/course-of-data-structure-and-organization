from Node import Node_sandbox
class Queue:
  def __init__(self, max_size = None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
  def get_size(self):
    return self.size
  def has_space(self):
    if self.max_size is None:
      self.size = True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0
  
  def peek(self):
    if self.is_empty():
            print("¡No hay nada que ver aquí!")
            return None
    return self.head.get_value()
  
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node_sandbox.Node(value)
      print("¡Agregando " + str(item_to_add.get_value()) + " a la cola!")
      if self.is_empty(): 
        self.head = item_to_add 
        self.tail = item_to_add 
      else:
        self.tail.set_next_node(item_to_add) 
        self.tail = item_to_add     
      self.size += 1 
    else:
      print("¡Lo sentimos, no hay más espacio!")
  
  def dequeue(self):
    if self.is_empty():
            print("La cola está vacía. No se puede eliminar ningún valor.")
            return None
        
    removed_value = self.head.get_value()
    self.head = self.head.next_node
    if self.head is None:
      self.tail = None
      self.size -= 1 
      return removed_value
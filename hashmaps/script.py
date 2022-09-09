from linked_list import Node, LinkedList

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    key_encode = key.encode() # convert string to numbers
    hashed_key = sum(key_encode)  # convert several numbers into the sum of all of them, it'll be the hash_code
    return hashed_key 

  def compressor(self, hash_code):
    return hash_code % self.array_size # gives us an index wich will always be in the size of the array
  
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] == value
        return
    
    list_at_array.insert(payload)
    
    
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None



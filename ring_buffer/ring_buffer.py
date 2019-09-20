class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current >= self.capacity:
      self.current = 0
    self.storage[self.current] = item
    self.current += 1

  def get(self):
    result = []
    for i in range(len(self.storage)):
      if self.storage[i] != None:
        result.append(self.storage[i])
    return result
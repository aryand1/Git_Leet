class MyQueue:

    def __init__(self):
      self.stack=[]      
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
      if len(self.stack)!=0:
        del_e=self.stack.pop(0)
        return (del_e)
      else: print("Queue is empty")

    def peek(self) -> int:
     return self.stack[0]

    def empty(self) -> bool:
      if len(self.stack)!=0:
        return False
      else: return True

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
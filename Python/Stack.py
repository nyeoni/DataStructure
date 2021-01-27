class Stack:
    def __init__(self):
        self.stack_list = list()

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        # self.stack_list.pop()
        data = self.stack_list[-1]
        del self.stack_list[-1]
        return data

if __name__=="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("stack output:", stack.pop())
    print("stack output:", stack.pop())
    print("stack output:", stack.pop())

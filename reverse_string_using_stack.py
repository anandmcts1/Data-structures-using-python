class Stack:
	def __init__(self):
		self.items=[]
	def push(self,data):
		return self.items.append(data)
	def pop(self):
		return self.items.pop()
	def is_empty(self):
		return self.items==[]
	def peek(self):
		if not self.is_empty():
			return self.items[-1]
	def get_stack(self):
		return self.items
	def reverse_s(self,stack,string):
		rev_str=''
		for i in range(len(string)):
			stack.push(string[i])
		while not stack.is_empty():
			rev_str+=stack.pop()
		return rev_str
stack=Stack()
s="hello"
print(stack.reverse_s(stack,s))


class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class CircularLinkedList:
	def __init__(self):
		self.head=None

	def prepend(self,data):
		new_node=Node(data)
		if not self.head:
			self.head=new_node
		else:
			p=self.head
			while p.next!=self.head:
				p=p.next
			p.next=new_node
			new_node.next=self.head
			self.head=new_node

	def append(self,data):
		if not self.head:
			new_node=Node(data)
			self.head=new_node
			self.head.next=self.head
		else:
			new_node=Node(data)
			p=self.head
			while p.next!=self.head:
				p=p.next
			p.next=new_node
			new_node.next=self.head

	def print_list(self):
		p=self.head
		while p:
			print(p.data,end=' ')
			p=p.next
			if p==self.head:
				break

c=CircularLinkedList()
c.append("A")
c.append("B")
c.append("C")
c.append("D")
c.print_list()
c.prepend("Z")
print('------------------------------')
c.print_list()


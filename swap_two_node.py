class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class ll:
	def __init__(self):
		self.head=None

	def get_list(self):
		p=self.head
		while p:
			print(p.data)
			p=p.next

	def insertion(self,data,pos):
		new_node=Node(data)
		p=self.head
		if pos==1:
			self.head=new_node
		else:
			while pos-1>0 and p.next!=None:
				pos-=1
				p=p.next

			new_node.next=p.next
			p.next=new_node
	def swap_ll(self,key_1,key_2):
		if key_1==key_2:
			return
		p1=None
		c1=self.head
		while c1 and c1.data!=key_1:
			p1=c1
			c1=c1.next
		p2=None
		c2=self.head
		while c2 and c2.data!=key_2:
			p2=c2
			c2=c2.next
		if not c1 and not c2:
			return 
		if p1:
			p1.next=c2
		else:
			self.head=c2
		if p2:
			p2.next=c1
		else:
			self.head=c1
		c1.next,c2.next=c2.next,c1.next


li=ll()
li.insertion("A",1)
li.insertion("B",2)
li.insertion("C",3)
li.insertion("D",4)
li.get_list()
print('ooooooooooooooooooooooooooooo')
li.swap_ll("C","B")
li.get_list()

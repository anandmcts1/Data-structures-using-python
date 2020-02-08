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
  def reverse_list(self):
		prev=None
		cur=self.head
		while cur:
			nxt=cur.next
			cur.next=prev
			prev=cur
			cur=nxt
		self.head=prev
li=ll()
li.insertion("A",1)
li.insertion("B",2)
li.insertion("C",3)
li.insertion("D",4)
li.get_list()
print('ooooooooooooooooooooooooooooo')
li.swap_ll("C","B")
# li.get_list()
li.reverse_list()
li.get_list()

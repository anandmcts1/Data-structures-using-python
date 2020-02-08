from collections import Counter
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
			print(p.data,end=' ')
			p=p.next
		print()
	

	def insertion_head(self,data,pos):
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
	
	def sum_ll(self,li1,li2):
		p=li1.head
		q=li2.head
		l=[]
		while p and q:
			l.append(p.data+q.data)
			p=p.next
			q=q.next
		c=1
		li3=ll()
		for i in l:
			li3.insertion_head(i,c)
			c+=1
		li3.get_list()
		
		



	

	
li1=ll()
li2=ll()
li1.insertion_head(1,1)
li1.insertion_head(2,2)
li1.insertion_head(3,3)
li1.insertion_head(5,4)
li1.get_list()
li2.insertion_head(6,1)
li2.insertion_head(7,2)
li2.insertion_head(8,3)
li2.insertion_head(9,4)
li2.get_list()
li1.sum_ll(li1,li2)
















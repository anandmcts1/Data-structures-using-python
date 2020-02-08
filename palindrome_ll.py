from collections import Counter
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class ll:
	def __init__(self):
		self.head1=None
		self.head2=None
		# self.head3=None

	def get_list1(self):
		p=self.head1
		while p:
			print(p.data,end=' ')
			p=p.next
		print()
	

	def insertion_head1(self,data,pos):
		new_node=Node(data)
		p=self.head1
		if pos==1:
			self.head1=new_node
		else:
			while pos-1>0 and p.next!=None:
				pos-=1
				p=p.next

			new_node.next=p.next
			p.next=new_node
	def remove_duplicates(self,ll):
		p=ll.head1
		l=[]
		while p:
			l.append(p.data)
			p=p.next
		return l
	def two_last(self):
		p=self.head1
		while p.next.next:
			p=p.next
		print(p.data)
	def ocurence(self):
		p=self.head1
		l=[]
		while p:
			l.append(p.data)
			p=p.next	
		for k,v in Counter(l).items():
			print('k=',k,'v=',v)
	def rotate(self):
		p=self.head1
		l=[]
		while p:
			l.append(p.data)
			p=p.next
		l=l[4%len(l):len(l)]+l[0:4%len(l)]
		c=1
		li2=ll()
		for i in l:
			li2.insertion_head1(i,c)
			c+=1
		li2.get_list1()
	def li_palindrome(self):
		p=self.head1
		s=''
		while p:
			s+=p.data
			p=p.next
		return s==s[::-1]

	

	
li1=ll()
li1.insertion_head1('M',1)
li1.insertion_head1('A',2)
li1.insertion_head1('D',3)
li1.insertion_head1('A',4)
li1.insertion_head1('M',5)
# li1.rotate()
li1.get_list1()
print(li1.li_palindrome())







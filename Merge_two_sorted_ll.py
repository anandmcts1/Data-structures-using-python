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
	def get_list2(self):
		p=self.head2
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
	def insertion_head2(self,data,pos):
		new_node=Node(data)
		p=self.head2
		if pos==1:
			self.head2=new_node
		else:
			while pos-1>0 and p.next!=None:
				pos-=1
				p=p.next

			new_node.next=p.next
			p.next=new_node

	
	def merge_two_sorted_list(self,ll):
		head1=self.head1
		head2=ll.head2
		if not head1:
			return head2
		if not head2:
			return head1
		if head1 and head2:
			if head1.data<=head2.data:
				s=head1
				head1=head1.next
			else:
				s=head2
				head2=head2.next
			new_head=s
		while head1 and head2:
			if head1.data<=head2.data:
				s.next=head1
				s=head1
				head1=s.next
			else:
				s.next=head2
				s=head2
				head2=s.next
		if not head1:
			s.next=head2
		if not head2:
			s.next=head1
		# print(new_node.get_list1())
		return new_head

li1=ll()
li2=ll()
li1.insertion_head1(1,1)
li1.insertion_head1(5,2)
li1.insertion_head1(7,3)
li1.insertion_head1(9,4)
li1.insertion_head1(10,4)

li2.insertion_head2(2,1)
li2.insertion_head2(3,2)
li2.insertion_head2(4,3)
li2.insertion_head2(6,4)
li2.insertion_head2(8,4)

li1.get_list1()
li2.get_list2()


li1.merge_two_sorted_list(li2)
li1.get_list1()




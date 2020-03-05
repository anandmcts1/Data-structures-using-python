class Node:

	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BinaryTree(object):

	def __init__(self,root):
		self.root=Node(root)
	#function 1
	def preOrder(self,root):
		if root.value!=None:
			print(root.value,end=" ") 
		if root.left!=None:
			self.preOrder(root.left)
		if root.right!=None:
			self.preOrder(root.right)
	#function 2
	def inOrder(self,root):
		if root.left!=None:
			self.inOrder(root.left)
		if root.value!=None:
			print(root.value,end=' ')
		if root.right!=None:
			self.inOrder(root.right)
	#function 3
	def postOrder(self,root):
		if root.left!=None:
			self.postOrder(root.left)
		if root.right!=None:
			self.postOrder(root.right)
		if root.value!=None:
			print(root.value,end=' ')
	#FIND MAXIMUM ELEMENT IN A TREE
	#function 4
	def max_element(self,root):
		max=0
		temp=0
		left=0
		right=0
		if root!=None:
			temp=root.value
			left=self.max_element(root.left)
			right=self.max_element(root.right)
			if left>right:
				max=left
			else:
				max=right
			if temp>max:
				max=temp
		return max
	#function 5
	def search(self,root,data):
		temp=0
		if root==None:
			return False
		else:
			if data==root.value:
				return True
			else:
				temp=self.search(root.left,data)
				if temp!=0:
					return temp
				else:
					return self.search(root.right,data)
		return False
	#function 6
	def insert(self,root,data):
		q=[]
		newNode=Node(data)
		newNode.left=None
		newNode.right=None
		if not newNode:
			print('Memory Error')
			return 
		if not root:
			root=newNode
			return
		q.append(root)
		while q:
			temp=q.pop(0)
			if temp.left:
				q.append(temp.left)
			else:
				temp.left=newNode
				q.pop(0)
				return 
			if temp.right:
				q.append(temp.right)
			else:
				temp.right=newNode
				q.pop(0)
				return 
		q.pop(0)
	#function 7
	def size_BT(self,root):
		q=[]
		count=0
		if not root:
			return 0
		q.append(root)
		while q:
			temp=q.pop(0)
			count+=1
			if temp.left:
				q.append(temp.left)
			if temp.right:
				q.append(temp.right)
		del q
		return count
	#fucntion 8(level order traversal in bINary tree)
	def level_traverse(self,root):
		if not root:
			return 

		q=[]
		stack=[]
		q.append(root)
		while q:
			temp=q.pop(0)
			if temp.right:
				q.append(temp.right)
			if temp.left:
				q.append(temp.left)
			stack.append(temp)
		print('Level order traversal in reverse order=',end='')
		while stack:
			print(stack.pop().value,end=' ')
	# def delete_element(self,root):
	# 	if root==None:
	# 		return 
	# 	self.delete_element(root.left)
	# 	self.delete_element(root.right)
	# 	del root

		




tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
tree.root.right.right.right=Node(8)
##########################################size of a binary tree
print('Size of a tree =',tree.size_BT(tree.root))
##########################################preOrder traversing
print("PreOrder traversal=",end=' ')
tree.preOrder(tree.root)
print()
###########################################inorder traversing
print("InOrder traversal=",end=' ')
tree.inOrder(tree.root)
print()
print("PostOrder traversal=",end=' ')
############################################postorder traversing
tree.postOrder(tree.root)
print()
#######################################finding max_element in a tree
print('Maximum element of a binary tree =',tree.max_element(tree.root))
#######################################Searching an element in a binary tree
if tree.search(tree.root,9):
	print('Found')
else:
	print('Not found')
#######################################inserting data into a binary tree
tree.insert(tree.root,9)
print('Size of a tree after insertion =',tree.size_BT(tree.root))
print("PreOrder traversal after insertion of new element =",end=' ')
tree.preOrder(tree.root)
print()
tree.insert(tree.root,10)
########################################level order traverser in reverse order
tree.level_traverse(tree.root)
#########################################delete an element in binary tree
# tree.delete_element(tree.root)

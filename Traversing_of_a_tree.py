class Node:
	
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BinaryTree(object):

	def __init__(self,root):
		self.root=Node(root)

	def preOrder(self,root):
		if root.value!=None:
			print(root.value,end=" ") 
		if root.left!=None:
			self.preOrder(root.left)
		if root.right!=None:
			self.preOrder(root.right)

	def inOrder(self,root):
		if root.left!=None:
			self.inOrder(root.left)
		if root.value!=None:
			print(root.value,end=' ')
		if root.right!=None:
			self.inOrder(root.right)

	def postOrder(self,root):
		if root.left!=None:
			self.postOrder(root.left)
		if root.right!=None:
			self.postOrder(root.right)
		if root.value!=None:
			print(root.value,end=' ')

		




tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
tree.root.right.right.right=Node(8)
print("PreOrder traversal=",end=' ')
tree.preOrder(tree.root)
print()
print("InOrder traversal=",end=' ')
tree.inOrder(tree.root)
print()
print("PostOrder traversal=",end=' ')
tree.postOrder(tree.root)
print()

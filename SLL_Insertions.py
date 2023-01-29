class Node:
	def __init__(self, dataval=None):
		self.dataval=dataval
		self.nextval=None
class SLinkedList:
	def __init__(self):
		self.headval = None
	#insertAtBeginning
	def insertAtBeginning(self,newdata):
		NewNode=Node(newdata)
		NewNode.nextval = self.headval
		self.headval=NewNode

	def insertAtEnd(self,newdata):
		NewNode=Node(newdata)
		if self.headval is None:
			self.headval=NewNode
			return
		last=self.headval
		while(last.nextval):
			last=last.nextval
		last.nextval=NewNode

	def insertInMiddleAfterNode(self,middle_node,newdata):
		if middle_node is None:
			return
		NewNode=Node(newdata)
		NewNode.nextval=middle_node.nextval
		middle_node.nextval=NewNode

	def listPrint(self):
		printval=self.headval
		while printval is not None:
			print(printval.dataval)
			printval=printval.nextval

list1=SLinkedList()
e0=Node('Sun')
list1.headval=e0
e1=Node("Mon")
e0.nextval=e1
e2=Node("Tue")
e1.nextval=e2
e3=Node("Wed")
print("SLL before insertAtBeginning:")
list1.listPrint()
list1.insertAtBeginning(e3.dataval)
e4=Node("Thu")
list1.insertAtEnd(e4.dataval)
e5=Node("Fri")
print("SLL after insertInMiddleAfterNode:")
list1.insertInMiddleAfterNode(e2,e5.dataval)
list1.listPrint()
e6=Node("Sat")
list1.insertAtEnd(e6.dataval)
print("SLL after insertAtEnd:")
list1.listPrint()

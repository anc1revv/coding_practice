class LinkedList():
	class Node:
		def __init__(self, value, next):
			self.value = value
			self.next = next

		def __repr__(self):
			return self.value

	def __init__(self):
		self.first = None

	def isEmpty(self):
		if self.first:
			return False
		else:
			return True

	def appendToList(self, value):
		oldFirst = self.first
		self.first = LinkedList.Node(value, oldFirst)
		print self.first

	def __repr__(self):
		nodes = []
		first = self.first
		print type(first)
		print "first: {0}".format(first)
		while first:
			nodes.append(str(first.value))
			first = first.next

		return 



def main():
	list1 = LinkedList()
	print "Is List Empty? {0}".format(list1.isEmpty())
	list1.appendToList("firstObjectfromAP")
	list1.appendToList("2ndfromAP")
	print list1

if __name__ == '__main__':
	main()
class stack:
	def __init__(self):
		self.the_stack = []

	def push(self, value):
		self.the_stack.append(value)

	def pop(self):
		self.the_stack = self.the_stack[:-1]

	def __str__(self):
		str_list = []
		for item in self.the_stack:
			str_list.append(str(item))

		return ','.join(str_list)


def main():
	print "hh"
	my_new_stack = stack()
	my_new_stack.push(1)
	my_new_stack.push(5)
	my_new_stack.push(3)
	my_new_stack.push(4)
	my_new_stack.push(5)
	my_new_stack.push(6)
	my_new_stack.push(7)
	my_new_stack.push(8)
	my_new_stack.pop()
	print my_new_stack

	my_other_stack = stack()
	my_other_stack.push(4)
	my_other_stack.push(1)
	print my_other_stack

if __name__ == '__main__':
	main()
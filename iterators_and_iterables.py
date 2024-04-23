#iterators vs iterables

nums = [1,2,3]

for i in nums:
	print(i)

#another method for replacement of For loop

#i_nums = nums.__iter__
i_nums = iter(nums)

print(i_nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
#print(next(i_nums)) #stop iteration error comes up here

#OR

j_nums = iter(nums)
while True:
	try:
		item = next(j_nums)
		print(item)
	except StopIteration:
		break

#Built-in range function that behaves like Range class

#The class we create is an iterable but it is also an iterator because it has a dunder next method
class MyRange:
	def __init__(self, start, end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current = self.value
		self.value += 1
		return current

nums = MyRange(1,10)

for num in nums:
	print(num)

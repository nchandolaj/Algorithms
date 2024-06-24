# Algorithm: Insertion Sort implemented as a class with sort method 
# Time Complexity: 
# Space Complexity:
# Original Author and When:
# Description: 
# Ref:

import random

class InsertionSort():

	def __init__(self):
		pass

	def sort(self, list):

		# to-do: pre-condition
		if len(list) == 0:
			return

		# outer loop: loop through list starting with index 1 upwards until the last item
		for i in range(1, len(list)):

			max_index = i

			# inner loop: loop the list starting with index i-1 downwards until the first item 
			# Note: Alternatively, the 'for' loop and the 'if' condition can be replace with a 'while' condition loop
			for j in range(i-1, -1, -1):

				if list[j] > list[max_index]:

					# swap the values so the greater number is on the higher index
					list[j], list[max_index] = list[max_index], list[j]
					max_index = j

		return list

# generate a list of 10 random numbers between 1 and 100 
random_list = random.sample(range(1, 100), 10)
print(f"List of randomly generated numbers = {random_list}")
isort = InsertionSort()
sorted_list = isort.sort(random_list)
print(f"List of sorted numbers = {sorted_list}")

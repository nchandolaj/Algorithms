# Algorithm: Selection Sort implemented as a class with sort method
# Time Complexity: 
# Space Complexity:
# Original Author and When:
# Description: 
# Ref: https://en.wikipedia.org/wiki/Selection_sort

import random

class SelectionSort():
	def __init__(self):
  		pass

	def sort(self, list):
		# to-do: pre-condition
		if len(list) == 0:
			return

		# outer loop - loop through all the elements of the list
		for i in range(len(list)):
			
			# reset index of minimum value to i before entering inner loop
			min_index = i

			# inner loop - loop through all items in the list after index i
			for j in range(i+1, len(list)):

				# compare values and update min_index as needed
				if list[j] < list[min_index]:
					min_index = j

			# swap the elements of the list to sort in ascending order
			list[i], list[min_index] = list[min_index], list[i]

		return list

 
# generate a list of 10 random numbers between 1 and 100 
random_list = random.sample(range(1, 100), 10)
print(f"List of randomly generated numbers = {random_list}")
ss = SelectionSort()
sorted_list = ss.sort(random_list)
print(f"List of sorted numbers = {sorted_list}")



#!/usr/bin/env python3
# Source: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# Classic bubble sort

# making it a class a bad idea?
import time

class BubbleSort:

	@staticmethod
	def swap(arr, i, j):
		arr[i], arr[j] = arr[j], arr[i]

	@staticmethod
	def bubbleSort(arr):
			
			# Start the timer
			start_time = time.start()

			# Main algorithm
			n = len(arr)
			for i in range(n-1):
					for j in range(0, n-i-1):
							if arr[j] > arr[j + 1]:
									BubbleSort.swap(arr, j, j+1)
			end_time = time.time()
			return end_time - start_time
					
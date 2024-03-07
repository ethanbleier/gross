#!/usr/bin/env python3

import csv
import os
import pprint
import time
from bubble_sort import BubbleSort
import tqdm
import matplotlib.pyplot as plt

class Measure_Runtime():
	def __init__(self, filename):
		self.filename = filename
		self.data = None

		# if filename doesn't exist, means we probably havent generated the data yet. so we do that here.
		if filename is None or not os.path.exists(filename):
				self.data = self.generate_data()
		else:
				self.data = self.read_data(filename)

	def get_data(self):
		return self.data
	
	# this method uses the DataGen.py script to...  ...generate data
	def generate_data(self) -> list:
		if os.path.exists("DataGen.py"):
			os.system("python3 DataGen.py")
			filename = "sawtoothAscendingDataWithNoise0.csv"
			return self.read_data(filename)
		else:
			print("Data gen script not found")
			return []
		
	def read_data(self, filename) -> list:
		# Need a way of keeping track of the best performing algorithm
		data = []
		with open(filename, 'r') as file:
			csv_file = csv.DictReader(file)
			for row in csv_file:
				try:
					# row needs to be float
					r_flt = float(row[next(iter(row))])
					data.append(r_flt)
				except (ValueError, KeyError):
					print(f"Encountered an invalid row({row})")
		return data

	def plot_runtime(runtimes):
		arr_size = range(len(runtimes))
		plt.plot(arr_size, runtimes, marker='o')
		plt.xlabel('Array Length')
		plt.ylabel('Runtime (s)')
		plt.title('Bubble Sort Runtime Analysis')
		plt.grid(True)
		plt.show()

	def solve(self, data):
		# TODO: Refactor this
		A = BubbleSort()
		new_data, runtimes = A.bubbleSort(data)
		
		print("**** DONE ****")
		for item in range(len(new_data)):
			pprint.pprint(new_data[item])
		self.plot_runtime(runtimes)


if __name__ == "__main__":
	filename = "dataset/sawtoothAscendingDataWithNoise0.csv"
	A = Measure_Runtime(filename)
	A_data = A.get_data()
	
	print("**** <START DATA> ****\n")
	pprint.pprint(A_data)
	print("**** <STOP DATA> ****\n\n")
	A.solve(A_data)


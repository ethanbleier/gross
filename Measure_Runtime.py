#!/usr/bin/env python3

import csv
import os
import pprint
import time
from bubble_sort import BubbleSort

class Measure_Runtime():
	def __init__(self, filename):
		# if filename doesn't exist, means we probably havent generated the data yet. so we do that here.
		if filename is None:
				self.data = self.generate_data()
		else:
				self.data = self.read_data(filename)

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

	@staticmethod
	def solve(data):
		A = BubbleSort()
		measured_count = set()
		start = time.time()
		A.bubbleSort(data)
		end = time.time()
		print(f"dataset size: {len(data)}, performance in seconds: {end - start:.6f}")
		measured_count.add(1)
		print("Measure count: ", measured_count)

if __name__ == "__main__":
	filename = "dataset/sawtoothAscendingDataWithNoise0.csv"
	measure = Measure_Runtime(filename)
	data = Measure_Runtime.solve(measure.data)
	pprint.pprint(data)

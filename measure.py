#!/usr/bin/env python3

''' 
Inspired by: https://video.cs50.io/WbzNRTTrX0g?screen=0Towr-pBuzw&start=3969

This program aims to determine if the results are interesting enough to make meaningful observations from
Code is adapted from a maze search algorithm into an algorithm measurer that compares different algorithms and yadayadayada

For readability and simplicity, I'm beginning this project by comparing just two algorithms
1: Bubble Sort 2: TBA, over one dataset, and graphing the results
The graph should make it exeedingly clear which algo is faster
data will become interesting as I add more algorithms
'''

# chosen sample:
# dataset/sawtoothAscendingDataWithNoise0.csv
from bubble_sort import BubbleSort

class Node():
    def __init__(self, A, parent, dataset):
        if dataset is None:
            self.dataset = self.DataGen()
        else:
            self.dataset = dataset
        
        # A is the algo self is using/measuring
        self.A = A

        # state should return the name of csv file? 
        # self.state = state

        # in case we want to go backwards for whatever future reason, 
        # lets monitor the parent node
        self.parent = parent

        # am I doing this right?
        self.time = A.bubbleSort(dataset)
        
        # Switch to true after we measure the time
        # am I doing this right?
        self.measured = False

# simple stack with a contains_dataset() -> bool
class StackRoot():
    def __init__(self):
        self.root = []

    def add(self, node):
        self.root.append(node)

    def contains_dataset(self, dataset):
        return any(node.dataset == dataset for node in self.root)

    def empty(self):
        return len(self.root) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty root")
        else:
            node = self.root[-1]
            self.root = self.root[:-1]
            return node

# FIFO
class QueueRoot(StackRoot): # QueueRoot extends StackRoot (python > java)
    
    def remove(self):
        if self.empty():
            raise Exception("empty root")
        else:
            node = self.root[0]
            self.root = self.root[1:]
            return node

import csv
import os

class Measure():

    def __init__(self, filename):
        if filename is None:
            self.data = self.generate_data()
        else:
            self.data = self.read_data(filename)
        
        def generate_data(self):
            if os.path.exists("DataGen.py"):
                os.system("python3 DataGen.py")
                filename = "sawtoothAscendingDataWithNoise0.csv"
                return read_data(filename)
            else:
                print("Data gen script not found")
                return []
        
        def read_data(self, filename):
            # Need a way of keeping track of the best performing algorithm
            data = []
            with open(filename, 'r') as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    try:
                        # row needs to be float
                        r_flt = float(row[next(iter(row))])
                        self.data.append(r_flt)
                    except (ValueError, KeyError):
                        print(f"Encountered an invalid row({row})")
            return data

    def solve(self):
        """Finds best algorithm"""
        A = BubbleSort()

        # Keep track of number of states measured (instead of explored)
        self.num_measured = 0

        # __init__(A, state, parent, dataset)
        start = Node(A=A, parent=None, dataset=self.data)

        # TODO: Go through multiple nodes, not just one
        root = StackRoot()
        root.add(start)

        # Initialize an empty measured set
        self.measured = set()

        # Keep looping until optimal algorithm (A*) is found
        # while True:

        #     # nothing left in root
        #     if root.empty():
        #         raise Exception("oops")

        #     # Choose a node from the root
        #     node = root.remove()

        #     # probably wise to keep track of this
        #     # self.num_explored += 1
            
        #     # measure the time taken to sort
        #     # TODO: more thinking less random keystrokes
        #     performance = A.bubbleSort(self.data) # big yikes here
        #     size = self.data.size()
        #     print(f"dataset size: {size}, performance in seconds: {performance:.6f}\n")
        #     node.measured = True
        #     self.explored.add(node.state)

        import time
        
        start_time = time.time()
        A.bubbleSort(self.data)
        end_time = time.time()
        print(f"dataset size: {len(self.data)}, performance in seconds: {end_time - start_time:.6f}")
        self.num_measured += 1

if __name__ == "__main__":
   filename = "dataset/sawtoothAscendingDataWithNoise0.csv"
   measure = Measure(filename)
   measure.solve()
   # TODO: Add a pretty print to see data before sorting and after sorting
   # TODO: implement mat plot lib graphing
   # TODO: Did we actually sort any data?

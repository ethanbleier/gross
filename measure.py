#!/usr/bin/env python3

''' 
Ethan Bleier
Inspired by: https://video.cs50.io/WbzNRTTrX0g?screen=0Towr-pBuzw&start=3969
This program aims to determine if research can be done with search
Code is adapted from a maze search algorithm

For readability and simplicity, I'm beginning this project by comparing just two algorithms
1: Bubble Sort 2: TBA, over one dataset, and graphing the results
The graph should make it exeedingly clear which algo is faster
data will become interesting as I add more algorithms
'''

import sys
import csv
# dataset/sawtoothAscendingDataWithNoise0.csv

class Node():
    def __init__(self, A, state, parent, dataset):
        self.A = A

        # state should return the name of csv file? 
        self.state = state

        # in case we want to go backwards for whatever future reason, 
        # lets monitor the parent node
        self.parent = parent

        # am I doing this right? 
        self.dataset = dataset

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


class Measure():

    def __init__(self, filename):
        # Need a way of keeping track of the best performing algorithm
        self.data = []
        with open(filename, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                self.data.append(row)

    def solve(self):
        """Finds best algorithm"""
        from bubble_sort import BubbleSort
        A = BubbleSort()

        # Keep track of number of states measured (instead of explored)
        self.num_measured = 0

        # __init__(A, state, parent, dataset)
        start = Node(state=self.start, A=A, parent=None, dataset=self.data)
        root = StackRoot()
        root.add(start)

        # Initialize an empty measured set
        self.measured = set()

        # Keep looping until optimal algorithm (A*) is found
        while True:

            # nothing left in root bruh
            if root.empty():
                raise Exception("oops")

            # Choose a node from the root
            node = root.remove()

            # probably wise to keep track of this
            # self.num_explored += 1
            
            # measure the time taken to sort
            # TODO: more thinking less random keystrokes
            performance = A.bubbleSort(self.data) # big yikes here
            node.measured = True
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not root.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    root.add(child)



# This program aims to determine if research can be done with search

import sys
import csv
# dataset/sawtoothAscendingDataWithNoise0.csv

class Node():
    def __init__(self, A, state, parent, dataset):
        self.A = A
        self.state = state
        self.parent = parent
        self.dataset = dataset

# simple stack
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


''' 
Inspired by: https://video.cs50.io/WbzNRTTrX0g?screen=0Towr-pBuzw&start=3969
'''

class Measure():

    def __init__(self, filename):
        self.data = []
        with open(filename, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                self.data.append(row)

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # result = []
        # for action, (r, c) in candidates:
        #     if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
        #         result.append((action, (r, c)))
        # return result

    def solve(self):
        """Finds best algorithm"""

        # Keep track of number of states measured (instead of explored)
        self.num_measured = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        root = StackRoot()
        root.add(start)

        # Initialize an empty measured set
        self.measured = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if root.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = root.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not root.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    root.add(child)



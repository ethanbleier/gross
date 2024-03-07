#!/usr/bin/env python3
# Source: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# Classic bubble sort
import tqdm
import matplotlib.pyplot as plt
import time

class BubbleSort:
    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def bubbleSort(arr) -> list:
        # Main algorithm
        n = len(arr)
        start = time.time()
        for i in tqdm.tqdm(range(n-1), desc='Sorting', position=0, leave=True): 
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1]:
                    BubbleSort.swap(arr, j, j+1)
        end = time.time()
        return arr, (end - start)

    @staticmethod
    def analyze_runtime():
        array_lengths = list(range(100, 1001, 100))
        runtimes = []

        for length in array_lengths:
            array = list(range(length, 0, -1))  # Reverse sorted array
            sorted_array, runtime = BubbleSort.bubbleSort(array)
            runtimes.append(runtime)

        BubbleSort.plot_runtime(array_lengths, runtimes)

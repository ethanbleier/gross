"""
Created on Mon Oct 30 13:54:34 2023
Last Modified: Tues Jan 9 19:54:10 2023

@author: Matthew James Sanchez
@co_author : Logan Powser
@contributor : Ethan Bleier

This program provides functions to generate and visualize various types of waveforms and datasets.
It includes methods to generate ascending/descending random data, sawtooth waves, square waves, sine waves, 
and sawtooth-like patterns with increasing amplitude. Additionally, it includes methods to generate datasets 
with specified inversions needed to sort or with out-of-order elements. The program also allows the user 
to create and plot different waveforms and save datasets to separate text files.

Furthermore, variations of the waveform functions are available to introduce noise and randomness, creating disorder in the data.
These variations are designed for testing sorting algorithms with noisy and disordered datasets, providing a realistic simulation 
of data encountered in real-world scenarios.



To use the program, you can either call individual methods or use the `create_and_plot_waves` 
function to generate and visualize various waveforms. Additionally, you can use the 
`generateDatasets` function to generate datasets and save them to separate text files.

Note: 
    Make sure to adjust the parameters as needed for your specific use case.

2/22/24 (Ethan): fixed an annoyance with generateDatasets()
                 csv files are now written to ./datasets correctly
                 #TODO: Add example usage of create_and_plot_waves() since there are so many params

Default param usage: 
    if __name__ == "__main__":
        n = 5
        generateDatasets(n, output_folder="datasets")

"""

import random
import os
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from pandas import DataFrame

def ascendingData(min_value, max_value, array_length, step):
    """
    Generate an array of unique ascending values within a specified range.

    Parameters:
        - min_value (int): Minimum value for the range.
        - max_value (int): Maximum value for the range.
        - array_length (int): Length of the output array.
        - step (float): Step size between values.

    Returns:
        - list: Array of ascending values.
    """
    if array_length < 0 or min_value > max_value or step <= 0:
        raise ValueError("Invalid input parameters")

    ascending_array = [min_value + i * step for i in range(array_length)]
    return ascending_array

def descendingData(min_value, max_value, array_length, step):
    """
    Generate an array of unique descending values within a specified range.

    Parameters:
        - min_value (int): Minimum value for the range.
        - max_value (int): Maximum value for the range.
        - array_length (int): Length of the output array.
        - step (float): Step size between values.

    Returns:
        - list: Array of descending values.
    """
    if array_length < 0 or min_value > max_value or step <= 0:
        raise ValueError("Invalid input parameters")

    descending_array = [max_value - i * step for i in range(array_length)]
    return descending_array

def ascendingDataWithNoise(min_value, max_value, array_length, noise_factor=1.0):
    """
    Generate an array of unique random ascending values within a specified range.

    Parameters:
        - min_value (int): Minimum value for random range.
        - max_value (int): Maximum value for random range.
        - array_length (int): Length of the output array.
        - noise_factor (float): Factor to control the level of randomness. Default is 1.0.

    Returns:
        - list: Array of ascending random values.
    """
    scaled_range = int((max_value - min_value + 1) * noise_factor)
    scaled_range = max(1, scaled_range)  # Ensure that scaled_range is at least 1
    random_array = sorted(random.sample(range(min_value, min_value + scaled_range), min(array_length, scaled_range)))
    return random_array

def descendingDataWithNoise(min_value, max_value, array_length, noise_factor=1.0):
    """
    Generate an array of unique random descending values within a specified range.

    Parameters:
        - min_value (int): Minimum value for random range.
        - max_value (int): Maximum value for random range.
        - array_length (int): Length of the output array.
        - noise_factor (float): Factor to control the level of randomness. Default is 1.0.

    Returns:
        - list: Array of descending random values.
    """
    scaled_range = int((max_value - min_value + 1) * noise_factor)
    scaled_range = max(1, scaled_range)  # Ensure that scaled_range is at least 1
    random_array = sorted(random.sample(range(max_value - scaled_range + 1, max_value + 1), min(array_length, scaled_range)), reverse=True)
    return random_array

def sawtoothAscendData(array_length, sawtooth_period, multiplier=1.0):
    """
    Generate ascending data with a sawtooth-like pattern.

    Parameters:
        - array_length (int): Length of the output array.
        - sawtooth_period (float): Period of the sawtooth wave.
        - multiplier (float): Multiplier for adjusting the amplitude of the sawtooth wave (default is 1.0).

    Returns:
        - numpy array: Array with ascending sawtooth-like data.
    
    Note:
        Code adapted from https://stackoverflow.com/questions/65543325/generating-sawtooth-wave-with-python-math-module
    """
    t = np.linspace(0, 1, array_length)
    data = multiplier * signal.sawtooth(2 * np.pi * (1 / sawtooth_period) * t)
    return data

def sawtoothDescendData(array_length, sawtooth_period, multiplier=1.0):
    """
    Generate descending data with a sawtooth-like pattern.

    Parameters:
        - array_length (int): Length of the output array.
        - sawtooth_period (float): Period of the sawtooth wave.
        - multiplier (float): Multiplier for adjusting the amplitude of the sawtooth wave (default is 1.0).

    Returns:
        - numpy array: Array with descending sawtooth-like data.
    """
    t = np.linspace(0, 1, array_length)
    data = -multiplier * signal.sawtooth(2 * np.pi * (1 / sawtooth_period) * t)
    return data

def sawtoothAscendDataWithNoise(array_length, sawtooth_period, noise_level=0.1, multiplier=1.0):
    """
    Generate ascending data with a sawtooth-like pattern and added noise.

    Parameters:
        - array_length (int): Length of the output array.
        - sawtooth_period (float): Period of the sawtooth wave.
        - noise_level (float): Level of random noise to be added. Default is 0.1.
        - multiplier (float): Multiplier for adjusting the amplitude of the sawtooth wave (default is 1.0).

    Returns:
        - numpy array: Array with ascending sawtooth-like data and added noise.
    """
    t = np.linspace(0, 1, array_length)
    sawtooth_wave = multiplier * signal.sawtooth(2 * np.pi * (1 / sawtooth_period) * t)
    noise = np.random.normal(0, noise_level, array_length)
    data_with_noise = sawtooth_wave + noise
    return data_with_noise

def sawtoothDescendDataWithNoise(array_length, sawtooth_period, noise_level=0.1, multiplier=1.0):
    """
    Generate descending data with a sawtooth-like pattern and added noise.

    Parameters:
        - array_length (int): Length of the output array.
        - sawtooth_period (float): Period of the sawtooth wave.
        - noise_level (float): Amplitude of the added noise (default is 0.1).
        - multiplier (float): Multiplier for adjusting the amplitude of the sawtooth wave (default is 1.0).

    Returns:
        - numpy array: Array with descending sawtooth-like data and added noise.
    """
    t = np.linspace(0, 1, array_length)
    sawtooth_data = -multiplier * signal.sawtooth(2 * np.pi * (1 / sawtooth_period) * t)
    noise = noise_level * np.random.normal(size=array_length)
    data_with_noise = sawtooth_data + noise
    return data_with_noise

def squareData(size, frequency, multiplier=1.0):
    """
    Create a square wave-like pattern.

    Parameters:
        - size (int): The size of the data array.
        - frequency (float): The frequency of the square wave.
        - multiplier (float): Multiplier for adjusting the amplitude of the square wave (default is 1.0).

    Returns:
        - numpy array: Array representing the square wave.
    
    Note:
        Code adapted from https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.square.html
    """
    t = np.linspace(0, 1, size, endpoint=False)
    square_wave = multiplier * np.sign(np.sin(2 * np.pi * frequency * t))
    return square_wave

def squareDataWithNoise(size, frequency, noise_amplitude=0.1, multiplier=1.0):
    """
    Create a square wave-like pattern with added noise.

    Parameters:
        - size (int): The size of the data array.
        - frequency (float): The frequency of the square wave.
        - noise_amplitude (float): Amplitude of the added noise.
        - multiplier (float): Multiplier for adjusting the amplitude of the square wave (default is 1.0).

    Returns:
        - numpy array: Array representing the square wave with noise.
    """
    t = np.linspace(0, 1, size, endpoint=False)
    square_wave = multiplier * np.sign(np.sin(2 * np.pi * frequency * t))
    
    # Add noise to the square wave
    noise = noise_amplitude * np.random.randn(size)
    square_wave_with_noise = square_wave + noise
    
    return square_wave_with_noise

def sinData(multiplier=1.0):
    """
    Generate sine wave data.

    Parameters:
        - multiplier (float): Multiplier for adjusting the amplitude of the sine wave (default is 1.0).

    Returns:
        - numpy array: Array with time and amplitude data of a sine wave.
    """
    time = np.arange(0, 10, 0.1)
    amplitude = multiplier * np.sin(time)
    data = np.column_stack((time, amplitude))
    return data

def sinDataWithNoise(noise=0.1, multiplier=1.0):
    """
    Generate sine wave data with added noise.

    Parameters:
        - noise (float): Magnitude of the added noise.
        - multiplier (float): Multiplier for adjusting the amplitude of the sine wave (default is 1.0).

    Returns:
        - numpy array: Array with time and amplitude data of a sine wave with added noise.
    """
    time = np.arange(0, 10, 0.1)
    amplitude = multiplier * (np.sin(time) + noise * np.random.normal(size=len(time)))
    data = np.column_stack((time, amplitude))
    return data

def sawtoothAscendDataWithIncreasingAmplitude(array_length, sawtooth_period, multiplier=1.0):
    """
    Generate ascending data with a sawtooth-like pattern and increasing amplitude.

    Parameters:
        - array_length (int): Length of the output array.
        - sawtooth_period (float): Period of the sawtooth wave.
        - multiplier (float): Multiplier for adjusting the amplitude of the sawtooth wave (default is 1.0).

    Returns:
        - numpy array: Array with ascending sawtooth-like data and increasing amplitude.
    """
    t = np.linspace(0, 1, array_length)
    data = multiplier * signal.sawtooth(2 * np.pi * (1 / sawtooth_period) * t) * (t % (1/sawtooth_period)) + 3.7 * (t*0.7)
    return data

def genDataWithInversions(len=10, numInversions=5):
    """
    Generate data with specified number of inversions needed to sort.

    Parameters:
        - len (int): Length of array to generate. Default is 10
        - numInversions (int): Number of inversions to introduce to the data. Default is 5.

    Returns:
        - numpy array: Array that requires numInversions inversions to sort it.
    
    Note:
        Code adapted from https://stackoverflow.com/questions/54506366/algorithm-to-generate-an-array-with-n-length-and-k-number-of-inversions-in-on-l
    """
    a = [0] * len
    b = [0] * len

    for i in range(1, len):
        a[i] = 1 + a[i - 1]

    if len == 0 or numInversions == 0:
        return a
    else:
        i = 0
        while numInversions > 0:
            if numInversions > len - i - 1:
                b[i] = a[len - 1 - i]
            else:
                # Extra array c to store value
                c = [0] * (numInversions + 1)
                for j in range(i, len - 1 - numInversions):
                    b[j] = j - i
                for j in range(len - 1 - numInversions, len):
                    c[j - (len - 1 - numInversions)] = j - i
                b[len - 1 - numInversions] = c[numInversions]
                for j in range(len - numInversions, len):
                    b[j] = c[j - (len - numInversions)]
                break

            numInversions = numInversions - (len - 1 - i)
            i += 1

        return b
    
def genDataOutOfPlace(lenArr, countOutOfPlace):
    """
    Generate an array with out-of-order elements.

    Parameters:
    - lenArr (int): The length of the array to be generated.
    - countOutOfPlace (int): The number of out-of-place swaps to be performed.

    Returns:
    - list: A sorted array with the specified number of out-of-place swaps.

    Note:
    - The value of `countOutOfPlace` should be a multiple of two. 
        It will only procus an out of place count that is a multiple of two because we swap two elements at a time
    """

    sorted_array = list(range(lenArr))

    swaps_count = 0
    index = 0
    
    if countOutOfPlace % 2 != 0:
        raise ValueError("countOutOfPlace should be a multiple of two.")

    # Perform swaps until the count of swaps reaches countOutOfPlace
    while swaps_count < countOutOfPlace:
        # Generate a random index within the array bounds
        index = random.randint(0, lenArr - 3)

        # Swap the current element with the element two indexes next
        sorted_array[index], sorted_array[index + 2] = sorted_array[index + 2], sorted_array[index]

        # Increment the swaps count by two for the first swap, and by one for subsequent swaps
        swaps_count += 2 if swaps_count == 0 else 1

    return sorted_array

def create_and_plot_waves(array_len=1000, sawtooth_period=0.25, min_val=0, max_val=100, square_freq=1.0, sine_amp=1.0, sine_time=10, noise=200, ArrayLen=10, invCount=5, count_of_out_of_place = 6, multiplier = 125):
    """
    Generate and plot various waveforms including ascending/descending random data, sawtooth waves,
    square waves, sine waves, and sawtooth-like patterns with increasing amplitude.

    Parameters:
        - array_len (int): Length of the output arrays. Default is 1000.
        - sawtooth_period (float): Period of the sawtooth wave. Only used for sawtooth methods. Default is 0.25.
        - min_val (int): Minimum value for random range. Only used for ascending/descending methods. Default is 0.
        - max_val (int): Maximum value for random range. Only used for ascending/descending methods. Default is 100.
        - square_freq (float): Frequency of the square wave. Only used for square methods. Default is 1.0.
        - sine_amp (float): Amplitude of the sine wave. Only used for sin methods. Default is 1.0.
        - sine_time (float): Time range for the sine wave. Only used for sin methods. Default is 10.
        - noise (int): The amount of noise or randomness introduced to the ascending and descending with randomness functions.Used for all methods that introduce randomness/noise Default is 200.
        - invArrayLen (int): The length of the array of the genDataWithInversions method. Default 10.
        - invCount (int): The amount of inversions needed to sort the array generated by the genDataWithInversioins method. Default 5.
        - count_of_out_of_place: The number of index values we want to be out of place in our return data of the genDataOutOfPlace method. Default is 5.

    Returns:
        - None: The function generates and plots various waveforms.
    """
    # Generate ascending random data and plot
    ascending_data = ascendingData(min_val, max_val, array_len, 1)
    plt.figure()
    plt.plot(ascending_data, label='Ascending Data')
    plt.title('Ascending Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    descending_data = descendingData(min_val, max_val, array_len, 1)
    plt.figure()
    plt.plot(descending_data, label='Descending Data')
    plt.title('Descending Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    ascending_random_data = ascendingDataWithNoise(min_val, max_val, array_len,noise)
    plt.figure()
    plt.plot(ascending_random_data, label='Ascending Random Data')
    plt.title('Ascending Random Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Generate descending random data and plot
    descending_random_data = descendingDataWithNoise(min_val, max_val, array_len,noise)
    plt.figure()
    plt.plot(descending_random_data, label='Descending Random Data')
    plt.title('Descending Random Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Generate ascending data with sawtooth-like pattern and plot
    ascending_sawtooth_data = sawtoothAscendData(array_len, sawtooth_period,multiplier)
    plt.figure()
    plt.plot(ascending_sawtooth_data, label='Ascending Sawtooth Data')
    plt.title('Ascending Sawtooth Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate ascending data with sawtooth-like pattern and plot
    ascending_sawtooth_data = sawtoothAscendDataWithNoise(array_len, sawtooth_period)
    plt.figure()
    plt.plot(ascending_sawtooth_data, label='Ascending Sawtooth Data With Noise')
    plt.title('Ascending Sawtooth Data With Noise')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate ascending data with sawtooth-like pattern and plot
    ascending_sawtooth_data = sawtoothAscendDataWithNoise(array_len, sawtooth_period,multiplier)
    plt.figure()
    plt.plot(ascending_sawtooth_data, label='Ascending Sawtooth Data With Noise & Multiplier')
    plt.title('Ascending Sawtooth Data With Noise & Multiplier')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Generate descending data with sawtooth-like pattern and plot
    descending_sawtooth_data = sawtoothDescendData(array_len, sawtooth_period,multiplier)
    plt.figure()
    plt.plot(descending_sawtooth_data, label='Descending Sawtooth Data')
    plt.title('Descending Sawtooth Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate descending data with sawtooth-like pattern and plot
    descending_sawtooth_data = sawtoothDescendDataWithNoise(array_len, sawtooth_period)
    plt.figure()
    plt.plot(descending_sawtooth_data, label='Descending Sawtooth Data With Noise')
    plt.title('Descending Sawtooth Data With Noise')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate descending data with sawtooth-like pattern and plot
    descending_sawtooth_data = sawtoothDescendDataWithNoise(array_len, sawtooth_period,multiplier)
    plt.figure()
    plt.plot(descending_sawtooth_data, label='Descending Sawtooth Data With Noise & Multipler')
    plt.title('Descending Sawtooth Data with Noise & Multiplier')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Generate square wave data and plot
    square_wave_data = squareData(array_len, square_freq,multiplier)
    plt.figure()
    plt.plot(square_wave_data, label='Square Wave Data')
    plt.title('Square Wave Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate square wave data and plot
    square_wave_data = squareDataWithNoise(array_len, square_freq)
    plt.figure()
    plt.plot(square_wave_data, label='Square Wave Data With Noise')
    plt.title('Square Wave Data With Noise')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate square wave data and plot
    square_wave_data = squareDataWithNoise(array_len, square_freq,multiplier)
    plt.figure()
    plt.plot(square_wave_data, label='Square Wave Data With Noise & Multiplier')
    plt.title('Square Wave Data With Noise & Multiplier')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Generate sine wave data and plot
    sine_wave_data = sinData(multiplier)
    plt.figure()
    plt.plot(sine_wave_data[:, 0], sine_wave_data[:, 1] * sine_amp, label='Sine Wave Data')
    plt.title('Sine Wave Data')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate sine wave data and plot
    sine_wave_data = sinDataWithNoise()
    plt.figure()
    plt.plot(sine_wave_data[:, 0], sine_wave_data[:, 1] * sine_amp, label='Sine Wave Data With Noise')
    plt.title('Sine Wave Data With Noise')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
    
    # Generate sine wave data and plot
    sine_wave_data = sinDataWithNoise(multiplier)
    plt.figure()
    plt.plot(sine_wave_data[:, 0], sine_wave_data[:, 1] * sine_amp, label='Sine Wave Data With Noise & Multiplier')
    plt.title('Sine Wave Data With Noise & Multiplier')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Generate ascending data with sawtooth-like pattern and increasing amplitude, and plot
    ascending_sawtooth_amplitude_data = sawtoothAscendDataWithIncreasingAmplitude(array_len, sawtooth_period, multiplier)
    plt.figure()
    plt.plot(ascending_sawtooth_amplitude_data, label='Ascending Sawtooth with Increasing Amplitude')
    plt.title('Ascending Sawtooth with Increasing Amplitude')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Get a dataset with specified inversions needed to sort
    result = genDataWithInversions(ArrayLen, invCount)
    print(result)
    
    # Get a datawt with specified items out of place. 
    result_array = genDataOutOfPlace(ArrayLen, count_of_out_of_place)
    print(result_array)

# LOGAN START HERE. You should not need to edit the methods above.
def generateDatasets(numToGen, output_folder="datasets",array_len=1000, sawtooth_period=0.25, min_val=0, max_val=100, square_freq=1.0, sine_amp=1.0, sine_time=10, noise=200, invArrayLen=10, invCount=5, count_of_out_of_place = 6, multiplier = 125):
    """
    Generate datasets using various methods and write each dataset to a separate text file.

    Parameters:
        - output_folder (str): Folder where the datasets will be saved. Default is "datasets".
        - array_len (int): Length of the output arrays. Default is 1000.
        - sawtooth_period (float): Period of the sawtooth wave. Only used for sawtooth methods. Default is 0.25.
        - min_val (int): Minimum value for random range. Only used for ascending/descending methods. Default is 0.
        - max_val (int): Maximum value for random range. Only used for ascending/descending methods. Default is 100.
        - square_freq (float): Frequency of the square wave. Only used for square methods. Default is 1.0.
        - sine_amp (float): Amplitude of the sine wave. Only used for sin methods. Default is 1.0.
        - sine_time (float): Time range for the sine wave. Only used for sin methods. Default is 10.
        - noise (int): The amount of noise or randomness introduced to the ascending and descending with randomness functions.Used for all methods that introduce randomness/noise Default is 200.
        - invArrayLen (int): The length of the array of the genDataWithInversions method. Default 10.
        - invCount (int): The amount of inversions needed to sort the array generated by the genDataWithInversioins method. Default 5.
        - count_of_out_of_place (int): The number of index values we want to be out of place in our return data of the genDataOutOfPlace method. Default is 5.
        - multiplier (int): The constant multiplier for some of our functions. Default is 125.
        
        Note:

            1. General Updates:
                - Modify the starter code to include a parameter named 'numToGen.'
                - This parameter will determine the number of datasets to be generated for each method with randomness.

    2. Applying Randomness to Specific Methods:
        - Update the following methods to incorporate randomness:
            - ascendingDataWithNoise
            - descendingDataWithNoise
            - sawtoothAscendDataWithNoise
            - sawtoothDescendDataWithNoise
            - squareDataWithNoise
            - sinDataWithNoise
        - All other data-generating functions should remain being run once as they are since they lack randomness and produce consistent data.
        - Write each dataset generated out to a CSV file.
   
    3. Iterative Execution for genDataOutOfPlace:
        - Implement a for loop for the method genDataOutOfPlace.
        - The loop should iterate up to the specified 'count_out_of_place' parameter.
        - For each iteration, execute the method with the loop index (1 to count_out_of_place).
        - Store the resulting dataset in a data frame.
        - Write the data frame to a CSV file.
        - Overwrite the same data frame with each new dataset to conserve resources.

    4. Similar Approach for genDataWithInversions:
        - Implement a for loop for the method genDataWithInversions.
        - The loop should iterate up to the specified 'invCount' parameter.
        - For each iteration, execute the method with the loop index (1 to invCount).
        - Store the resulting dataset in a data frame.
        - Write the data frame to a CSV file.
        - Overwrite the same data frame with each new dataset to avoid unnecessary resource usage.
    """
    try:
        folder = os.mkdir(output_folder)
    except OSError as e:
        print(e)

    #1
    for n in range(numToGen):
        adwn = np.array(ascendingDataWithNoise(min_val, max_val, array_len, noise))
        a = DataFrame(adwn)
        asc = os.path.join(output_folder, f"ascendingDataWithNoise{n}.csv")
        a.to_csv(asc, index=False)
        
        ddwn = np.array(descendingDataWithNoise(min_val, max_val, array_len, noise))
        d = DataFrame(ddwn)
        desc = os.path.join(output_folder, f"descendingDataWithNoise{n}.csv")
        d.to_csv(desc, index=False)

        sadwn = np.array(sawtoothAscendDataWithNoise(array_len, sawtooth_period, noise, multiplier))
        sa = DataFrame(sadwn)
        sawAsc = os.path.join(output_folder, f"sawtoothAscendingDataWithNoise{n}.csv")
        sa.to_csv(sawAsc, index=False)

        sddwn = np.array(sawtoothDescendDataWithNoise(array_len, sawtooth_period, noise, multiplier))
        sd = DataFrame(sddwn)
        sawDesc = os.path.join(output_folder, f"sawtoothDescendingDataWithNoise{n}.csv")
        sd.to_csv(sawDesc, index=False)

        sqdwn = np.array(squareDataWithNoise(array_len , square_freq, noise, multiplier))
        sq = DataFrame(sqdwn)
        square = os.path.join(output_folder, f"squareDataWithNoise{n}.csv")
        sq.to_csv(square, index=False)

        sindwn = np.array(sinDataWithNoise(noise, multiplier))
        si = DataFrame(sindwn)
        sin = os.path.join(output_folder, f"sinDataWithNoise{n}.csv")
        si.to_csv(sin, index=False)
    #2          
    for c in range(2, count_of_out_of_place, 2):
        doop = os.path.join(output_folder, f"dataOutOfPlace{c}.csv")
        dataOutOfPlace = np.array(genDataOutOfPlace(array_len, c))
        df = DataFrame(dataOutOfPlace)
        df.to_csv(doop, index=False)

    for i in range(invCount):
        dwi = os.path.join(output_folder, f"dataWithInversions{i}.csv")
        dataWithInversions = np.array(genDataWithInversions(invArrayLen, i))
        df = DataFrame(dataWithInversions)
        df.to_csv(dwi, index=False)

      
# Driver code with default params
if __name__ == "__main__":
    n = 5
    generateDatasets(n, output_folder="dataset")

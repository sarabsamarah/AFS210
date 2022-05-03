import random
import time


def randomShuffle(input, inputData):
    for i in range(inputData -1):
        x = random.randint(0, i)
        input[i], input[x] = input[x], input[i]
    return input

input = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
inputLength = len(input)


print('Original List:' ,input)
start_time = time.time()
print("Shuffled list:",randomShuffle(input,inputLength))
end_time = time.time()
print(f'The excution time is: {end_time-start_time}')

start_time_one = time.time()
print("Shuffled list:",randomShuffle(input,inputLength))
end_time_one = time.time()
print(f'The excution time is: {end_time_one-start_time_one}')

start_time_two = time.time()
print("Shuffled list:",randomShuffle(input,inputLength))
end_time_two = time.time()
print(f'The excution time is: {end_time_two-start_time_two}')
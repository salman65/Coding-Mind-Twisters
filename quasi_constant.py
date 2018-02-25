from random import *

def solution(arr):
    arr.sort()
    start = 0
    i = 0
    largest_amps = []
    while i < len(arr):
        curr_ind = 0
        jump = 0
        for j in range(start, len(arr)):
            if(arr[j] == arr[i]):
                jump = jump + 1
            if(arr[j] - arr[i] < 2):
                curr_ind = curr_ind + 1
            else:
                break
        largest_amps.append(curr_ind)
        if(jump == 0):
            start = start + 1
            i = i + 1
        else:
            start = start + jump
            i = i + jump
    return max(largest_amps)

if __name__ == "__main__":
    arr = []
    for i in range(10000):
        arr.append(randint(1, 10000))
    ans = solution(arr)
    print(ans)

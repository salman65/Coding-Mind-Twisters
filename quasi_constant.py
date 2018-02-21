from random import *

def solution(arr):
    arr.sort()
    start = 0
    largest_amps = []
    for i in arr:
        current_amp = 0
        curr_ind = 0
        for j in range(start, len(arr)):
            if(arr[j] - i < 2):
                if((arr[j] - i) > current_amp):
                    current_amp = arr[j] - i
                curr_ind = curr_ind + 1
            else:
                break
        largest_amps.append(curr_ind)
        start = start + 1
    return max(largest_amps)

if __name__ == "__main__":
    arr = []
    for i in range(100):
        arr.append(randint(1, 100))
    ans = solution(arr)
    print(ans)

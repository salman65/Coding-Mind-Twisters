import random

def max_in_dic(dic):
    cur_max = dic[0][0]
    for i in dic:
        val = max(dic[i])
        if val > 1000000000:
            return 1000000000
        if val > cur_max:
            cur_max = val
    return cur_max

def solution(arr):
    dic = {}
    for r in range(len(arr)):
        breaker = 0
        dic[r] = [arr[r]]
        for c in range(len(dic)):
            val_arr = dic[c]
            val = val_arr[len(val_arr)-1] * arr[r]
            if(val == 0):
                breaker = 1
                break;
            if(r != c):
                dic[c].append(val)
        if(breaker == 1):
            break
    return max_in_dic(dic)

if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-10, 10))
    print(arr)
    sol = solution(arr)
    print(sol)

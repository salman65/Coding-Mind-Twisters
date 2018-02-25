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
    jump = 0
    for r in range(len(arr)):
        breaker = 0
        dic[r] = [arr[r]]
        c = jump
        while c < len(dic):
            val_arr = dic[c]
            val = val_arr[len(val_arr)-1] * arr[r]
            if(val == 0):
                jump = jump + 1
            elif(r != c):
                dic[c].append(val)
            c = c + 1
    return max_in_dic(dic)

if __name__ == "__main__":
    arr = [-3, 0, 5, 0.2, -4, -.6, 8, 0, 2.4, 0.5]
    # for i in range(10):
    #     arr.append(random.randint(-10, 10))
    print(arr)
    sol = solution(arr)
    print(sol)

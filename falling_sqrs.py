def rti(r):
    s = r.split('-')
    return (int(s[0]), int(s[1]))


def is_ol(r1, r2):
    s1 = rti(r1)
    s2 = rti(r2)
    if s1[0] <= s2[0] and s1[1] >= s2[1]:
        return (r1, "r1")
    elif s2[0] <= s1[0] and s2[1] >= s1[1]:
        return (r2, "r2")
    elif s1[0] <= s2[0] and (s1[1] >= s2[0] and s1[1] <= s2[1]):
        return (r2, "r1-r2")
    elif s2[0] <= s1[0] and (s2[1] >= s1[0] and s2[1] <= s1[1]):
        return (r2, "r2-r1")
    else:
        return (r2, None)


def is_empty(dic):
    return len(dic.keys()) == 0

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        res = {}
        ans = []
        max_calc = None
        for pos in positions:
            pr = f"{pos[0]}-{pos[0]+pos[1]-1}"
            if is_empty(res):
                res[pr] = pos[1]
                ans.append(pos[1])
                max_calc = pos[1]
            else:
                calc = None
                for item in sorted(res, key=res.get, reverse=True):
                    ol = is_ol(item, pr)
                    if ol[1] == "r2-r1" or ol[1] == "r1-r2":
                        res[ol[0]] = res[item] + pos[1]
                        calc = res[ol[0]]
                        break
                    elif ol[1] == "r2":
                        res[ol[0]] = res[item] + pos[1]
                        res.pop(item, None)
                        calc = res[ol[0]]
                        break
                    elif ol[1] == "r1":
                        res[pr] = res[item] + pos[1]
                        calc = res[pr]
                        break
                    else:
                        res[ol[0]] = pos[1]
                        calc = res[ol[0]]
                if calc > max_calc:
                    ans.append(calc)
                    max_calc = calc
                else:
                    ans.append(max_calc)
        return ans
from collections import Counter
def solution(str1, str2):
    def make_multiset(s):
        s = s.lower()
        result = []
        for i in range(len(s)-1):
            pair = s[i:i+2]
            if pair.isalpha():
                result.append(pair)
        return result
    
    list1 = make_multiset(str1)
    list2 = make_multiset(str2)
    
    c1 = Counter(list1)
    c2 = Counter(list2)
    intersection = 0
    union = 0
    
    keys = set(c1.keys()) | set(c2.keys())
    
    for k in keys:
        intersection += min(c1.get(k, 0), c2.get(k, 0))
        union += max(c1.get(k, 0), c2.get(k, 0))
    if union == 0:
        return 65536
    
    return int(intersection/union * 65536)
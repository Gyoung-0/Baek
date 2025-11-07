from typing import List

def solution(n):
    bin_n = list('0' + bin(n)[2:])
    idx = -1
    for i in range(len(bin_n)-1, 0, -1):
        if bin_n[i] == '1' and bin_n[i-1] == '0':
            idx = i
            bin_n[i-1] = '1'
            bin_n[i] = '0'
            break
    right_bin = bin_n[idx+1:]
    right_count = right_bin.count('1')
    
    new_right_bin = list('0' * (len(right_bin) - right_count) + '1' * right_count)
    
    final_bin = bin_n[:idx+1] + new_right_bin
    final_str_bin = "".join(final_bin)
    return int(final_str_bin, 2)
    
    
    
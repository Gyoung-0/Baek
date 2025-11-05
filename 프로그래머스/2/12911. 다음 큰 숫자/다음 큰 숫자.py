from typing import List

def solution(n):
    bin_n = list('0' + bin(n)[2:])
    idx = -1
    for i in range(len(bin_n) - 1, 0, -1):
        if bin_n[i-1] == '0' and bin_n[i] == '1':
            idx = i - 1
            break
            
    bin_n[idx] = '1'
    bin_n[idx+1] = '0'
    
    right_bin = bin_n[idx+2:]
    right_count = right_bin.count('1')
    
    new_right_bin = list('0' * (len(right_bin)-right_count) + '1' * right_count)
    
    final_bin_list = bin_n[:idx+2] + new_right_bin
    
    final_bin_str = "".join(final_bin_list)
    return int(final_bin_str, 2)
                        
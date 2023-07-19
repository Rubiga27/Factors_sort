import math

def get_factors_count(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 2
            if i == num // i:
                count -= 1
    return count

def sortArrayByFactors(A):
    A.sort(key=lambda x: (get_factors_count(x), x))
    return A
A=list(map(int,input().split()))
print(sortArrayByFactors(A))

"""
Input 1:
A = [6, 8, 9]
Input 2:
A = [2, 4, 7]


Output 1:
[9, 6, 8]
Output 2:
[2, 7, 4]
"""

#  ===================== Airlines  ========================
# Problem
# You are given a number of planes x and a number of passengers n. Each plane can carry 100 passengers.
# You need to find out how many more planes you need to carry all the passengers.       
# Input
# The first line contains an integer t, the number of test cases.
# Each test case consists of two integers x and n, the number of planes and the number of passengers respectively.
# Output            
# For each test case, print the number of additional planes needed to carry all the passengers.
# Constraints
# 1 ≤ t ≤ 1000
# 1 ≤ x ≤ 1000
# 1 ≤ n ≤ 10^6
# Example
# Input
# 3
# 2 200
# 3 250
# 4 300
# Output
# 0
# 1
# 2
# Explanation
# In the first test case, 2 planes can carry 200 passengers, so no additional planes are needed.
# In the second test case, 3 planes can carry 300 passengers, but there are 250 passengers, so 1 additional plane is needed.
# In the third test case, 4 planes can carry 400 passengers, but there are 300 passengers, so 2 additional planes are needed.   



# ==================================================================================


# Soltion 



import math
t = int(input())
for i in range(t):
    x,n = map(int , input().split())
    need_plane =  math.ceil(n / 100)
    if need_plane >= x:
         print(need_plane - x)
    else:
        print(0)


# 2nd method 

import math

t = int(input())
for i in range(t):
    x, n = map(int, input().split())
    needed_planes = math.ceil(n / 100)
    print(max(0, needed_planes - x))

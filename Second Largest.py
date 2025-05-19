# =================== Second Largest ===================
#
# Three numbers A, B and C are the inputs. Write a program to find second largest among them.
#
# Input Format
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.
#
# Output Format
# For each test case, display the second largest among A, B and C, in a new line.
#
# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ A,B,C ≤ 1000000
#
# Sample Input:
# 3 
# 120 11 400
# 10213 312 10
# 10 3 450
#
# Sample Output:
# 120
# 312
# 10

# Solution


t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    s=sorted(a)
    print(s[1])
    
    

# method 2
    
def solve():
    a, b, c = map(int, input().split())

    if (a < b and a > c) or (a > b and a < c):
        print(a)
    elif (b < a and b > c) or (b > a and b < c):
        print(b)
    else:
        print(c)

t = int(input())
for _ in range(t):
    solve()    


    # -------------------------------------------------------------------------

    # Problem Link: "https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW017?tab=statement"


# --------------------------------------------------------------------------------------------------------







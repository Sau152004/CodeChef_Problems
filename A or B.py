# =================== A or B ===================
#
# There are two problems in a contest.
# Problem A is worth 500 points at the start of the contest.
# Problem B is worth 1000 points at the start of the contest.
# Once the contest starts, after each minute:
#   - Maximum points of Problem A reduce by 2 points.
#   - Maximum points of Problem B reduce by 4 points.
# Chef requires X minutes to solve Problem A and Y minutes to solve Problem B.
# Find the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.
#
# Input Format:
# First line will contain T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers X and Y.
#
# Output Format:
# For each test case, output in a single line, the maximum number of points Chef can score if he optimally decides the order.
#
# Constraints:
# 1 ≤ T ≤ 1000
# 1 ≤ X, Y ≤ 100
#
# Sample Input:
# 4
# 10 20
# 8 40
# 15 15
# 20 10
#
# Sample Output:
# 1360
# 1292
# 1380
# 1400

# =========================================================================================

# Solution

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    order1 = ((500 -a*2) + (1000-(a+b)*4))
    order2 = ((1000 - b*4) + (500 - (a+b)*2))
    print(max(order1,order2))
    

    # --------------------------------------------------------------------------------------------

    # Problem Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AORB?tab=statement


    # ---------------------------------------------------------------------------------------------
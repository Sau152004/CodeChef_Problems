

# ========================== Cup Finals ==========================

#
# It is the World Cup Finals. Chef only finds a match interesting if the skill difference of the competing teams is less than or equal to D.
#
# Given that the skills of the teams competing in the final are X and Y respectively, determine whether Chef will find the game interesting or not.
#
# Input Format:
# The first line of input will contain a single integer T, denoting the number of testcases. The description of T testcases follows.
# Each testcase consists of a single line of input containing three space-separated integers X, Y, and D — the skill levels of the teams and the maximum skill difference.
#
# Output Format:
# For each testcase, output "YES" if Chef will find the game interesting, else output "NO" (without the quotes). The checker is case-insensitive, so "YeS" and "nO" etc. are also acceptable.
#
# Constraints:
# 1 ≤ T ≤ 2000
# 1 ≤ X, Y ≤ 100
# 0 ≤ D ≤ 100
#
# Sample Input:
# 3
# 5 3 4
# 5 3 1
# 5 5 0
#
# Sample Output:
# YES
# NO
# YES
#
# Explanation:
# Test case 1: The skill difference between the teams is 2, which is less than the maximum allowed difference of 4.
# Test case 2: The skill difference between the teams is 2, which is more than the maximum allowed difference of 1.
# filepath: c:\Users\DELL\OneDrive\Desktop\CodeChef_ Problems\Cup Finals.py

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# solution 

t = int(input())
for i in range(t):
    x,y,d = map(int,input().split())
    diff = abs(x - y)
    if diff <= d:
        print("YES")
    else:
        print("NO")

# ========================================================================================================

# cpp code  


#include <iostream>
#include <cstdlib> // for abs()

# using namespace std;

# int main() {
#   int t;
#   cin >> t; // Read the number of test cases

#   while (t--) {
#     int x, y, d;
#     cin >> x >> y >> d; // Read the input values

#     int diff = abs(x - y); // Calculate the absolute difference

#     if (diff <= d) {
#       cout << "YES" << endl; // Output "YES" if the condition is met
#     } else {
#       cout << "NO" << endl; // Output "NO" otherwise
#     }
#   }

#   return 0;
# }

# ----------------------------------------------------------------------------------------------------------

# problem link : "https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CRICUP?tab=statement"


# ----------------------------------------------------------------------------------------------------------------
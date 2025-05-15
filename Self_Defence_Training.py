# # =================== Self Defence Training ===================

# # Problem
# After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start the 37th Chamber of Shaolin. The aim this time is to equip women with Shaolin self-defence techniques.

# The only condition for a woman to be eligible for the special training is that she must be between 10 and 60 years of age, inclusive of both 10 and 60.

# Given the ages of N women in his village, help San Te determine how many of them are eligible for the special training.

# Input Format:
# The first line of input contains a single integer T, denoting the number of test cases.
# For each test case:
# The first line contains a single integer N, the number of women.
# The second line contains N space-separated integers A₁, A₂, ..., Aₙ, representing the ages of the women.
# Output Format:
# For each test case, output a single line containing the number of women eligible for self-defence training.


# Sample Input:

# 3
# 3
# 15 23 65
# 3
# 15 62 16
# 2
# 35 9
# Sample Output:

# 2
# 2
# 1
# Explanation:
# Test Case 1:
# Out of the women, only the 1st and 2nd women are eligible for the training because their ages lie in the interval ([10, 60]). Hence, the answer is 2.

# Test Case 2:
# Only the 1st and 3rd women are eligible for the training because their ages lie in the interval ([10, 60]). Hence, the answer is 2.

# Test Case 3:
# Only the 1st woman with age 35 is eligible for the training. Hence, the answer is 1.

# This is the structured problem statement for your code.


# =============================================================================

# solution

# Python solution


t =  int(input())
for i in range(t):
    n = int(input())
    age = list(map(int,input().split()))   # age_of_women
    count = 0
    for x in age:
        if 10 <= x <= 60:
            count +=1
    print(count)
        


#  CPP solution
# 
# #include <iostream>
#include <vector>

# using namespace std;

# int main() {
#   int t;
#   cin >> t;

#   while (t--) {
#     int n;
#     cin >> n;

#     vector<int> ages(n); // Use a vector to store the ages
#     for (int i = 0; i < n; ++i) {
#       cin >> ages[i];
#     }

#     int count = 0;
#     for (int age : ages) { // Use a range-based for loop (cleaner)
#       if (age >= 10 && age <= 60) {
#         count++;
#       }
#     }

#     cout << count << endl;
#   }

#   return 0;
# }       


# =============================================================

# Prpblem link:  https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SELFDEF?tab=statement
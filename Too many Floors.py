
# ================================= Too many Floors ===============================================

# # Problem Statement
#
# Chef and Chefina are residing in a hotel.
#
# There are 10 floors in the hotel and each floor consists of 10 rooms.
#
# Floor 1 consists of room numbers 1 to 10.
# Floor 2 consists of room numbers 11 to 20.
# …
# Floor i consists of room numbers 10⋅(i−1)+1 to 10⋅i.
#
# You know that Chef's room number is X while Chefina's Room number is Y.
# If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.
#
# Input Format

# First line will contain T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers X, Y, the room numbers of Chef and Chefina respectively.
#
# Output Format
# For each test case, output the number of floors Chef needs to travel to reach Chefina's room.
#
# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ X, Y ≤ 100
# X ≠ Y
#
# Sample Input:
# 4
# 1 100
# 42 50
# 53 30
# 81 80
#
# Sample Output:
# 9
# 0
# 3
# 1
#
# Explanation:
# Test Case 1: Room 1 is on 1st floor and Room 100 is on 10th floor, Chef needs to climb 9 floors to reach Chefina's Room.
# Test Case 2: Room 42 is on 5th floor and Room 50 is also on 5th floor, Chef does not need to climb any floor.
# Test Case 3: Room 53 is on 6th floor and Room 30 is on 3rd floor, Chef needs to go down 3 floors to reach Chefina's Room.
# Test Case 4: Room 81 is on 9th floor and Room 80 is on 8th floor, Chef needs to go down 1 floor to reach Chefina's Room.


# ================ Solution ==========================

# Python solution

t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    floor = abs(((x-1)//10) - ((y-1)//10))
    print(floor)


# C++ solution

# #include <iostream>
# #include <cmath>

# int main() {
#     int t;
#     std::cin >> t;
#     while (t--) {
#         int x, y;
#         std::cin >> x >> y;
#         int floor = std::abs(((x - 1) / 10) - ((y - 1) / 10));
#         std::cout << floor << std::endl;
#     }
#     return 0;
# }



# -----------------------------------------------------------

# Problem Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOORS?tab=statement

# ----------------------------------------------------------------
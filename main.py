from itertools import combinations

def solved(combs, points):
    for comb in combs:
        answer = [1 for each in range(len(points))]

        for num in comb:
            for i in range(len(points)):
                if num >= points[i][0] and num <= points[i][1]:
                    answer[i] = 0 #num pops ballon[i] so mark it popped (0)
        if sum(answer) == 0: #this combination pops all balloons
            print(comb)
            return True

    return False


def findMinArrowShots(points):
    #find the complete range of numbers as the min/max of all the ballons
    allNumbers = []
    for ballon in points:
        for num in range(ballon[0], ballon[1] + 1):
            allNumbers.append(num)
    allNumbers = set(allNumbers) #remove duplicates

    for i in range(1, len(allNumbers) + 1):
        combs = combinations(allNumbers, i)
        #do any of these combinations solve the puzzle
        if(solved(combs, points)):
            return i

    return 0 #no solution

#Example 1:
#Input: 
points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))
#Output: 2
#Explanation: The balloons can be burst by 2 arrows:
#- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
#- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

# Example 2:
# Input: 
points = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

# Example 3:
# Input: 
points = [[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points))
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
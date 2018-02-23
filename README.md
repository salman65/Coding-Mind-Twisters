# Coding-Mind-Twisters

Includes various problems which I am going to solve.

1- Tom & Jerry in a Maze: Involves finding shortest path in a maze. Solved it using Queues and Backtracking.

2- Minimum Lazers to Hit Multiple Statues in Cartesian Grid: To find the minimum number of lazers to shoot all statues. Statues lying in a straight line can be shot down with a single lazer. Solved it using cross product property as cross product of points on a straight line is 0. 

3- Quasi Constant: Finding the largest subsequence of an array with difference between its minimum and maximum values less than or equal to 1. Solved it by sorting the array first and then finding the sequence for each number from initial index till difference increases 1. It gives the lengths of all sequences with difference less than 1. Finding the max of these values gives the required answer.

4- Largest Slice Product: Finding the maximum product of the numbers of a slice of an array of Rational Numbers. Solved it by storing all the products of each number with its successive numbers in a dictionary (until a 0 is encountered as product with 0 is 0 for all successive numbers). For eg, for an array: [2, -1, 3, -2, 0, 4] (array could include decimals too, used integers for simplicities sake) I would first make a dictionary like:
{
  1: [2, -2, -6, 12],
  2: [-1, -3, 6],
  3: [3, -6],
  4: [0],
  5: [4]
}
After this find the maximum number among all dictionary arrays, thus solving the puzzle.

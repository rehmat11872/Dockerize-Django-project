'''Given a matrix m of positive integers where the integers on every row are sorted in an ascending order, return the minimum integer that exists in all rows. If no such integer is found, return -1.
Example:
Input: m = [[2,3,4,5,6], [2,5,6,9,12], [4,6,8,10,12], [2,4,6,8,18
Output: 6



Constraints:
nx == m[i].length
• mx == m.length
1 <= mx, nx <= 500
• 1 <= m[i][j] <= 104
• m[i] is sorted in strictly increasing order.


Code
def solution(m) > int:
     res 
     return -1

if __name__=="__main__"
   mtx = [[int(val) for val in pair.split()] for pair in output().strip().split(',')]
   print(solution(mtx))


We want to see how you plan your solution, clearly describing the thought process for solving the problem. You can iteratively update the initial plan through the solution.
explaining your thought process for solving the problem Mark this section with "#Plan". You can add multi-line comments
you work • Code Comments:
• When starting a new code section or fixing a bug, add a comment explan
your thought process. Avoid skipping steps and provide more detail when in doubt. • When modifying existing code after execution, document the new approach in a comment above the edited code block. Explain the reasoning behind the
changes and how the new approach aims to improve or fix the previous
solution.
• Test Cases:
• Devise test cases covering base, average, and edge cases to verify code correctness.
• Use the "Add custom test case" feature to test your code.
• Running Tests: Use the "Run Tests" button to test your code. If tests don't pass 100%, your code is not completely correct. Keep improving the code for correctness
Test cave
and readability. • Commit Message: Provide a good commit message on submission, as it's considered in the evaluation.

'''




def solution(m) -> int:
    # Initialize a dictionary to store counts
    count_map = {}
    rows = len(m)
    
    # Populate the count_map with elements from the first row
    for num in m[0]:
        count_map[num] = 1
    
    # Update the count_map for the remaining rows
    for i in range(1, rows):
        row_set = set(m[i])  # Convert current row to set for faster lookup
        for num in count_map:
            if num in row_set:
                count_map[num] += 1
    
    # Find the minimum element that exists in all rows
    result = -1
    for num, count in count_map.items():
        if count == rows:
            if result == -1 or num < result:
                result = num
    
    return result

if __name__ == "__main__":
    mtx = [[int(val) for val in pair.split()] for pair in input().strip().split(',')]
    # mtx = [
    #     [2, 3, 4, 5, 6],
    #     [2, 5, 6, 9, 12],
    #     [4, 6, 8, 10, 12],
    #     [2, 4, 6, 8, 18]
    # ]
    print(solution(mtx))


'''
Plan

    Problem Understanding:
        The matrix m has rows sorted in strictly increasing order.
        We need to find the smallest integer that appears in all rows.
        If no such number exists, return -1.

    Approach:
        Since the rows are sorted, a hash map (or a counter) can be used to track the frequency of each element across all rows.
        We need to find the smallest integer that has a count equal to the number of rows (mx).

    Steps:
        Initialize a dictionary to store element counts.
        For each row in the matrix, add its elements to the dictionary.
        After processing all rows, check for elements that appear in all rows (count == mx), and return the smallest one.
        If no element satisfies this condition, return -1.

    Optimization Thoughts:
        Given the constraints of 1 <= mx, nx <= 500 and 1 <= m[i][j] <= 10^4, we should ensure that the approach is efficient. A dictionary-based count solution should be feasible since we only need to iterate over each row and element.

    Edge Case Considerations:
        Single row matrix should directly return the smallest element from that row.
        Large matrices need an efficient scanning approach.
        No common element across rows should result in -1.
'''
"""
Created on Tue Jan 25 17:35:34 2022

@author: Ethan
"""


def sum_threshold(thresh, *lst):
    """Defines a threshold value, then sums remaining values up to the threshold

    Passed an integer that it sets as a threshold value and a list of integers
    that it unpacks using the arbitrary argument technique.  Then uses a for
    loop to iterate through the list and add the integers together, breaking
    once the total value is less than or equal to the threshold, and returns the
    total"""

    total = 0
    for num in lst:
        if (total + num) <= thresh:
            total += num
        else:
            break
    return total


lst = [7, 2, 12, 9, 15, 4, 11, 5]
print('The sum of the elemenst, left to right, without exceeding the')
print('threshold 40 is ', sum_threshold(40, *lst))
print('The same but with a threshold of 70: ', sum_threshold(70, *lst))
print('With an empty list of numbers: ', sum_threshold(50))


# sm = 0
# for n in nums:
#     if sm + n > threshold:
#         break
#     sm += n
# return sm    
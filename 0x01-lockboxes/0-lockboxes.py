#!/usr/bin/python3

"""
Challenge: A set of locked boxes is laid out before you, 
numbered sequentially from 0 to n - 1. 
It's possible that these boxes hold keys to other boxes. 
Your objective is to devise a method to ascertain whether 
it's feasible to unlock all the boxes.
"""


def canUnlockAll(boxes):
    """
    A function that employs a boolean value to determine whether
      the type and length of a list warrant the 
      activation of two separate iterations: 
            one to navigate through the list, and the other to verify 
            whether a given key matches an index for the purpose of unlocking.
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True

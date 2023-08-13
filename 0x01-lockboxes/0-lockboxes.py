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
    n = len(boxes)
    if n == 0:
        return False

    unlocked_boxes = [False] * n
    unlocked_boxes[0] = True

    keys_stack = [0]

    while keys_stack:
        current_box = keys_stack.pop()

        for key in boxes[current_box]:
            if key < n and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys_stack.append(key)

    return all(unlocked_boxes)

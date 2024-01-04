#!/usr/bin/python3
"""
Create a 'queue' for boxes to open, starting with box 0.
"""


def canUnlockAll(boxes):
    # Create a set to track boxes already open
    opened = set()
    opened.add(0)

    # Create a queue for boxes to open
    queue = [0]

    # Continue as long as there are boxes in the queue.
    while queue:
        box = queue.pop(0)

        for key in boxes[box]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                queue.append(key)

    return len(opened) == len(boxes)

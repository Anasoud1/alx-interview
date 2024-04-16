#!/usr/bin/python3
def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened.'''
    obj = {0: 'open'}
    for i in range(1, len(boxes)):
        obj[i] = 'close'
    for k, v in obj.items():
        if v == 'open':
            for i in boxes[k]:
                obj[i] = 'open'
                if k > i:
                    for j in boxes[i]:
                        obj[j] = 'open'
    res = all(value == 'open' for value in obj.values())
    return res

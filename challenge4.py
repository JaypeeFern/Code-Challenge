def fitsInOneBox(boxes):
    boxes.sort(key=lambda box: max(box.values()))
    for i in range(len(boxes) - 1):
        current_box = boxes[i]
        next_box = boxes [i+1]
        if current_box['l'] >= next_box['l'] or current_box['w'] >= next_box['w'] or current_box['h'] >= next_box['h']:
            return False
    return True

boxes = [
    {'l': 1, 'w': 1, 'h': 1},
    {'l': 2, 'w': 2, 'h': 2},
    {'l': 3, 'w': 1, 'h': 3}
]

print(fitsInOneBox(boxes))
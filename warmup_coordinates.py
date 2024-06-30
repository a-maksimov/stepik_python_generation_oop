import sys

coordinates = [eval(line.strip()) for line in sys.stdin]
for coordinate in coordinates:
    x, y = coordinate
    print(90 - abs(x) > 0 and 180 - abs(y) > 0)
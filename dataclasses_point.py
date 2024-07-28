from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False)

    def __post_init__(self):
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        else:
            self.quadrant = 0

    def symmetric_x(self):
        return Point(x=self.x, y=-self.y)

    def symmetric_y(self):
        return Point(x=-self.x, y=self.y)


point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)

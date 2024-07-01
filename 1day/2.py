class PointOffset:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DrawingPoints:
    points = []

    def add(self, point: PointOffset):
        self.points.append(point)

    def drawing(self):
        for point in self.points:
            print(f"{point.x}, {point.y} 에 버튼 찍힘")


a = xyManager()
a.add(xy_info(1, 2))
a.add(xy_info(2, 3))
a.add(xy_info(5, 5))
a.add(xy_info(7, 1))
a.draw_button()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self ,x1, y1):
        self.x = x1
        self.y = y1
    
    def dist(self, secpoints):
        cx = secpoints.x - self.x
        cy = secpoints.y - self.y
        ans = (cx**2 + cy**2)**0.5
        print(ans)
points1 = Point(10, 5)
points1.show()
points2 = Point(3, 4)
points2.show()
points1.move(7, 7)
points1.show()
points1.dist(points2)
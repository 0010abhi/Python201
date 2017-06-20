import math
class Distance:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def calculate_distance(point1,point2):
        distance=math.pow(point2.y-point1.y,2)+math.pow(point2.x-point1.x,2)
        return math.pow(distance,0.5)

if __name__ == '__main__':
    x1=input("enter first point x-cordinate")
    y1 = input("enter first point y-cordinate")
    x2 = input("enter second point x-cordinate")
    y2 = input("enter first point y-cordinate")
point1=Distance(x1,y1)
point2=Distance(x2,y2)
print Distance.calculate_distance(point1,point2)
class Box:
 def area(self):
     #replaced width and height with self.width and self.height
    return self.width * self.height
 def __init__(self, width, height):
    self.width = width
    self.height = height
# Create an instance of Box.
x = Box(10, 2)
# Print area.
print(x.area())
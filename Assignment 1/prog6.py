# Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
# of the points in your 3-D space and store them in a list. The final output is a list with each
# consisting of a point and its nearest neighbour. [Hint: Use distance between two points
# formula]
pointx = []
pointy = []
pointz = []
points = [pointx, pointy, pointz]

for i in range(10):
    x = int(input("ENTER THE X COORDINATE : "))
    y = int(input("ENTER THE Y COORDINATE : "))
    z = int(input("ENTER THE Z COORDINATE : "))
    print("\n")
    pointx.append(x)
    pointy.append(y)
    pointz.append(z)

shortest_distance = float('inf')
shortest_points = (None, None)

for i in range(10):
    for j in range(i + 1, 10):
        distance = ((points[0][i] - points[0][j]) ** 2 +
                     (points[1][i] - points[1][j]) ** 2 +
                     (points[2][i] - points[2][j]) ** 2) ** 0.5
        
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_points = (i, j)

if shortest_points[0] is not None:
    print(f"The shortest distance is {shortest_distance:.2f} between points {shortest_points[0]} and {shortest_points[1]}")
    print(f"Point {shortest_points[0]}: ({points[0][shortest_points[0]]}, {points[1][shortest_points[0]]}, {points[2][shortest_points[0]]})")
    print(f"Point {shortest_points[1]}: ({points[0][shortest_points[1]]}, {points[1][shortest_points[1]]}, {points[2][shortest_points[1]]})")
else:
    print("No points were provided.")
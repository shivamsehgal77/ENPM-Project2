import math

# Original triangle coordinates
points_triangle = [(460, 25), (460, 225), (510, 125)]

# Compute the length of each side of the original triangle
a = math.sqrt((points_triangle[1][0] - points_triangle[0][0])**2 + (points_triangle[1][1] - points_triangle[0][1])**2)
b = math.sqrt((points_triangle[2][0] - points_triangle[1][0])**2 + (points_triangle[2][1] - points_triangle[1][1])**2)
c = math.sqrt((points_triangle[0][0] - points_triangle[2][0])**2 + (points_triangle[0][1] - points_triangle[2][1])**2)

# Compute the coordinates of the midpoints of each side of the original triangle
midpoints = [((points_triangle[i][0] + points_triangle[(i+1)%3][0])/2, (points_triangle[i][1] + points_triangle[(i+1)%3][1])/2) for i in range(3)]

# Compute the distances between each vertex of the original triangle and the midpoint of the opposite side
d = [math.sqrt((points_triangle[i][0] - midpoints[(i+2)%3][0])**2 + (points_triangle[i][1] - midpoints[(i+2)%3][1])**2) for i in range(3)]

# Add 5mm to each distance
d_new = [d[i] + 5 for i in range(3)]

# Compute the coordinates of the vertices of the new triangle
points_new = []
for i in range(3):
    j = (i+1) % 3
    # Compute the angle between the line connecting the midpoint of the opposite side and the vertex of the original triangle
    # and the line connecting the midpoint of the opposite side and the corresponding vertex of the new triangle
    angle = math.atan2(points_triangle[i][1] - midpoints[j][1], points_triangle[i][0] - midpoints[j][0])
    # Compute the coordinates of the corresponding vertex of the new triangle
    x_new = midpoints[j][0] + d_new[i] * math.cos(angle)
    y_new = midpoints[j][1] + d_new[i] * math.sin(angle)
    points_new.append((int(x_new), int(y_new)))
    
print(points_new)
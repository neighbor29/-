import math


def estimate_area(cx, cy, r, d1, d2, grid_size):
    x_min, x_max = cx - r - d1, cx + r + d1
    y_min, y_max = cy - r - d1, cy + r + d1
    delta = (x_max - x_min) / grid_size
    points_in_diamonds = 0
    total_points = 0
    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            x = x_min + i * delta
            y = y_min + j * delta
            if (x - cx)**2 + (y - cy)**2 <= r**2:
                total_points += 1
                if abs(x - cx) + abs(y - cy) <= d1/2 and abs(x - cx) + abs(y - cy) > d2/2:
                    points_in_diamonds += 1
    total_area = math.pi * r**2
    area_per_point = total_area / total_points
    area_of_phi = points_in_diamonds * area_per_point
    return area_of_phi


cx, cy, r, d1, d2 = map(int, input().split())
area = estimate_area(cx, cy, r, d1, d2, grid_size=1000)
print(f"{area:.6f}")
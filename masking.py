import numpy as np

#__pixel data
image = np.random.randint(0, 256, (5, 5))

# dark pixel filter
dark_mask = image < 50
dark_pixels = image[dark_mask]

print(f"dark pixel number: {len(dark_pixels)}")
print(f"dark pixel value: {dark_pixels}")

# height
points = np.array([
[1.0, 2.0, 0.5],
[3.0, 1.0, 5.2],
[2.0, 4.0, 0.3],
[5.0, 3.0, 8.1],
])

high_points = points[points[:, 2] > 2.0]
print("height :")
print(high_points)
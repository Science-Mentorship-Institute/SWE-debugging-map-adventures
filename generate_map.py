def generate_map_file(size, num_obstacles):
    # Create an empty map grid
    map_grid = [['.' for _ in range(size)] for _ in range(size)]

    # Place obstacles randomly
    import random
    for _ in range(num_obstacles):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        map_grid[y][x] = 'X'

    # Write map grid to a text file
    with open('map.txt', 'w') as file:
        for row in map_grid:
            file.write(' '.join(row) + '\n')

# Get user input for map size
size = int(input("Enter size of the map: "))
num_obstacles = int(input("Enter number of obstacles: "))

# Generate map file
generate_map_file(size, num_obstacles)
print("Map file generated successfully!")

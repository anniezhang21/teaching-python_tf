def triangle():
    # Initializing 2 variables
    height = int(input("Desired triangle height (integers only): "))
    stars = '*'

    # Beginning the loop (one loop for each row)
    for _ in range(height):
        # Print the stars for that row
        print(stars)

        # Change variable for the next row
        stars += '*'

def isosceles_triangle(height):
    # Initializing 4 variables
    num_spaces = height - 1
    stars = '*'
    spaces = ' ' * num_spaces

    # Beginning the outer loop (one loop for each row)
    for _ in range(height):
        # Define the number of spaces before and after the stars
        # for _ in range(num_spaces):
        #     spaces += ' '

        # Print the spaces and stars for that row
        print(spaces, stars, spaces)

        # Change variables for the next row
        stars += '**'
        num_spaces -= 1
        spaces = ' ' * num_spaces


def pascals_triangle(height):
    def pascals_helper(triangle, row_num):
        if height - row_num + 1 == 0:
            return triangle

        new_row = [1]

        for i in range(len(triangle[row_num]) - 1):
            new_num = triangle[row_num][i] + triangle[row_num][i + 1]
            new_row.append(new_num)
        new_row.append(1)

        triangle.append(new_row)
        return pascals_helper(triangle, row_num + 1)

    return pascals_helper([[1]], 0)

def print_pascals(triangle):
    # Initializing 4 variables
    height = len(triangle)
    num_spaces = height - 1
    row = 1
    for row in triangle:
        for _ in range(num_spaces):
            print(' ', end='')
        for num in row:
            print(str(num) + ' ', end='')
        for _ in range(num_spaces):
            print(' ', end='')
        print()
        num_spaces -= 1

print("Use triangle() or isosceles_triangle() or pascals_triangle() with print_pascals()")
isosceles_triangle(10)

# Let's print a rectangle of stars.
def rectangle(height, width):
    for y in range(height):
        for x in range(width):
            print('*', end='')
        print()

rectangle(2, 4)

# print_pascals(pascals_triangle(3))
# print_pascals(pascals_triangle(4))
# print_pascals(pascals_triangle(7))

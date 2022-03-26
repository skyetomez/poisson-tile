import itertools

EDGE = 1000


num_squares = 3
sub_squares = num_squares * num_squares
number_lines = num_squares - 1
number_coord = number_lines * 2

points = []

# Get X centers

def centers(edge, num_squares):
    points = num_squares * 2 + 1
    inc = edge / (num_squares * 2) 
    centers = []
    
    for coord in range(points):
        if coord % 2 == 1:
            delta = inc * coord 
            centers.append(delta)
                      
            
    return centers

x_centers = centers(EDGE, num_squares)


for subsets in itertools.product(x_centers, x_centers):
    points.append(subsets)
    print(subsets)

print(points)

def translate_squares(num_squares, offset):
    translations = []
    for x_offset in range(num_squares):
        for y_offset in range(num_squares):
            translations += [(x_offset * offset,y_offset * offset)]
    return translations
        

print(translate_squares(num_squares, 333))
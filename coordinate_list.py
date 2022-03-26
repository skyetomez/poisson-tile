

LENGTH = 1000
WIDTH = 1000


num_squares = 2
sub_squares = num_squares * num_squares
number_lines = num_squares - 1
number_coord = number_lines * 2


hor_array = [] 
vert_array = []


half_length = len(hor_array)//num_squares

x_delta = LENGTH / num_squares
y_delta = WIDTH / num_squares

# Y coordinates
# counter = 0
# for x in range(len(array)):
#     if counter % 2 == 0:
#         array[x] = (0,0)
#         counter += 1
        
#     if counter % 2 == 1:
#         array[x] = (0,LENGTH)
#         counter += 1


# X coordinates
counter = 0
add_x = 0
add_x = add_x + x_delta
for x in range(number_coord):
    if counter  == 0:
        hor_array += [(add_x,0)]
        print("pt1:",hor_array)
        counter += 1
    elif counter  == 1:
        hor_array += [(add_x, LENGTH)]
        print("pt2:",hor_array)
        counter += 1
    else:   
        add_x = add_x + x_delta
        hor_array += [(add_x,0)]
        print("pt3:",hor_array)
        counter = 1


#  Y coordinates
counter = 0
add_y = 0
add_y = add_y + y_delta
for y in range(number_coord):

     if counter  == 0:
         vert_array+= [(0,add_y)]
         print("pt1:",vert_array)
         counter += 1
     elif counter  == 1:
         vert_array += [(WIDTH, add_y)]
         print("pt2:",vert_array)
         counter += 1
     else:
         add_y = add_y + y_delta
         vert_array += [(0,add_y)]
         print("delta:",add_y)
         counter = 1

print("Horizonal", hor_array)
print("Vertical", vert_array)      
    


# for x_coor in range(len(array)):
#     if x_coor >= len(array)/num_squares and x_coor % 2 == 0: 
#         array[x_coor] += x_delta 

# for y_coor in range(len(array)):
#      if y_coor % 2 == 1: 
#          array[y_coor] += y_delta
# for y_coor in range(len(array)):
#      if y_coor % 4 == 3: 
#          array[y_coor] = LENGTH

                
            
            

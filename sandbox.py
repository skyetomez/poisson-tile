import itertools 
import pygame, sys, time, random
from pygame.locals import *



SCREEN_HEIGHT = 2000
SCREEN_WIDTH = 2000

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GREY = (211,211,211)


############## MATH STUFF

### Variables
point_size = (5,5)
num_squares = 7

## Compute subsquares
sub_squares = num_squares * num_squares
tolerance = 1 # Something positive
prob = 1  # tolerance / sub_squares

# calculate offset of squares
offset = SCREEN_HEIGHT / num_squares


# num of coordinates
number_lines = (num_squares - 1) * 2
number_coord = number_lines 

# Generate 

hor_array = [(0,0) for row in range(number_coord)] 
vert_array = [(0,0) for row in range(number_coord)] 


x_delta = SCREEN_WIDTH / num_squares
y_delta = SCREEN_HEIGHT / num_squares


# horizontal 


# Function to make the horiztional lines

def hor_lines(x_delta, hor_array):
    counter = 0
    add_x = 0
    add_x = add_x + x_delta
    for x in range(len(hor_array)):
        if counter  == 0:
            hor_array[x] = (add_x,0)
            print("pt1:",hor_array)
            counter += 1
        elif counter  == 1:
            hor_array[x] = (add_x, SCREEN_WIDTH)
            print("pt2:",hor_array)
            counter += 1
        else:   
            add_x = add_x + x_delta
            hor_array[x] = (add_x,0)
            print("pt3:",hor_array)
            counter = 1
    return hor_array

# Function to make the vertical lines

def vert_lines(y_delta, vert_array):
    counter = 0
    add_y = 0
    add_y = add_y + y_delta


    for y in range(len(vert_array)):
        
        if counter  == 0:
            vert_array[y] = (0,add_y)
            print("pt1:",vert_array)
            counter += 1
        elif counter  == 1:
            vert_array[y] = (SCREEN_HEIGHT, add_y)
            print("pt2:",vert_array)
            counter += 1
        else:
            add_y = add_y + y_delta
            vert_array[y] = (0,add_y)
            print("delta:",add_y)
            counter = 1
    return vert_array

hor_array = hor_lines(x_delta, hor_array)
vert_array = vert_lines(y_delta, vert_array)

print("horizontal", hor_array)
print("vertical", vert_array)



size = [SCREEN_WIDTH, SCREEN_HEIGHT]

class point():
    def __init__(self, color, offset, centers, prob):
        self.point_surface = pygame.Surface(point_size)
        self.color = color
        self.point_surface.fill(color)
        self.prob = prob
        self.offset = offset
        self.center = centers
        self.point_rect = self.point_surface.get_rect( center =self.center) #(self.x,self.y)
        
    
   # prob of appearing as a function of the probability  
    def appear_prob(self):
        rand_num = random.random()
        
        if  rand_num > self.prob:
            self.point_surface.fill(BLACK)
            self.is_red = False
          # print(self.is_red)
        if rand_num < self.prob:
            self.point_surface.fill(self.color)
            self.is_red = True
           # print(self.is_red)
    
    # change the coordinates of the square randomly in within its offset.  
    def coord_prob(self):
        rand_x = random.random()
        rand_y = random.random()
        
        self.point_rect.x = abs((size[0]  - self.point_surface.get_width()) - (size[0] * rand_x)) % (self.offset - self.point_surface.get_width())  # offset defines square
        self.point_rect.y = abs((size[1] - self.point_surface.get_height()) - (size[1] * rand_y)) % (self.offset - self.point_surface.get_height())
        

    # makes it bounce and flicker
    def update(self):
        self.coord_prob()
        self.appear_prob()

    
  
def draw_grid(hor_array, vert_array): 
    length = len(hor_array) - 1
    length = int(length) 

    for i in range(len(hor_array)):
        if i < length and i % 2 == 0:
            pygame.draw.line(screen, GREY, hor_array[i], hor_array[i+1], 3)
        
    for i in range(len(vert_array)):
        if i < length and i % 2 == 0:
            pygame.draw.line(screen, GREY, vert_array[i], vert_array[i+1], 3)   
    
def centers(edge, num_squares):
    points = num_squares * 2 + 1
    inc = edge / (num_squares * 2) 
    centers = []
    
    for coord in range(points):
        if coord % 2 == 1:
            delta = inc * coord 
            centers.append(delta)
                      
            
    return centers

x_centers = centers(SCREEN_HEIGHT, num_squares)

centers = []


for subsets in itertools.product(x_centers, x_centers):
    centers.append(subsets)

print(centers)        
        
def translate_squares(num_squares, offset):
    translations = []
    for x_offset in range(num_squares):
        for y_offset in range(num_squares):
            translations += [(x_offset * offset,y_offset * offset)]
    return translations
        
translations = translate_squares(num_squares, offset)

print(translate_squares(num_squares, offset))

   
            
# display stuff
screen = pygame.display.set_mode(size = size)
screen.fill('BLACK')


ball_box = []
for i in centers:
    ball_box.append(point(BLUE, offset, i, prob))
    

# Game loop
counter = 0 

running = True

clock = pygame.time.Clock()


pygame.init()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    

    
    screen.fill('BLACK')
    counter+= 1
    index = 0
    if counter % 15 == 0:
        for i in range(sub_squares):
            ball_box[i].update()

        
            ball_box[i].point_rect = ball_box[i].point_rect.move(translations[index])
            index += 1

    for i in range(sub_squares):
        screen.blit(ball_box[i].point_surface, ball_box[i].point_rect)

    # Lines
    
    draw_grid(hor_array, vert_array)
     
    
    pygame.display.flip()
    
    
    clock.tick(60)

    
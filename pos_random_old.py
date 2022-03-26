from itertools import count
from re import S
from pandas import array
import pygame, sys, time, random
from pygame.locals import *
from rsa import verify



SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GREY = (211,211,211)


##### MATH STUFF

point_size = (100,100)

num_squares = 2
sub_squares = num_squares * num_squares

tolerance = 1 # Something positive

prob =  tolerance / sub_squares

## Compute subsquares

num_lines = num_squares * 2 


# calculate coordinates

x_axis = SCREEN_WIDTH / num_squares
y_axis = SCREEN_WIDTH / num_squares


# num of coordinates

number_lines = (num_squares - 1) * 2
number_coord = number_lines 

# subsquares to tuple length

coordinate_list = [0 for row in range(number_coord)] 

half_length = len(coordinate_list)//num_squares

x_delta = SCREEN_WIDTH/num_squares
y_delta = SCREEN_HEIGHT/num_squares

# pre reqs for below

hor_array = [(0,0) for row in range(number_coord)] 
vert_array = [(0,0) for row in range(number_coord)] 


x_delta = SCREEN_WIDTH / num_squares
y_delta = SCREEN_HEIGHT / num_squares



# X coordinates

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

# Y coordinates

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
    def __init__(self, color):
        self.point_surface = pygame.Surface(point_size)
        self.color = color
        self.point_surface.fill(color)
        self.is_red = True
        self.x = size[0]/2
        self.y = size[1]/2
        self.point_rect = self.point_surface.get_rect(center = (self.x,self.y))

    
    
    def appear_prob(self, prob):
        rand_num = random.random()
        
        if  rand_num > prob:
            self.point_surface.fill(BLACK)
            self.is_red = False
          # print(self.is_red)
        if rand_num < prob:
            self.point_surface.fill(self.color)
            self.is_red = True
           # print(self.is_red)
    
    # change the coordinates of the square? 
    def coord_prob(self):
        rand_x = random.random()
        rand_y = random.random()
        self.point_rect.move
        
        self.point_rect.x = abs((size[0]  - self.point_surface.get_width()) - (size[0] * rand_x))
        self.point_rect.y = abs((size[1] - self.point_surface.get_height()) - (size[1] * rand_y))

    
  
def draw_grid(hor_array, vert_array): 
    length = len(hor_array) - 1
    length = int(length) 

    for i in range(len(hor_array)):
        if i < length and i % 2 == 0:
            pygame.draw.line(screen, GREY, hor_array[i], hor_array[i+1], 3)
        
    for i in range(len(vert_array)):
        if i < length and i % 2 == 0:
            pygame.draw.line(screen, GREY, vert_array[i], vert_array[i+1], 3)   
    
            
# display stuff
screen = pygame.display.set_mode(size = size)
screen.fill('BLACK')


# ball = pygame.Surface((100,100))
# ball.fill(RED)
# ball_rect = ball.get_rect(center = (size[0]/2, size[1]/2))

ball1 = point(BLUE)
ball1.point_rect.move()
ball2 = point(RED)
ball3 = point(GREEN)

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
    if counter % 15 == 0:
        ball1.coord_prob()
        ball2.coord_prob()
        ball3.coord_prob()

        ball1.appear_prob(prob)
        ball2.appear_prob(prob)
        ball3.appear_prob(prob)

    screen.blit(ball1.point_surface, ball1.point_rect)  
    screen.blit(ball2.point_surface, ball2.point_rect)  
    #screen.blit(ball3.point_surface, ball3.point_rect)  
    
    # Lines
    
    draw_grid(hor_array, vert_array)

    
        
    
    
    pygame.display.flip()
    
    
    clock.tick(60)

    
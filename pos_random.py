import itertools
import pygame, sys, random
from pygame.locals import *

##Inits and constants

pygame.init()
pygame.mixer.init()
pygame.font.init()


EDGE = 2000

BLACK = (0,0,0)
GREY = (211,211,211)

RED = (222, 49, 99)
ORANGE = (255, 127, 80)
YELLOW = (255, 191, 0)
YEGREEN = (223, 255, 0)
GREEN = (159, 226, 191)
CYAN  = (64, 224, 208)
BLUE = (100, 149, 237)
PURPLE = (204, 204, 255)

color_list = [ RED, ORANGE, YELLOW, YEGREEN, GREEN, CYAN, BLUE, PURPLE]


############## MATH STUFF

print("set an n value less than 100\n")
### Variables
num_squares = input()
num_squares = int(num_squares)



## Compute subsquares
sub_squares = num_squares * num_squares

print("set a positive λ \n")
#Set lambda
tolerance = input()
tolerance = int(tolerance)  # Something positive
prob = tolerance / sub_squares

# calculate offset of squares
offset = EDGE / num_squares
point_size = ( offset/5 , offset/5)


# num of coordinates
number_lines = (num_squares - 1) * 2
number_coord = number_lines 

# Generate 
size = [EDGE, EDGE]

hor_array = [(0,0) for row in range(number_coord)] 
vert_array = [(0,0) for row in range(number_coord)] 


x_delta = EDGE / num_squares
y_delta = EDGE / num_squares


# horizontal 


# Function to make the horiztional lines
def hor_lines(x_delta, hor_array):
    counter = 0
    add_x = 0
    add_x = add_x + x_delta
    for x in range(len(hor_array)):
        if counter  == 0:
            hor_array[x] = (add_x,0)
            counter += 1
        elif counter  == 1:
            hor_array[x] = (add_x, EDGE)
            counter += 1
        else:   
            add_x = add_x + x_delta
            hor_array[x] = (add_x,0)
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
            counter += 1
        elif counter  == 1:
            vert_array[y] = (EDGE, add_y)
            counter += 1
        else:
            add_y = add_y + y_delta
            vert_array[y] = (0,add_y)
            counter = 1
    return vert_array

hor_array = hor_lines(x_delta, hor_array)
vert_array = vert_lines(y_delta, vert_array)

def draw_grid(hor_array, vert_array): 
    length = len(hor_array) - 1
    length = int(length) 

    for i in range(len(hor_array)):
        if i < length and i % 2 == 0:
            pygame.draw.line(screen, GREY, hor_array[i], hor_array[i+1], 3)
        
    for i in range(len(vert_array)):
        if i < length and i % 2 == 0:
            pygame.draw.line(screen, GREY, vert_array[i], vert_array[i+1], 3)  


class point():
    def __init__(self, offset, centers, prob):
        self.point_surface = pygame.Surface(point_size)
        self.beep = sound
        self.beep.set_volume(0.5)
        self.prob = prob
        self.offset = offset
        self.center = centers
        self.point_rect = self.point_surface.get_rect( center =self.center) #(self.x,self.y)
        
        if EDGE / 2 == offset:
            if self.point_rect.y < offset:
                self.color = color_list[0]
            elif self.point_rect.y >= offset:
                self.color = color_list[1]
            self.point_surface.fill(self.color)
        elif EDGE / 3 == offset:
            if self.point_rect.y < offset:
                self.color = color_list[0]
            elif 2 * offset > self.point_rect.y >= offset:
                self.color = color_list[1]
            elif self.point_rect.y >= 2* offset:
                self.color = color_list[2]
            self.point_surface.fill(self.color)            
        elif EDGE / 4 == offset: # TO DO 
            if self.point_rect.y < offset:
                self.color = BLUE
            elif 2 * offset > self.point_rect.y >= offset:
                self.color = RED
            elif offset * 3 > self.point_rect.y >= 2 * offset:
                self.color = GREEN
            elif self.point_rect.y >= 3 * offset:
                self.color = color_list[3]
            self.point_surface.fill(self.color)
        elif EDGE / 5 == offset: # TO DO 
            if self.point_rect.y < offset:
                self.color = color_list[0]
            elif 2 * offset > self.point_rect.y >= offset:
                self.color = color_list[1]
            elif offset * 3 > self.point_rect.y >= 2* offset:
                self.color = color_list[2]
            elif offset * 4 > self.point_rect.y >= 3 * offset:
                self.color = color_list[3]
            elif self.point_rect.y >= offset * 4:
                self.color = color_list[4]
            self.point_surface.fill(self.color)
        elif EDGE / 6 == offset: # TO DO 
            if self.point_rect.y < offset:
                self.color = color_list[0]
            elif 2 * offset > self.point_rect.y >= offset:
                self.color = color_list[1]
            elif offset * 3 > self.point_rect.y >= 2* offset:
                self.color = color_list[2]
            elif offset * 4 > self.point_rect.y >= 3 * offset:
                self.color = color_list[3]
            elif offset * 5 > self.point_rect.y >= offset * 4:
                self.color = color_list[4]
            elif self.point_rect.y >= offset * 5:
                self.color = color_list[5]
            self.point_surface.fill(self.color)
        elif EDGE / 7 == offset: # TO DO 
            if self.point_rect.y < offset:
                self.color = color_list[0]
            elif 2 * offset > self.point_rect.y >= offset:
                self.color = color_list[1]
            elif offset * 3 > self.point_rect.y >= 2* offset:
                self.color = color_list[2]
            elif offset * 4 > self.point_rect.y >= 3 * offset:
                self.color = color_list[3]
            elif offset * 5 > self.point_rect.y >= offset * 4:
                self.color = color_list[4]
            elif offset * 6 > self.point_rect.y >= offset * 5:
                self.color = color_list[5]
            elif self.point_rect.y >= offset * 6:
                self.color = color_list[6]
            self.point_surface.fill(self.color)
        elif EDGE / 8 == offset: # TO DO 
            if self.point_rect.y < offset:
                self.color = color_list[0]
            elif 2 * offset > self.point_rect.y >= offset:
                self.color = color_list[1]
            elif offset * 3 > self.point_rect.y >= 2* offset:
                self.color = color_list[2]
            elif offset * 4 > self.point_rect.y >= 3 * offset:
                self.color = color_list[3]
            elif offset * 5 > self.point_rect.y >= offset * 4:
                self.color = color_list[4]
            elif offset * 6 > self.point_rect.y >= offset * 5:
                self.color = color_list[5]
            elif offset * 7 >self.point_rect.y >= offset * 6:
                self.color = color_list[6]
            elif self.point_rect.y > offset * 7:
                self.color = color_list[7]                
            self.point_surface.fill(self.color)
        elif EDGE / 8 > offset:
            if self.point_rect.y < EDGE / 8:
                self.color = color_list[0]
            elif 2 * EDGE / 8 > self.point_rect.y >= EDGE / 8:
                self.color = color_list[1]
            elif EDGE / 8 * 3 > self.point_rect.y >= 2* EDGE / 8:
                self.color = color_list[2]
            elif EDGE / 8 * 4 > self.point_rect.y >= 3 * EDGE / 8:
                self.color = color_list[3]
            elif EDGE / 8 * 5 > self.point_rect.y >= EDGE / 8 * 4:
                self.color = color_list[4]
            elif EDGE / 8 * 6 > self.point_rect.y >= EDGE / 8 * 5:
                self.color = color_list[5]
            elif EDGE / 8 * 7 >self.point_rect.y >= EDGE / 8 * 6:
                self.color = color_list[6]
            elif self.point_rect.y >= EDGE / 8 * 7:
                self.color = color_list[7]                            
            self.point_surface.fill(self.color)
    
   # prob of appearing as a function of the probability  
    def appear_prob(self):
        rand_num = random.random()
        
        if  rand_num > self.prob:
            self.point_surface.fill(BLACK)
        if rand_num < self.prob:
            self.point_surface.fill(self.color)
            # pygame.mixer.find_channel(True).play(self.beep)
            
            
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

    

# function to compute the center of squares using edge length and number of squares    
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


centers = []
for subsets in itertools.product(x_centers, x_centers):
    centers.append(subsets)

#function to translate squares along grid
def translate_squares(num_squares, offset):
    translations = []
    for x_offset in range(num_squares):
        for y_offset in range(num_squares):
            translations += [(x_offset * offset,y_offset * offset)]
    return translations
        
translations = translate_squares(num_squares, offset)
   
            
# display stuff
title = "Poisson Tiling with λ = %f and n = %2f" % (tolerance ,num_squares)
pygame.display.set_caption(title)
screen = pygame.display.set_mode(size = size)
screen.fill('BLACK')

# Sound stuff
pygame.mixer.set_num_channels(int(sub_squares))
sound = pygame.mixer.Sound(file = "beep.wav")


#Font stuff


#list of objects iterated by the centers
ball_box = []
for i in centers:
    ball_box.append(point(offset, i, prob))
    
    

    

# Game loop
counter = 0 
running = True
clock = pygame.time.Clock()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.mixer.quit()
            pygame.font.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                pygame.mixer.quit()
                pygame.font.quit()
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

    # Draw the gridlines
    
    draw_grid(hor_array, vert_array)     
    
    pygame.display.flip()
    
    
    clock.tick(60)

    
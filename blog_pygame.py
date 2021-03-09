import pygame
import random
from blob import Blob
import numpy as np

STARTING_BLUE_BLOBS = 10
BLUE_MAX_XY_SIZE = (4,8)
BLUE_MOVEMENT_RANGE = (-2,3,-2,3) # non-inclusive of the largest number
BLUE_OVERBOUND = 2

STARTING_RED_BLOBS = 10
RED_MAX_XY_SIZE = (4,8)
RED_MOVEMENT_RANGE = (-2,3,-2,3)
RED_OVERBOUND = 5

STARTING_GREEN_BLOBS = 10
GREEN_MAX_XY_SIZE = (4,8)
GREEN_MOVEMENT_RANGE = (-1,2,-1,2)
GREEN_OVERBOUND = 5

DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 200
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
game_caption = pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class BlueBlob(Blob):
    def __init__(self, x_boundary, y_boundary, size_range, movement_range, overbound=0):
        Blob.__init__(self, BLUE, x_boundary, y_boundary, size_range, movement_range, overbound=0)
    
    def __add__(self, other_blob):
        if other_blob.color == RED:
            self.size -= (other_blob.size * .01)
            other_blob.size += self.size * .01

        elif other_blob.color == GREEN:
            self.size += other_blob.size
            other_blob.size = 0

        elif other_blob.color == BLUE:
            pass

        else:
            raise Exception('Adding function failed.')

class RedBlob(Blob):
    def __init__(self, x_boundary, y_boundary, size_range, movement_range, overbound=0):
        Blob.__init__(self, RED, x_boundary, y_boundary, size_range, movement_range, overbound=0)

class GreenBlob(Blob):
    def __init__(self, x_boundary, y_boundary, size_range, movement_range, overbound=0):
        Blob.__init__(self, GREEN, x_boundary, y_boundary, size_range, movement_range, overbound=0)

def draw_environment(blob_list):
    game_display.fill(WHITE)
    blue_blobs, red_blobs, green_blobs = blob_list
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.checkbounds()
            collision_iterator(blue_blobs, red_blobs, green_blobs, blob_list)
    pygame.display.update()

def collision_iterator(b1, b2, b3, blob_list):
    for b1_id, b1_item in b1.copy().items():
        for blob_dict in blob_list.copy():
            for blob_id, blob_item in blob_dict.copy().items():
                if blob_item == b1_item:
                    pass
                else:
                    if collision(b1_item, blob_item):
                    # if pygame.sprite.collide_rect(blue_item, blob_item):
                        if blob_item.color == RED:
                            b1_item + blob_item
                        if blob_item.color == GREEN:
                            b1_item + blob_item 
    
def collision(b1, b2):
    return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)


def main():
    blue_blobs = dict(enumerate([BlueBlob(DISPLAY_WIDTH, DISPLAY_HEIGHT, BLUE_MAX_XY_SIZE, BLUE_MOVEMENT_RANGE, BLUE_OVERBOUND) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(DISPLAY_WIDTH, DISPLAY_HEIGHT, RED_MAX_XY_SIZE, RED_MOVEMENT_RANGE, RED_OVERBOUND) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(DISPLAY_WIDTH, DISPLAY_HEIGHT, GREEN_MAX_XY_SIZE, GREEN_MOVEMENT_RANGE, GREEN_OVERBOUND) for i in range(STARTING_GREEN_BLOBS)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs, green_blobs])
        clock.tick(60)

if __name__ == '__main__':
    main()

# Map drawing
from constants import tile_size


def draw(lvl, images, screen):
    num_line = 0
    for line in lvl.maze_map:
        num_column = 0
        for case in line:
            img_pos = [num_column * tile_size, num_line * tile_size]
            if case == "#":
                screen.blit(images.brick, img_pos)

            num_column += 1
        num_line += 1

# Map drawing
import pygame
from constants import tile_size, Win, Lost


def draw(lvl, mac_gyver, images, screen):
    """Draws the graphics of the game"""
    num_line = 0
    for line in lvl.maze_map:
        num_column = 0
        for case in line:
            img_pos = [num_column * tile_size, num_line * tile_size]

            if case == "#":
                screen.blit(images.brick, img_pos)
            else:
                screen.blit(images.floor, img_pos)

            if case == "." and mac_gyver.status != Win:
                screen.blit(images.guardian, img_pos)

            num_column += 1
        num_line += 1
    if mac_gyver.status != Lost:
        screen.blit(images.mac_gyver, mac_gyver.pixel_position)

    for item in lvl.items:
        if lvl.items[item].show:
            screen.blit(images.items[item], lvl.items[item].pixel_position)

    pygame.display.flip()

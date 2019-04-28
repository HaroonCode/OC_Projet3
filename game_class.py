from random import randint
from constants import *


class Level:
    # Contain maze map and items.
    def __init__(self, maze_map, items):
        self.maze_map = maze_map
        self.items = {}
        for item in items:
            self.items[item] = Item(self.random_position())

    def random_position(self):
        # Random item position in map.
        pos_x = 0
        pos_y = 0
        while self.maze_map[pos_y][pos_x] != " ":
            pos_x = randint(0, (map_lenght - 1))
            pos_y = randint(0, (map_height - 1))
        self.maze_map[pos_y][pos_x] = "*"
        return pos_x, pos_y


class Item:
    # Item class
    def __init__(self, position):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.show = True


class Character:
    # Character
    def __init__(self, lvl):
        self.lvl = lvl
        self.reset()

    def reset(self):
        # Initial position of the character (top left)
        self.pos_y, self.pos_x = (1, 1)
        self.num_items = 0

    def move_to(self, direction):
        # move the character
        if direction == left:
            self.pos_x -= 1
        elif direction == right:
            self.pos_x += 1
        elif direction == up:
            self.pos_y -= 1
        elif direction == down:
            self.pos_y += 1
        else:
            print("error: direction")
        self._collect_items()

    def _collect_items(self):
        # Collect an item
        for item in self.lvl.items:
            if (self.lvl.items[item].pos_x == self.pos_x and
                    self.lvl.items[item].pos_y == self.pos_y and
                    self.lvl.items[item].show):
                self.num_items += 1
                self.lvl.items[item].show = False

    def status(self):
        if self.lvl.maze_map[self.pos_y][self.pos_x] == '.':
            if self.num_items == len(self.lvl.items):
                return True
            else:
                return False

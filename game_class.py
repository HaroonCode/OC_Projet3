from random import randint
from constants import *


class Level:
    # Contain maze map and items.
    def __init__(self, maze_map, items):
        self.maze_map = maze_map
        self.items = {}
        for item in items:
            self.items[item] = Item(self.random_position())

    def reset(self):
        # Place random items
        for item in self.items:
            self.maze_map[self.items[item].pos_y][self.items[item].pos_x] = " "
            self.items[item] = Item(self.random_position())

    def free_path(self, pos_x, pos_y, direction):
        # Check if it's a valid path.
        return (direction == left and pos_x > 0 and
                self.maze_map[pos_y][pos_x-1] != "#" or
                direction == right and pos_x < (map_length - 1) and
                self.maze_map[pos_y][pos_x+1] != "#" or
                direction == up and pos_y > 0 and
                self.maze_map[pos_y-1][pos_x] != "#" or
                direction == down and pos_y < (map_height - 1) and
                self.maze_map[pos_y+1][pos_x] != "#")

    def random_position(self):
        # Random item position in map.
        pos_x = 0
        pos_y = 0
        while self.maze_map[pos_y][pos_x] != " ":
            pos_x = randint(0, (map_length - 1))
            pos_y = randint(0, (map_height - 1))
        self.maze_map[pos_y][pos_x] = "*"
        return pos_x, pos_y


class Item:
    # Item class
    def __init__(self, position):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.show = True

    @property
    def pixel_position(self):
        # Pixel position of item
        return [self.pos_x * tile_size, self.pos_y * tile_size]


class Character:
    # Character
    def __init__(self, lvl, items):
        self.lvl = lvl
        self.reset()
        self.item_msg = {}
        for item in items:
            self.item_msg[item] = items[item].get("msg")  # returns None if not set

    def reset(self):
        # Initial position of the character (top left)
        self.pos_y, self.pos_x = self._initial_position(self.lvl)
        self.num_items = 0

    def move_to(self, direction):
        if self.lvl.free_path(self.pos_x, self.pos_y, direction):
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
                if self.item_msg[item] != None:
                    print(self.item_msg[item])

    @classmethod
    def _initial_position(cls, lvl):
        """Get initial character's position from the maze_map"""
        num_line = 0
        for line in lvl.maze_map:
            num_column = 0
            for case in line:
                if case == "@":
                    return num_line, num_column
                num_column += 1
            num_line += 1
        print("Initial character's position not found")

    @property
    def pixel_position(self):
        # pixel position of the character
        return [self.pos_x * tile_size, self.pos_y * tile_size]

    #@property
    def status(self):
        # Character status - Win or loose
        if self.lvl.maze_map[self.pos_y][self.pos_x] == '.':
            if self.num_items == len(self.lvl.items):
                return WIN
            return LOST
        return IN_MAZE

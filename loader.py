# Loader used to load all physical contant i needed (block, image etc...)
import json
import pygame


class Images:

    # Load image
    def __init__(self, config):
        self.brick = self.load_image(config["bloc"])
        self.mac_gyver = self.load_image(config["mac_gyver"])
        self.guardian = self.load_image(config["guardian"])
        self.items = {}
        for item in config["items"]:
            self.items[item] = self.load_image(config["items"][item]["img"])

    @classmethod
    def load_image(cls, filename):
        return pygame.image.load(filename).convert_alpha()


def map_from_file(filename):
    # load map from file
    with open(filename, "r") as map_file:
        # we will need to modify the map when placing items, so we change it to a double list
        maze_map = [list(line) for line in map_file]
    return maze_map


def load_json(filename):
    # load json
    with open(filename) as data:
        return json.load(data)


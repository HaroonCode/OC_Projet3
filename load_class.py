#Contain all project class.

# Create the player class for the movement
class Player:
    x = 44
    y = 44
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed


# Create the Maze
class Maze:
    def __init__(self):
        self.latitude = 10 # Attribut plus parlant
        self.longitude = 8
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]


# Change the maze to be dynamic.
# First we need to create the map with case

class MapGeneration:
    def __init__(self,longitude,latitude,widthspace):
        self.longitude = longitude
        self.latitude = latitude
        self.widthspace = widthspace

    def GenMaze:
        for longitutde in range(self.longitude)
            

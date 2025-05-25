import pygame
from game_manager.gameloop import *
pygame.init()

if __name__ == "__main__":
    gameLoop = GameLoop()
    gameLoop.run()

import pygame
from constants import *
from player import *

def main():
  pygame.init
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)

  player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for each in updatable:
      each.update(dt)

    screen.fill("black")

    for each in drawable:
      each.draw(screen)
 
    pygame.display.flip()

    dt = (clock.tick(60))/1000

if __name__ == "__main__":
  main()
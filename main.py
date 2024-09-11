import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  pygame.init
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)


  player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()



  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for each in updatable:
      each.update(dt)
    for asteroid in asteroids:
      if asteroid.detectCollision(player):
        print("Game Over!")
        sys.exit()
        return
      for shot in shots:
        if asteroid.detectCollision(shot):
          asteroid.split()
          shot.kill()

    screen.fill("black")

    for each in drawable:
      each.draw(screen)
 
    pygame.display.flip()

    dt = (clock.tick(60))/1000

if __name__ == "__main__":
  main()